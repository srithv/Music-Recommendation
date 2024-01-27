"""
# Initial imports
"""

import pandas as pd
from google.colab import output



"""# Pre-requisites

"""

data= pd.read_csv("https://raw.githubusercontent.com/srithv/Music-Recommendation/main/data/data.csv")
df= pd.DataFrame(data)
now_playing_values={"acousticness":0.0,"danceability":0.0,"energy":0.0,"liveness":0.0,"speechiness":0.0}

"""# Function for weight calculation

"""

def weight_calc(i ,now):
            temp_weight=0.0
            if abs(i-now)==0:
                pass
            elif abs(i-now)<=0.1 and abs(i-now)!=0 :
                temp_weight+=1.0
            elif abs(i-now)<=0.2 and abs(i-now)<0.1:
                temp_weight+=0.5
            elif abs(i-now)<=0.3 and abs(i-now)<0.2:
                temp_weight-=0.5
            else:
                temp_weight-=1
            return(temp_weight)

"""# Program start

"""

weight_calc(0.977,0.93)

"""# Main Program"""

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Music Recommendation using Content based filtering ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print("press 1 to like the song and 0 for skiping it\n")
playlist=df.query("year > 2000").sample(n=150,replace=True)
#playlist=df.query().sample(n=10,replace=True)
# playlist=df
playlist=playlist.reset_index(drop=True)


playlist["weight"].values[:] = 0.0
now_playing=playlist.sample()
i=0
while (True):
    # output.clear()
    print("\n\nnow playing : {0} ({2}) by {1} \n".format(now_playing["name"].values[0],now_playing["artists"].values[0],now_playing["year"].values[0]))
    #print(now_playing["weight"].values[0])
    t=int(input("\nenter your selection\t"))
    if t==1:
        now_playing_values["acousticness"]=now_playing["acousticness"].values[0]
        now_playing_values["danceability"]=now_playing["danceability"].values[0]
        now_playing_values["energy"]=now_playing["energy"].values[0]
        now_playing_values["liveness"]=now_playing["liveness"].values[0]
        now_playing_values["speechiness"]=now_playing["speechiness"].values[0]

        for index , row in playlist.iterrows():
            # print(index,row.values[:])
            temp_weight=0.0
            temp_weight+= weight_calc(row["acousticness"],now_playing_values["acousticness"])
            temp_weight+= weight_calc(row["danceability"],now_playing_values["danceability"])
            temp_weight+= weight_calc(row["energy"],now_playing_values["energy"])
            temp_weight+= weight_calc(row["liveness"],now_playing_values["liveness"])
            temp_weight+= weight_calc(row["speechiness"],now_playing_values["speechiness"])
            # print(temp_weight)
            playlist["weight"].values[index]=temp_weight


        playlist=playlist.sort_values(by="weight",ascending=False)
        # playlist=playlist.query("weight > 0")
        # playlist=playlist.reset_index(drop=True)

        now_playing=playlist.head(1)


    elif t==0:
        i+=1
        now_playing=playlist.iloc[[i]]
    else:
      break
