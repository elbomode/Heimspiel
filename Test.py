import pandas as pd
import pickle

with open("blub.pkl",'rb') as f:
    data = pickle.load(f)

print(data)

df = pd.json_normalize(data[0]["competition"][0]["season"][0]["round"],record_path=['match'], meta=['id','name','current_matchday','round_order'],meta_prefix="round.")
# print(df.iloc[0])
df2 = df.explode("match_result")
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

def superblub(spaltennamen,dataframe):
    dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
    map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
    for blub in map_blub:
        dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
    dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
    return dataframe


def superblubANDexlode(spaltennamen,dataframe):
    dataframe = dataframe.explode(spaltennamen)
    dataframe[spaltennamen+"tmp"] = dataframe[spaltennamen].copy()
    map_blub = dataframe.iloc[0][spaltennamen+"tmp"].keys()
    for blub in map_blub:
        dataframe[blub] = [x[blub] for x in dataframe[spaltennamen+"tmp"]]
    dataframe.drop(spaltennamen+"tmp", axis=1, inplace=True)
    return dataframe

# df3 = superblub("match_result",df2)

df3 = superblubANDexlode("competition",pd.json_normalize(data))
print(df3.iloc[0])

df4 = superblubANDexlode("match_result_at",df3)

print(df4.iloc[0])