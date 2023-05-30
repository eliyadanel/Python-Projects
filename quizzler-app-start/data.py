import requests as rq

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = rq.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
