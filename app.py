import streamlit as st
import pickle 
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import requests


import nltk

@st.cache_resource
def download_nltk_data():
    nltk.download('wordnet')
    nltk.download('omw-1.4')

download_nltk_data()


@st.cache_resource
def build_similarity():
    tfidf = TfidfVectorizer(max_features=5000)
    vectors = tfidf.fit_transform(movies['tags'])
    return cosine_similarity(vectors)


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)
similarity = build_similarity()


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8e53e65dc2e5a308c0767b339af2385b&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if 'poster_path' not in data or data['poster_path'] is None:
            return "https://via.placeholder.com/500x750?text=No+Image"

        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    except requests.exceptions.RequestException as e:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recomemnded_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id        #fetch poster from api
        recomemnded_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recomemnded_movies,recommended_movies_posters


st.title("Movie Recommender System")

selected_movie_name=st.selectbox("Select a movie:", movies['title'].values)
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



