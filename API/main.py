from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_PlayTimeGenre = pd.read_csv('funcion1.csv')
df_UserforGenre = pd.read_csv('funcion2.csv')

@app.get('/PlayTimegenre/{genre}')
async def PlayTimeGenre(genre:str):
        genre_data = df_PlayTimeGenre[df_PlayTimeGenre['tags'] == genre]
        if genre_data.empty:
            return {"error": "Género no encontrado"}
        playtime_sum = genre_data['playtime_forever_sum'].iloc[0]
        return {"genre": genre, "playtime_sum": playtime_sum}
