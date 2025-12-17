# Bechdel_test_dashboard
Streamlit dashboard for Bechdel Test analysis using IMDb + Kaggle data
# Bechdel Test Movie Dashboard

Interactive data science project that analyzes how movies perform on the Bechdel Test and how it relates to IMDb ratings. [web:4][web:19]

## Project overview
This dashboard explores a Kaggle dataset of 9,000+ movies with IMDb information and Bechdel Test scores.  
Users can filter by release year and genre to study how representation of women in films changes over time. [web:15][web:155]

## Data source
- **Dataset**: 9000+ Movies: IMDb and Bechdel  
- **Link**: https://www.kaggle.com/datasets/nliabzd/movies-imdb-and-bechdel-information [web:15]  
- Key columns used: `year`, `genre1–3`, `bechdelRating`, `imdbAverageRating`, `numVotes`, `runtimeMinutes`. [web:15]

## Features
- Sidebar filters for:
  - Year range (e.g., 1980–2020)
  - Primary genre (Action, Drama, Comedy, etc.)
- Bechdel rating distribution (0–3) for filtered movies
- Boxplot of IMDb rating vs. Bechdel score
- Scatter plot of votes vs. IMDb rating, colored by Bechdel score
- Quick insights (pass rate and rating differences)
- Download filtered data as CSV from the app

## Tech stack
- Python
- Streamlit for the interactive dashboard UI
- pandas for data cleaning and manipulation
- Plotly Express for visualizations
- kagglehub for downloading the dataset programmatically [web:57][web:162]

## How to run locally
git clone <this-repo-url>
cd bechdel_test_dashboard # or your repo name
python -m venv venv
.\venv\Scripts\Activate.ps1 # on Windows
pip install -r requirements.txt
streamlit run app.py


## Bechdel Test (brief)
The Bechdel Test checks if a movie includes at least two named women who talk to each other about something other than a man. [web:4]
