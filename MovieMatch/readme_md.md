# 🍿 MovieMatch | Content-Based Movie Recommendation System

**MovieMatch** is an interactive, full-fledged Streamlit web dashboard that delivers personalized movie recommendations using Content-Based Filtering. By analyzing metadata—including genres, plot overviews, key tags, directors, and top cast members—MovieMatch computes similarity scores via CountVectorizer and Cosine Similarity to find the perfect movie match.

---

## ✨ Features

- **🍿 Smart Recommendation Engine:** Select any movie from the dataset to receive top 5 recommendations generated via cosine similarity.
- **🎨 Modern Dark Dashboard Theme:** Includes a sleek dark-mode UI with custom CSS, neon pink/purple accents, and interactive outlined buttons with gradient hover effects.
- **🔍 Interactive Catalog Explorer:** Browse through the entire movie dataset with live title search and responsive table views.
- **📈 Dataset Analytics & Insights:** View high-level catalog metrics, vocabulary shapes, unique records, and leverage a "Random Spotlight" feature to discover hidden gems.
- **🖼️ TMDB Poster Integration (Optional):** Fetches high-resolution posters on-the-fly using the TMDB API.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.8+
- **Frontend / Web Framework:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
- **Machine Learning & NLP:** [scikit-learn](https://scikit-learn.org/) (`CountVectorizer`, `cosine_similarity`)
- **Serialization:** `pickle`

---

## 📂 Project Structure

```text
├── app.py              # Main Streamlit application file
├── movies_dict.pkl     # Preprocessed movie metadata dictionary
├── similarity.pkl     # Precalculated cosine similarity matrix
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
```

---

## ⚡ Quick Start & Local Setup

### 1. Prerequisites
Ensure you have Python installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/MovieMatch.git
cd MovieMatch
```

### 3. Install Dependencies
Create a virtual environment (optional but recommended) and install required libraries:
```bash
# Optional: Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required packages
pip install streamlit pandas requests
```

### 4. Add Data Files
Ensure you have generated and placed the following required pickle files in the project root folder:
- `movies_dict.pkl`
- `similarity.pkl`

### 5. Run the Application
Launch the Streamlit dashboard:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to explore MovieMatch!

---

## 🤖 How the Recommendation Model Works

1. **Feature Extraction:** Key tags, genres, director names, main actors, and plot summaries are combined into a unified text string per movie.
2. **Text Vectorization:** `CountVectorizer` converts the combined text strings into numeric feature vectors while filtering out common English stop words.
3. **Similarity Score Calculation:** `cosine_similarity` calculates the angle/similarity between every movie vector pair, forming a matrix stored in `similarity.pkl`.
4. **Ranking:** When a movie is selected, the application queries the similarity matrix, sorts candidate scores in descending order, and fetches the top 5 nearest neighbors.

---

## 🤝 Contributing

Contributions are always welcome! Feel free to open an issue or submit a pull request for new features, bug fixes, or UI enhancements.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).