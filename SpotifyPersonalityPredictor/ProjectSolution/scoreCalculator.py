data = {'Timestamp': '10/28/2022 10:51:04', 'Email Address': 'aswalman@msu.edu', 'questionAnswers': [3, 4, 2, 3, 1, 4, 2, 5, 2, 5]}

key = 10

def quesScoreCalc(quesAns, key):
  return quesAns * key

def revQuesScoreCalc(revQuesAns, key):
  return (6 - revQuesAns) * key

def scoreCalc(quesAns, revQuesAns, key):
  quesScore = quesScoreCalc(quesAns, key)
  revQuesScore = revQuesScoreCalc(revQuesAns, key)
  score = quesScore + revQuesScore
  return score

scores = {
  'Extraversion' : scoreCalc(data["questionAnswers"][5-1], data["questionAnswers"][1-1], key),
  'Agreeableness' : scoreCalc(data["questionAnswers"][2-1], data["questionAnswers"][7-1], key),
  'Conscientiousness' : scoreCalc(data["questionAnswers"][8-1], data["questionAnswers"][3-1], key),
  'Neuroticism' : scoreCalc(data["questionAnswers"][9-1], data["questionAnswers"][4-1], key),
  'Openness' : scoreCalc(data["questionAnswers"][10-1], data["questionAnswers"][5-1], key)
}

print('{:<30s}{:>5s}'.format('Personality Trait', 'Score'), end='\n\n')
for score in scores:
  print('{:<30s}{:>5d}'.format(score, scores[score]))