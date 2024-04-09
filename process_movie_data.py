import json
import pandas as pd

def de_jsonify(json_string, field_string):
    l = json.loads(json_string)
    return ','.join([d[field_string] for d in l])

def extract_director(json_string, field_string, director_string):
    l = json.loads(json_string)
    for d in l:
        if d[director_string] == 'Director':
            return d[field_string]

    return None


df = pd.read_csv('data/full/movies/tmdb_5000_movies.csv')

df['keywords'] = df.apply(lambda row: de_jsonify(row['keywords'],"name"), axis=1)
df['genres'] = df.apply(lambda row: de_jsonify(row['genres'],"name"), axis=1)
df['production_companies'] = df.apply(lambda row: de_jsonify(row['production_companies'],"name"), axis=1)
df['production_countries'] = df.apply(lambda row: de_jsonify(row['production_countries'],"name"), axis=1)
df['spoken_languages'] = df.apply(lambda row: de_jsonify(row['spoken_languages'],"name"), axis=1)

df.to_csv('data/full/movies/tmdb_5000_movies_modified.csv',index=False)


df = pd.read_csv('data/full/movies/tmdb_5000_credits.csv')

df['actors'] = df.apply(lambda row: de_jsonify(row['cast'],"name"), axis=1)
df['director'] = df.apply(lambda row: extract_director(row['crew'],"name", "job"), axis=1)

df.to_csv('data/full/movies/tmdb_5000_credits_modified.csv',index=False)