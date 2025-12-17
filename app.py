import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- DATA LOAD + CLEAN ----------------
df = pd.read_csv('cleaned_data.csv')

# Numeric conversions
df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'], errors='coerce')
df['numVotes'] = pd.to_numeric(df['numVotes'], errors='coerce')

# Basic drops
df = df.dropna(subset=['bechdel_rating', 'imdbAverageRating', 'year'])
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Separate copy for scatter
df_scatter = df.dropna(
    subset=['numVotes', 'imdbAverageRating', 'runtimeMinutes', 'bechdel_rating']
)

# ---------------- LAYOUT + SIDEBAR FILTERS ----------------
st.title("Bechdel Test Dashboard")
st.caption(
    "Data source: Kaggle - IMDb + Bechdel ratings. "
    "Use the sidebar to filter by year and primary genre."
)

st.sidebar.header("Filters")

min_year = int(df['year'].min())
max_year = int(df['year'].max())

year_range = st.sidebar.slider(
    "Year range",
    min_year, max_year,
    (1980, 2020)
)

genres = sorted(df['genre1'].dropna().unique())
selected_genre = st.sidebar.selectbox("Primary genre", ["All"] + list(genres))

# Apply filters
filtered = df[
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

if selected_genre != "All":
    filtered = filtered[filtered['genre1'] == selected_genre]

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total movies", len(df))
with col2:
    st.metric("Filtered movies", len(filtered))
with col3:
    st.metric(
        "Avg IMDb rating (filtered)",
        round(filtered['imdbAverageRating'].mean(), 2)
    )

# ---------------- CHARTS ----------------
st.subheader("Bechdel rating counts (filtered)")
st.bar_chart(filtered['bechdel_rating'].value_counts())

st.subheader("IMDb rating by Bechdel score")
fig_box = px.box(
    filtered,
    x="bechdel_rating",
    y="imdbAverageRating",
    labels={
        "bechdel_rating": "Bechdel score (0–3)",
        "imdbAverageRating": "IMDb rating"
    },
    title="Do movies that pass the Bechdel test have higher IMDb ratings?"
)
st.plotly_chart(fig_box, width="stretch")

st.subheader("Votes vs rating (colored by Bechdel score)")

scatter_data = df_scatter[
    (df_scatter['year'] >= year_range[0]) &
    (df_scatter['year'] <= year_range[1])
]

fig_scatter = px.scatter(
    scatter_data,
    x="numVotes",
    y="imdbAverageRating",
    color="bechdel_rating",
    size="runtimeMinutes",
    size_max=40,
    labels={"numVotes": "Number of votes"},
    title="Popularity, rating, and Bechdel score"
)

# ... boxplot, scatter code mudinja piragu ...

st.markdown("### Quick insights")

pass_rate = (filtered['bechdel_rating'] == 3).mean() * 100
avg_rating_pass = filtered.loc[
    filtered['bechdel_rating'] == 3, 'imdbAverageRating'
].mean()
avg_rating_fail = filtered.loc[
    filtered['bechdel_rating'] == 0, 'imdbAverageRating'
].mean()

st.write(f"• Bechdel score 3 (full pass) share in current filter: {pass_rate:.1f}%.")
st.write(f"• Avg IMDb rating (pass=3): {avg_rating_pass:.2f}")
st.write(f"• Avg IMDb rating (fail=0): {avg_rating_fail:.2f}")

st.plotly_chart(fig_scatter, width="stretch")

# ---------------- TABLE + DOWNLOAD ----------------
st.subheader("Filtered data preview")
st.dataframe(filtered.head(20))

csv = filtered.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="bechdel_filtered.csv",
    mime="text/csv",
)
