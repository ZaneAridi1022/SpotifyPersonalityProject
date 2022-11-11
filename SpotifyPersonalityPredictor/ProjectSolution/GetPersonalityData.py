from Google import create_service


def get_personality(index, Overall_Personality):
    Personality1 = []
    Extraversion = 0
    Agreeableness = 0
    Conscientiousness = 0
    Neuroticism = 0
    Openness_to_Experience = 0
    for j in range(len(Overall_Personality[index])):
        if j == 0:
            Extraversion += 6 - Overall_Personality[index][j]
        elif j == 1:
            Agreeableness += Overall_Personality[index][j]
        elif j == 2:
            Conscientiousness += 6 - Overall_Personality[index][j]
        elif j == 3:
            Neuroticism += 6 - Overall_Personality[index][j]
        elif j == 4:
            Openness_to_Experience += 6 - Overall_Personality[index][j]
        elif j == 5:
            Extraversion += Overall_Personality[index][j]
        elif j == 6:
            Agreeableness += 6 - Overall_Personality[index][j]
        elif j == 7:
            Conscientiousness += Overall_Personality[index][j]
        elif j == 8:
            Neuroticism += Overall_Personality[index][j]
        elif j == 9:
            Openness_to_Experience += Overall_Personality[index][j]
    Personality1.append(Extraversion)
    Personality1.append(Agreeableness)
    Personality1.append(Conscientiousness)
    Personality1.append(Neuroticism)
    Personality1.append(Openness_to_Experience)
    return Personality1


def personalityss_converter():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    spreadsheet_id = '1YNXtrmp844UWP8q8zVVBZj-kW-o-SVOs887Ct0cTToU'

    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        majorDimension='ROWS',
        range='C:L'  # need to adjust accordingly
    ).execute()

    values_responses = response['values'][1:]
    values_responses1 = []
    for i in range(len(values_responses)):
        values_responses1.append([int(x) for x in values_responses[i]])

    #print(values_responses1)   #THIS IS A CHECKPOINT

    Personality = []
    Overall_Personality = []

    for i in range(len(values_responses1)):
        Overall_Personality.append(get_personality(i, values_responses1))

    return Overall_Personality


def flatten(l):
    return [item for sublist in l for item in sublist]


def personality_dictionary():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    spreadsheet_id = '1YNXtrmp844UWP8q8zVVBZj-kW-o-SVOs887Ct0cTToU'

    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, majorDimension='ROWS',
        range='B:B').execute()

    email_response = response['values']
    email_response = flatten(email_response)[1:]

    person_response = personalityss_converter()

    res = {
        email_response[i]: person_response[i]
        for i in range(len(email_response))
    }
    return res
