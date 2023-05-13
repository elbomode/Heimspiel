import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from pathlib import Path


def Altersklassen(lines,path):
    baseUrl = lines[0] + "/age-list/"
    path = path / "Stammdaten"
    file = "Altersklassen.csv"

    response = requests.get(
        baseUrl,
        auth=HTTPBasicAuth(lines[1], lines[2])
    )
    data = response.json()

    # print(response.status_code)

    # print(type(data))
    # print(data)
    df = pd.json_normalize(data)
    df.reset_index(drop=True)

    path.mkdir(parents=True, exist_ok=True)

    df.to_csv(path / file,index=False)

def Wettbewerbsliste(lines,path):
    baseUrl = lines[0] + "competition-list/sp1/"
    path = path / "Stammdaten"
    file = "Wettbewerbsliste.csv"

    response = requests.get(
        baseUrl,
        auth=HTTPBasicAuth(lines[1], lines[2])
    )
    data = response.json()

    # print(response.status_code)

    # print(type(data))
    print(data)
    df = pd.json_normalize(data,record_path="competition")
    df.reset_index(drop=True)

    path.mkdir(parents=True, exist_ok=True)

    df.to_csv(path / file,index=False)