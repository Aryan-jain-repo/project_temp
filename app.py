import pickle
import streamlit as st
import requests
from test import play_trailer

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🤖",
    layout = "centered"
)


def fetch_poster(movie_id):
    
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def details(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    data_details = {"date":data["release_date"],"revenue":data["revenue"],"runtime":data["runtime"]}
    return data_details

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    movie_details = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        movie_details.append(details(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters,movie_details

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,movie_details= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        movie_data = movie_details[0]
        st.write(f"Release date :{movie_data['date']}")
        st.write(f"Revenue :{movie_data['revenue']}")
        st.write(f"Run time :{movie_data['runtime']}")
    
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        movie_data = movie_details[1]
        st.write(f"Release date :{movie_data['date']}")
        st.write(f"Revenue :{movie_data['revenue']}")
        st.write(f"Run time :{movie_data['runtime']}")

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        movie_data = movie_details[2]
        st.write(f"Release date :{movie_data['date']}")
        st.write(f"Revenue :{movie_data['revenue']}")
        st.write(f"Run time :{movie_data['runtime']}")

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        movie_data = movie_details[3]
        st.write(f"Release date :{movie_data['date']}")
        st.write(f"Revenue :{movie_data['revenue']}")
        st.write(f"Run time :{movie_data['runtime']}")

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        movie_data = movie_details[4]
        st.write(f"Release date :{movie_data['date']}")
        st.write(f"Revenue :{movie_data['revenue']}")
        st.write(f"Run time :{movie_data['runtime']}")
            

    
movie_name = st.text_input('Enter the name of the movie:')
if st.button('Play Trailer'):
    play_trailer(movie_name)
    




