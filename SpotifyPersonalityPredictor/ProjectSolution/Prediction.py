from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import os

dest = r"SpotifyPersonalityDataset.xlsx"
assert os.path.isfile(dest)

currData = pd.read_excel(dest)
x_in = currData.drop('User_ID',1).drop('Extraversion',1).drop('Agreeableness',1).drop('Conscientiousness',1).drop('Neuroticism',1).drop('Openness',1).values.tolist()
y_in = currData.drop('User_ID',1).drop('Danceability',1).drop('Energy',1).drop('Key',1).drop('Loudness',1).drop('Speechiness',1).drop('Acousticness',1).drop('Instrumentalness',1).drop('Liveness',1).drop('Valence',1).drop('Tempo',1).drop('Time_Signature',1).values.tolist()
print('x_in: ',x_in)
print('\ny_in: ',y_in)

X_train, X_test, y_train, y_test = train_test_split(x_in,y_in)

LR = LinearRegression()
LR.fit(X_train, y_train)

prediction = LR.predict(X_test)

print('\nPrediction: ',prediction)

score = LR.score(X_test,y_test)
print('\nAccuracy Score: ',score)