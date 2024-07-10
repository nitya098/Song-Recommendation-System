#Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

#Loading the dataset
print("Execuing")
df=pd.read_csv('D:/6TH SEM MINI PROJECT/DATASET/genres_v2.csv')
print(df.head(3))

# Drop rows with any NaN values
df_dropped = df.dropna()
numerical_cols=['danceability','energy','loudness','speechiness','acousticness','liveness','valence','tempo','duration_ms']

#Normalizing the numerical columns
scaler=StandardScaler()
df[numerical_cols]=scaler.fit_transform(df[numerical_cols])
print("3")

# Check for non-string values in the song name column
non_string_count = df['song_name'].apply(lambda x: isinstance(x, str)).sum()
print(f"Number of non-string values in the song name column: {len(df) - non_string_count}")

# Convert all values to strings, replacing non-string values with 'Unknown'
df['song_name'] = df['song_name'].apply(lambda x: x if isinstance(x, str) else 'Unknown')

# Ensure the column is treated as a string type
df['song_name'] = df['song_name'].astype(str)

#Function to recommend a song based on content similarity
def recommend_song(song_title,num_recommendations=25):
    if song_title not in df['song_name'].values:
        print("Song not found")
        return[]
    
    #Fetching the index of given song
    idx=df.index[df['song_name']==song_title].tolist()[0]

    #Computing the cosine similarity between selected song and all other songs
    song_features=df[numerical_cols].iloc[idx].values.reshape(1,-1)
    similarities=cosine_similarity(song_features,df[numerical_cols])

    #Get the indexes of similar songs
    similarity_scores=similarities.flatten()
    similar_indices=similarity_scores.argsort()[-num_recommendations-1:-1][::-1]

    #Get the titles of the recommended songs
    recommendations=df.iloc[similar_indices][['song_name']].to_dict(orient='records')
    list=[]
    for item in recommendations:
        song=item['song_name']
        print(song)
        if song!='Unknown':
            if song not in list:
                list.append(song)
    return list
