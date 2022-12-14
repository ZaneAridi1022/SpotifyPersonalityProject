import ast
from typing import List
import spotipy
import requests
import pandas as pd
import os
import openpyxl
from operator import itemgetter
import json
import time
import pathlib

def get_streamings(path: str = 'alex@gmail_com') -> List[dict]:

    files = [pathlib.PurePath(path, x) for x in os.listdir(path)
             if x.split('.')[0][:-1] == 'StreamingHistory']

    all_streamings = []
    totalTimeByTrack = {}

    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            new_streamings = ast.literal_eval(f.read())
            for streaming in new_streamings:
                if streaming['trackName'] in totalTimeByTrack:
                    totalTimeByTrack[streaming['trackName']] += round(streaming['msPlayed']/60000)
                else:
                    totalTimeByTrack[streaming['trackName']] = round(streaming['msPlayed']/60000)
                all_streamings.append(streaming)
    return totalTimeByTrack

def get_streamings_given_jsons(files):
    all_streamings = []
    totalTimeByTrack = {}

    for file in files:
        new_streamings = json.load(file)
        for streaming in new_streamings:
            if streaming['trackName'] in totalTimeByTrack:
                totalTimeByTrack[streaming['trackName']] += round(streaming['msPlayed']/60000)
            else:
                totalTimeByTrack[streaming['trackName']] = round(streaming['msPlayed']/60000)
            all_streamings.append(streaming)

    return totalTimeByTrack

def get_id(track_name: str, token: str) -> str:
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [
    ('q', track_name),
    ('type', 'track'),
    ]
    response = None
    try:
        response = requests.get('https://api.spotify.com/v1/search',
                    headers = headers, params = params,timeout=10)
        print(response)
        json = response.json()
        
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except Exception as json:
        print(json)
        print(response.headers['retry-after'])
        return int(response.headers['retry-after'])


def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None

def trim_features(features: dict) -> dict:
    if features is None:
        return None
    trimFeat = {}
    KEYS = ['key','time_signature','danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
    for key,value in features.items():
        if key in KEYS:
            trimFeat[key] = value
    return trimFeat

def get_final_feature_values(streamingData,token,topX,sortedListByStreamingTimes):

    ffv = {}
    featuresKeyValues = {}
    featuresTSValues = {}
    for streamingName, timePlayed in streamingData.items():
        # Remove any song info that is not in the top topx = 50% (1-.5) of listened data
        if timePlayed < sortedListByStreamingTimes[topX]:
            continue
        
        ID = get_id(streamingName, token)
        if type(ID) is int:
            time.sleep(ID)
        
        features = trim_features(get_features(ID, token))
        if features is None:
            continue
        # get a single representative data point for each value in features
        for key, value in features.items():
            if key != 'key' and key != 'time_signature':
                if key in ffv:
                    ffv[key][0] += value * timePlayed
                    ffv[key][1] += timePlayed
                else:
                    ffv[key] = [value * timePlayed, timePlayed]
            else:
                if key == 'key':
                    if value in featuresKeyValues:
                        featuresKeyValues[value] += timePlayed
                    else:
                        featuresKeyValues[value] = timePlayed
                if key == 'time_signature':
                    if value in featuresTSValues:
                        featuresTSValues[value] += timePlayed
                    else:
                        featuresTSValues[value] = timePlayed
    t1 = sorted([(key, value) for key, value in featuresKeyValues.items()],
                key=itemgetter(1))
    t2 = sorted([(key, value) for key, value in featuresTSValues.items()],
                key=itemgetter(1))
    ffv['key'] = t1[-1]
    ffv['time_signature'] = t2[-1]
    dance = ffv['danceability'][0] / ffv['danceability'][1]
    energy = ffv['energy'][0] / ffv['energy'][1]
    key = ffv['key'][0]
    loud = ffv['loudness'][0] / ffv['loudness'][1]
    speech = ffv['speechiness'][0] / ffv['speechiness'][1]
    ts = ffv['time_signature'][0]
    acoust = ffv['acousticness'][0] / ffv['acousticness'][1]
    inst = ffv['instrumentalness'][0] / ffv['instrumentalness'][1]
    life = ffv['liveness'][0] / ffv['liveness'][1]
    val = ffv['valence'][0] / ffv['valence'][1]
    tempo = ffv['tempo'][0] / ffv['tempo'][1]
    return [
        round(dance, 2),
        round(energy, 2), key,
        round(loud, 1),
        round(speech, 2),
        round(acoust, 3),
        round(inst, 2),
        round(life, 3),
        round(val, 2),
        round(tempo), ts
    ]

def connect_to_Spotify(username = 'qut9zcs5mbfdmc5cykwudcjtj',
                       client_id = '248c415c42004414acfa6cc8fe305bc3',
                       client_secret = 'acb2bbbec3184747b5851fa482419ade',
                       redirect_url = 'http://localhost:7777/callback',
                       scope = 'user-read-recently-played') :

    token = spotipy.util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_url)
    return token

def get_upper_bound(streamingData):
    sortedListByStreamingTimes = sorted([x for x in streamingData.values()])
    return int(len(sortedListByStreamingTimes)*.75),sortedListByStreamingTimes

def write_to_excel(identifier,final_data):
    dest = r"SpotifyPersonalityDataset.xlsx"
    wb = openpyxl.load_workbook(dest)
    sheet = wb.worksheets[0]
    row_count = sheet.max_row

    currData = pd.read_excel(dest)

    currData.loc[row_count] = [identifier]+final_data

    currData.to_excel(dest, index=False)

def main(files = None):
    menu_selection = 0
    if files is not None:
        menu_selection = 2
    else:
        menu_selection = 1
    token = connect_to_Spotify()
    
    if menu_selection != 1 and menu_selection != 2:
        print('Invalid option.')
        return

    list_of_repos = []
    personality_dict = dict()
    if menu_selection == 1:
        # from GetPersonalityData import personality_dictionary
        # personality_dict = personality_dictionary()
        list_of_repos = os.listdir(pathlib.Path('UserSpotifyData'))
    else:
        list_of_repos = ['grunew14@msu_edu']
    
    for repo in list_of_repos:
        streamingData = {}
        if menu_selection == 1:
            streamingData = get_streamings(pathlib.PurePath('UserSpotifyData',repo))
        elif menu_selection == 2:
            streamingData = get_streamings_given_jsons(files)
        topX, sortedListByStreamingTimes = get_upper_bound(streamingData)
        final_feature_values = get_final_feature_values(streamingData,token,topX,sortedListByStreamingTimes)
        if menu_selection == 2:
            return final_feature_values
        person_dictionary_index = repo.replace('_','.')
        bigFive = personality_dict[person_dictionary_index]
        
        write_to_excel(repo[:2],final_feature_values+bigFive)

    return

# main()

