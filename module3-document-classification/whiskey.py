import pandas as pd


files = [
    'data/submission0.csv',
    'data/submission1.csv',
    'data/submission2.csv'
]

submissions = (pd.read_csv(file)[['ratingCategory']] for file in files)
ensemble = pd.concat(submissions, axis='columns')
majority_vote = ensemble.mode(axis='columns')[0]

test = pd.read_csv("data/test.csv")
submission = pd.DataFrame({'id': test['id'], 'ratingCategory': test['id']})
submission['ratingCategory'] = majority_vote.astype('int64')

submission.to_csv('submission-ultra.csv', index=False)