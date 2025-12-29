# 🎬 Movie Recommendation System

A **content-based movie recommender system** built using **TF-IDF vectorization** and **cosine similarity** to suggest movies similar to a selected title.  
The project is deployed as an interactive **Streamlit web application** and demonstrates the end-to-end workflow of an ML project — from data preprocessing to deployment.

🔗 **Live Demo:** https://<your-app-name>.streamlit.app

---

## 📌 Project Overview

This project focuses on building a **content-based recommendation engine** that works without user interaction history.  
It recommends movies by analyzing textual features such as genres, keywords, cast, director, and plot overview.

The goal of the project was to:
- Understand recommendation system fundamentals
- Apply NLP techniques to real-world data
- Build and deploy a production-ready ML application

---

## 🚀 Key Features

- Content-based filtering using textual movie metadata
- Text preprocessing with stopword removal and lemmatization (NLTK)
- TF-IDF vectorization for feature extraction
- Cosine similarity for ranking recommendations
- Movie poster integration using the TMDB API
- Deployed and hosted using Streamlit Community Cloud

---

## 🧠 Recommendation Pipeline (Technical Details)

1. **Feature Engineering**
   - Movie attributes (genres, keywords, cast, director, overview) are merged into a single text field.
2. **Text Preprocessing**
   - Lowercasing
   - Stopword removal
   - Lemmatization using NLTK
3. **Vectorization**
   - TF-IDF is applied to convert text into numerical feature vectors.
4. **Similarity Computation**
   - Cosine similarity is computed between movie vectors.
5. **Inference**
   - For a selected movie, the top-N most similar movies are returned along with posters fetched via API.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **NLP:** NLTK  
- **Web Framework:** Streamlit  
- **External API:** TMDB API  

---

## 📁 Project Structure

| 
 |--- app.py
 |--- movies.pkl
 |--- requirements.txt
 |--- .gitignore
 |___ README.md

---

## ▶️ Running the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdityaChandra06/movie-recommender-system.git
   cd movie-recommender-system
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the app**
   ```bash
   streamlit run app.py
   
   

   
