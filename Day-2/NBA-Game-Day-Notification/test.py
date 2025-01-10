import os
import json
import requests
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    # Get environment variables
    api_key = os.getenv("soccer_key")

response = requests.get("https://api.sportsdata.io/v3/nba/scores/json/Standings/?key{api_key}")
print(response.json())
