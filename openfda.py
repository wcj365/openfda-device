import json
import requests
import pandas as pd

def get_data(specialty):
    if specialty == None:
        url = "https://api.fda.gov/device/classification.json?limit=1000&skip="
    else:
       url = f"https://api.fda.gov/device/classification.json?search=medical_specialty_description:{specialty}&limit=1000&skip="

    i = 0
    contents = []
    while True:
        skip = i * 1000
        resp = requests.get(url + str(skip))
        json_resp = json.loads(resp.text)
        contents += json_resp["results"]
        total = int(json_resp["meta"]["results"]["total"])
        i = i + 1
        if total < 1000 * i:
            break

    return pd.DataFrame(contents)     
