import streamlit as st
import pandas as pd
import pickle
import joblib


# -----------------------------
# Load the saved model
# -----------------------------

@st.cache_resource
def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = joblib.load("similarity.pkl")
    return movies, similarity

movies, similarity = load_data()


# -----------------------------
# Recommendation function
# -----------------------------

def recommend(movie):

    # Find the index of the selected movie
    movie_index = movies[movies["title"] == movie].index[0]

    # Get similarity scores for that movie
    distances = similarity[movie_index]

    # Sort movies by similarity score
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    # Get movie titles
    recommendations = []

    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get 5 similar movie recommendations!")


# Movie dropdown
movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)


# Recommendation button
if st.button("Recommend Movies"):

    recommendations = recommend(movie)

    st.subheader("Recommended Movies:")

    for i, title in enumerate(recommendations, 1):
        st.write(f"**{i}. {title}**")