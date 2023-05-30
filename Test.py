import pandas as pd
import pickle
from pathlib import Path
import glob

path = Path(r"\\s04bi-store\PROD_BACKUP_01\11 Extraktion\Heimspiel")

# blub = []
#
# for f in glob.glob(str(path) + "\Results\*.csv"):
#     df = pd.read_csv(f,nrows=1)
#     blub.append(df["seasonID"].iloc[0])
#
# print(blub)

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

liste1 = bestandAusSpalte(str(path) + "\Results\*.csv","seasonID")
liste2 = csvColumnToList(str(path) + "\Stammdaten\SaisonsProWettbewerb.csv","id")
print(liste1)
print(liste2)
print(len(liste1))
print(len(liste2))
liste3 = diff(liste1,liste2)
print(liste3)
print(len(liste3))


# with open("blub.pkl",'rb') as f:
#     data = pickle.load(f)
#
# print(data)
#
# df = pd.json_normalize(data[0]["competition"][0]["season"][0]["round"],record_path=['match'],meta=['id','name','current_matchday','round_order'],meta_prefix="round.")
# # print(df.iloc[0])
# df2 = df.explode("match_result")
# # print(df2.iloc[1])

# print(df2.iloc[1])
# df2["match_result"]=[x["match_result"]for x in df2["match_result_tmp"]]
# df2["match_result_at"]=[x["match_result_at"]for x in df2["match_result_tmp"]]
# df2["place"]=[x["place"]for x in df2["match_result_tmp"]]
# df2["rounds"]=[x["rounds"]for x in df2["match_result_tmp"]]
# df2["team_id"]=[x["team_id"]for x in df2["match_result_tmp"]]
# df2.drop("match_result_tmp",axis=1,inplace=True)
#
# # df2["match_result"]=df2["match_result_tmp"]["match_result"]
# # df2["match_result_at"]=df2["match_result_tmp"]["match_result_at"]
# print(df2.iloc[1])

# test = pd.read_csv("Test.csv")
#
# print(test["match_result"])
# print(test.explode("match_result"))

# def superblub(spaltennamen,dataframe):
#     dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
#     map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
#     for blub in map_blub:
#         dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
#     dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
#     return dataframe
#
#
# def superblubANDexlode(spaltennamen,dataframe):
#     dataframe = dataframe.explode(spaltennamen)
#     dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
#     map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
#     for blub in map_blub:
#         dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
#     dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
#     return dataframe
#
# # df3 = superblub("match_result",df2)
#
# df3 = superblubANDexlode("competition",pd.json_normalize(data))
# print(df3.iloc[0])
#
# df4 = superblubANDexlode("match_result_at",df3)
#
# print(df4.iloc[0])

