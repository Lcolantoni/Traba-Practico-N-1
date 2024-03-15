from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_PlayTimeGenre = pd.read_csv('PlayTimeGenre.csv')
df_UsersForGenre = pd.read_csv('UserForGenre.csv')
df_UsersRecommendd = pd.read_csv('Usersrecommend.csv')
df_UsersWorstDeveloper = pd.read_csv('UsersWorstDeveloper.csv')
df_sentiment_analysis = pd.read_csv('sentiment_analysis.csv')
@app.get('/PlayTimeGenre/{genre}')
async def PlayTimegenre(genre: str):
    
    '''debe devolver el año con mas horas jugadas para el genero solicitado'''
    
    filtered_df = df_PlayTimeGenre[df_PlayTimeGenre['genres'].str.contains(genre)]
    if filtered_df.empty:
        return {"error": "No se encontraron datos para el género proporcionado."}
    
    max_hours_row = filtered_df.loc[filtered_df['playtime_forever_sum'].idxmax()]
    
    year_with_max_hours = int(max_hours_row['year'])
    
    return {"Año de lanzamiento con más horas jugadas para " + genre: year_with_max_hours}


@app.get('/UserForGenre/{genre}')
async def UserForGenre(genre: str):
    '''Debe devolver el usuario que acumula más horas jugadas para el género dado
      y una lista de la acumulación de horas jugadas por año.'''
    user_with_most_playtime = df_UsersForGenre.loc[0, 'user_id']
    
    playtime_by_year = df_UsersForGenre.groupby(pd.Grouper(key='posted', freq='YE'))['playtime_forever'].sum().reset_index()
    playtime_by_year['posted'] = playtime_by_year['posted'].dt.year
    playtime_by_year = playtime_by_year.rename(columns={'posted': 'year', 'playtime_forever': 'total_playtime'})
    playtime_by_year = playtime_by_year.astype(int)
    playtime_by_year = playtime_by_year.to_dict(orient='records')
    
    return {
        "usuario_con_mas_horas_jugadas": user_with_most_playtime,
        "acumulacion_horas_jugadas_por_año": playtime_by_year
    }

@app.get('/UsersRecommend/{year}')
async def UsersRecommend(year: int):
    return "UsersRecommend"

@app.get('/UsersWorstDeveloper/{year}')
async def UsersWorstDeveloper(year: int):
    '''Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado'''
    filtered_df = df_UsersWorstDeveloper[df_UsersWorstDeveloper['year'] == year]
    
    if filtered_df.empty:
        return {"error": "No se encontraron datos para el año proporcionado."}
    
    sorted_df = filtered_df.sort_values(by=['score1', 'score2', 'score3'])
    
    top_3_developers = sorted_df[['worst1', 'worst2', 'worst3']].iloc[:3].values.flatten().tolist()
    
    return {"top 3 worst developers": top_3_developers}


@app.get('/Sentiment_analysis/{developer}')
async def sentiment_analysis(developer: str):
    '''devuelve un diccionario con el nombre de la desarrolladora como llave y
      una lista con la cantidad total de registros de reseñas de usuarios 
    que se encuentren categorizados con un análisis de sentimiento como valor.'''
    df_filtrado = df_sentiment_analysis[df_sentiment_analysis['developer'] == developer]
    if df_filtrado.empty:
        return {'error': f'El desarrollador {developer} no fue encontrado.'}
    valores = df_filtrado.iloc[0, 1:].tolist()
    valores = [int(val) for val in valores]

    resultado = {
        developer: {
            'Negative': valores[0],
            'Neutral': valores[1],
            'Positive': valores[2]
        }
    }
    return resultado