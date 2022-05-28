import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import json
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
# from surprise import Reader, Dataset
# from surprise.prediction_algorithms.matrix_factorization import SVD
# from surprise.model_selection import cross_validate
import urllib.request
import pickle
import requests


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
# cosine_sim = pickle.load(open('similarity.pkl','rb'))
indices = pickle.load(open('indices.pkl','rb'))
id_map = pickle.load(open('id_map.pkl','rb'))
svd = pickle.load(open('svd.pkl','rb'))
indices_map = id_map.set_index('id')
smd = pd.DataFrame(movie_dict)

# reader = Reader()
# ratings = pd.read_csv('ratings_small.csv')
# data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
# svd = SVD()
# cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5)
# trainset = data.build_full_trainset()
# svd.fit(trainset)



def hybrid(userId, title):
     if title not in list(smd.loc[:,'title']):
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
     idx = indices[title]
     tmdbId = id_map.loc[title]['id']
     movie_id = id_map.loc[title]['movieId']
     count = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
     count_matrix = count.fit_transform(smd['soup'])
     cosine_sim = cosine_similarity(count_matrix, count_matrix)
     sim_scores = list(enumerate(cosine_sim[int(idx)]))
     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
     sim_scores = sim_scores[1:26]
     movie_indices = [i[0] for i in sim_scores]

     movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'id']]
     movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, indices_map.loc[x]['movieId']).est)
     movies = movies.sort_values('est', ascending=False)
     recommended_movies =[]
     for i in range(10):
          recommended_movies.append(movies.iloc[i].title)
     return recommended_movies
    
# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list

def get_suggestions():
    return list(smd.loc[:,'title'])

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    # print(suggestions)
    return render_template('home.html',suggestions=suggestions)

@app.route("/similarity",methods=["POST"])
def similarity():
    # print(request.form)
    movie = request.form['name']
    userId = int(request.form['user_id'])
    rc = hybrid(userId , movie)
    # print(userId)
    # print(rc)
    if type(rc)==type('string'):
        return rc
    else:
        m_str="---".join(rc)
        return m_str

@app.route("/recommend",methods=["POST"])
def recommend():
    # getting data from AJAX request
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    # get movie suggestions for auto complete
    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)
    
    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")
    
    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
    
    # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    
    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

    cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_cards,casts=casts,cast_details=cast_details)

if __name__ == '__main__':
    app.run(debug=True)
