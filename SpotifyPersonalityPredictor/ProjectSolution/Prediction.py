from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
import os

MODEL_MAPPING = {'lr':LinearRegression(),'xgb':XGBClassifier(),'gnb':GaussianNB()}
def trainAndMakePrediction(x_in,y_in,model,encoder=False,trainOrPredict='train',manualTest=None):
    trainOrPreictMap = {'train':(.2,.8),'predict':(0,1)}

    test_siz, train_siz = trainOrPreictMap[trainOrPredict]
    X_train, X_test, y_train, y_test = train_test_split(x_in,y_in,test_size=.2,train_size=.8)
    if encoder:
        le = LabelEncoder()
        y_train = le.fit_transform(y_train)
    # print('\nXtrain: ', X_train)
    # print('\nYtrain: ', y_train)
    model.fit(X_train, y_train)

    if manualTest is not None:
        X_test,y_test = manualTest

    prediction = model.predict(X_test)

    # score = model.score(X_test, y_test)
    return prediction,y_test
    # print('\nAccuracy Score: ',score)


def reShape(y_in):
    y_out = []
    rows = len(y_in)
    cols = len(y_in[0])
    for n in range(cols):
        y_out.append([0]*rows)

    for i in range(rows):
        for j in range(cols):
            y_out[j][i] = y_in[i][j]

    return y_out

def testingMode(x_in,y_in):
    print('x_in: ', x_in)
    print('\ny_in: ', y_in)

    # Linear Regression Model
    print('\nLinear Regression: ')
    LR = LinearRegression()
    prediction, y_test = trainAndMakePrediction(x_in, y_in, LR)

    print('\nPrediction: ',prediction)
    print('\nActual: ',y_test)

    # Naive Bayes Model
    print('\nNiave Bayes: ')
    gnbOutput = []
    testOutput = []
    for y in reShape(y_in):
        gnb = GaussianNB()
        prediction, test = trainAndMakePrediction(x_in, y, gnb)
        gnbOutput.append(prediction)
        testOutput.append(test)

    print('\nPrediction: ', gnbOutput)
    print('\nActual: ', testOutput)

    # XGBoost Model
    print('\nXGBoost: ')
    xgbOutput = []
    testOutput = []
    for y in reShape(y_in):
        xgb = XGBClassifier()
        prediction, test = trainAndMakePrediction(x_in, y, xgb, True)
        xgbOutput.append(prediction)
        testOutput.append(test)

    print('\nPrediction: ', xgbOutput)
    print('\nActual: ', testOutput)

    # Decision Tree Model
    print('\nDecision Tree: ')
    dt = DecisionTreeClassifier()
    prediction, y_test = trainAndMakePrediction(x_in, y_in, dt)

    print('\nPrediction: ', prediction)
    print('\nActual: ', y_test)

    # Random Forest Model
    print('\nRandom Forest: ')
    rf = RandomForestClassifier()
    prediction, y_test = trainAndMakePrediction(x_in, y_in, rf)

    print('\nPrediction: ', prediction)
    print('\nActual: ', y_test)

    # Gradient Boost Model
    print('\nGradient Boost: ')
    gbOutput = []
    testOutput = []
    for y in reShape(y_in):
        gb = GradientBoostingClassifier()
        prediction, test = trainAndMakePrediction(x_in, y, gb)
        gbOutput.append(prediction)
        testOutput.append(test)

    print('\nPrediction: ', gbOutput)
    print('\nActual: ', testOutput)

def SpotifyModel(predictionData=None):
    dest = r"SpotifyPersonalityDataset.xlsx"
    assert os.path.isfile(dest)

    currData = pd.read_excel(dest)

    # Parameters
    x_in = currData.drop('User_ID', 1).drop('Extraversion', 1).drop(
        'Agreeableness', 1).drop('Conscientiousness',
                                1).drop('Neuroticism', 1).drop('Openness',
                                                                1).values.tolist()

    # Outputs
    y_in = currData.drop('User_ID', 1).drop('Danceability', 1).drop(
        'Energy',
        1).drop('Key', 1).drop('Loudness', 1).drop('Speechiness', 1).drop(
            'Acousticness',
            1).drop('Instrumentalness',
                    1).drop('Liveness',
                            1).drop('Valence',
                                    1).drop('Tempo', 1).drop('Time_Signature',
                                                            1).values.tolist()

    if predictionData is None:
        testingMode(x_in,y_in)
    else:
        rf = RandomForestClassifier()
        return trainAndMakePrediction(x_in,
                                      y_in,
                                      rf,
                                      trainOrPredict='predict',
                                      manualTest=predictionData)

SpotifyModel()