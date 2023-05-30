import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import glob

def ResolveListwithindf(spaltennamen,dataframe):
    dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
    map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
    for blub in map_blub:
        dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
    dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
    return dataframe

def ExplodeResolveListwithindf(spaltennamen,dataframe):
    dataframe = dataframe.explode(spaltennamen)
    dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
    map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
    for blub in map_blub:
        dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
    dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
    return dataframe

def bestandAusSpalte(path,spalte):
    blub = []

    for f in glob.glob(path):
        df = pd.read_csv(f, nrows=1)
        blub.append(df[spalte].iloc[0])

    return blub

def csvColumnToList(path,spalte):
    blub = pd.read_csv(path)
    return blub[spalte].values.tolist()

def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)

##############
# Einzelne Api-Methoden ab hier
##############

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

def SpielplanProSaison(lines, path):

    saisons = pd.read_csv(str(path) + "\Stammdaten\SaisonsProWettbewerb.csv")
    competitions = pd.read_csv(str(path) + "\Stammdaten\Wettbewerbsliste.csv")
    vorhanden = csvColumnToList(str(path) + "\Stammdaten\SaisonsProWettbewerb.csv", "id")
    bestand = bestandAusSpalte(str(path) + "\Results\*.csv", "seasonID")

    zuLaden = diff(vorhanden, bestand)

    path = path / "Results"

    # print(competitions.to_string())

    for i in zuLaden:

        print(i)

        if i == 23468:
            print("Kaputte Saison")
            continue

        baseUrl = lines[0] + "/matches-by-season/se" + str(i) + "/"
        # baseUrl = lines[0] + "/matches-by-season/se" + "23468" + "/"
        # baseUrl = lines[0] + "/matches-by-season/se" + "42529" + "/"
        wettbewerb=saisons[(saisons.id == i)]["competition_id"].iloc[0]
        saisonsName_tmp=(saisons[(saisons.id == i)]["name"].iloc[0])
        saisonsName = saisonsName_tmp.replace("\\","_").replace("/","_")
        wettbewerbname=competitions[(competitions.id == wettbewerb)]["name"].iloc[0].replace("\\","_").replace("/","_")
        landTMP=competitions[(competitions.id == wettbewerb)]["country.name"].iloc[0]
        if str(landTMP)=="nan":
            land=""
        else:
            land = str(competitions[(competitions.id == wettbewerb)]["country.name"].iloc[0]) + "_"

        file = land + wettbewerbname + "_" + saisonsName + ".csv"

        # print(file)



        response = requests.get(
            baseUrl,
            auth=HTTPBasicAuth(lines[1], lines[2])
        )
        data = response.json()

        print(response.status_code)

        # Checken ob das Dictionary leer ist
        if len(data) == 0:
            print("Saison ist leer")
            continue

        # print(type(data))
        # print(data)

        # with open("blub.pkl","wb") as f:
        #     pickle.dump(data,f)

        df = pd.json_normalize(data[0]["competition"][0]["season"][0]["round"], record_path=['match'],meta=['id', 'name', 'current_matchday', 'round_order'], meta_prefix="round.")
        print(df.iloc[0])
        df2 = ExplodeResolveListwithindf("match_result", df)

        df2["seasonID"] = i

        df2.reset_index(drop=True)

        path.mkdir(parents=True, exist_ok=True)

        # print(path)
        # print(file)

        df2.to_csv(path / file, index=False)

        
