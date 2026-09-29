import requests
import random

parameters = {
    "amount": random.randint(1, 50),
    "type": "boolean",
}

response = requests.get(url=f"https://opentdb.com/api.php?amount={random.randint(1, 50)}&type=boolean",
                        params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
