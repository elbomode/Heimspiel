import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from pathlib import Path


def Altersklassen(lines,path):
    baseUrl = lines[0] + "/age-list/"
    path = path / "Stammdaten"
    file = "Altersklassen.csv"
    print(baseUrl)
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
    baseUrl = lines[0] + "/competition-list/sp1/"
    path = path / "Stammdaten"
    file = "Wettbewerbsliste.csv"

    response = requests.get(
        baseUrl,
        auth=HTTPBasicAuth(lines[1], lines[2])
    )
    data = response.json()

    # print(response.status_code)

    # print(type(data))
    # print(data)
    df = pd.json_normalize(data,record_path="competition")
    df.reset_index(drop=True)

    path.mkdir(parents=True, exist_ok=True)

    df.to_csv(path / file,index=False)

def Länderliste(lines,path):
    baseUrl = lines[0] + "/country-list/"
    path = path / "Stammdaten"
    file = "Länderliste.csv"

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

def Eventtypen(lines,path):
    baseUrl = lines[0] + "/match-event-type/sp1/"
    path = path / "Stammdaten"
    file = "Eventtypen.csv"

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

    df.to_csv(path / file, index=False)

def SaisonsProWettbewerb(lines, path):

    # Leeren Dataframe für die Competitions erzeugen
    SaisonsProWettbewerb_df = pd.DataFrame()

    competitions = pd.read_csv(str(path) + "\Stammdaten\Wettbewerbsliste.csv")

    path = path / "Stammdaten"

    # print(competitions.to_string())

    for i in competitions['id'].unique():

        baseUrl = lines[0] + "/seasons-by-competition/co" + str(i) + "/"
        # print(baseUrl)

        file = "SaisonsProWettbewerb.csv"

        response = requests.get(
            baseUrl,
            auth=HTTPBasicAuth(lines[1], lines[2])
        )
        data = response.json()

        # print(response.status_code)

        # print(type(data))
        # print(data[0]["competition"][0]["season"])
        df = pd.json_normalize(data[0]["competition"][0]["season"])
        df["competition_id"]=str(i)
        # print(df)
        df.reset_index(drop=True)

        SaisonsProWettbewerb_df = pd.concat([SaisonsProWettbewerb_df, df])


    path.mkdir(parents=True, exist_ok=True)

    SaisonsProWettbewerb_df.to_csv(path / file, index=False)
