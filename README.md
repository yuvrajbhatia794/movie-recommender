# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Python, Pandas, Scikit-learn, and Streamlit**.

The system recommends movies based on the similarity between their genres, keywords, overview, cast, and crew.

## 🚀 Live Demo

[Click here to try the Movie Recommendation System](https://movie-recommender-sample.streamlit.app/)

## 📌 Features

- Select a movie from the available movie database
- Get the top 5 movies similar to the selected movie
- Uses content-based filtering
- Uses text feature extraction and cosine similarity
- Interactive web interface built with Streamlit

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and preprocessing
- **Scikit-learn** – CountVectorizer and cosine similarity
- **Streamlit** – Web application and deployment
- **Pickle** – Model/data serialization

## 🧠 How It Works

The recommendation system follows these steps:

1. Movie information such as **genres, keywords, overview, cast, and crew** is combined into a single `tags` feature.
2. The text data is converted into numerical vectors using **CountVectorizer**.
3. **Cosine similarity** is calculated between movies.
4. When a user selects a movie, the system finds movies with the highest similarity scores.
5. The top 5 most similar movies are displayed as recommendations.

### Recommendation Flow

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Combine Movie Features
      ↓
Create "Tags"
      ↓
CountVectorizer
      ↓
Feature Vectors
      ↓
Cosine Similarity
      ↓
Top 5 Similar Movies
