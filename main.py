import requests
from dotenv import load_dotenv
import os

load_dotenv()
covid_api = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces'
result = requests.get(covid_api).json()
#province bangkok
data = result[1]

token = os.getenv("TOKEN")
msg = f"""
π Daily Report: {data["txn_date"]}
πΉπ­ Province : Bangkok
π¨ New Cases: {data["new_case"]} 
π¦ Total Cases: {data["total_case"]}
π New Deaths: {data["new_death"]}
β  Total Deaths: {data["total_death"]}
"""

headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
url = 'https://notify-api.line.me/api/notify'

r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)