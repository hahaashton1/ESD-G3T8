import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'N2oXB2loL73OQ87R7yQ50Dicu'
credentials['CONSUMER_SECRET'] = 'LlrU3ZuuoMWaGIFNNDkdLnyUrKSOZSk8x8DLKsPYA5omVXQUo6'
credentials['ACCESS_TOKEN'] = '1238352975132626944-BfCcBHGNpgELefKXTEiwEHHigQ03ec'
credentials['ACCESS_SECRET'] = 'c4E5Mgo7HrY85dXG7wpeYnS5Mow0ZtsMVNXFkkoddT1ZJ'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)