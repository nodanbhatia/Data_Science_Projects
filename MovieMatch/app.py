# import libraries

import streamlit as st
import pickle 
import pandas as pd




# function for getting the recommended movies 

def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
       recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))




# FRONTEND OF STREAMLIT DAHBOARD

st.set_page_config(
    page_title="MovieMatch | Movie Recommendation System",
    layout="wide",
)

st.title(" MovieMatch")
st.write("Find movies similar to the one you love using content-based recommendations.")
st.caption("Built with movie genres, keywords, overview, cast, director, CountVectorizer, and cosine similarity.")





# DEVELOP SIDEBAR

st.sidebar.header(" Catalog Insights")
st.sidebar.metric("Total Movies Loaded", len(movies))

if 'genre' in movies.columns:
    all_genres = set([g for genres in movies['genre'].dropna() for g in (genres if isinstance(genres, list) else str(genres).split(','))])
    selected_genre = st.sidebar.selectbox("Filter Explorer by Genre", ["All"] + sorted(list(all_genres)))
else:
    selected_genre = "All"

st.sidebar.divider()
st.sidebar.info("**Tip:** Select a movie from the main tab to generate top similarity recommendations.")





# DASHBORAD ALL TABS

tab_rec, tab_explore, tab_analytics = st.tabs([" Movie Recommender", " Browse Catalog", "Dataset Analytics"])

with tab_rec:
    selected_movie_name=st.selectbox(
        "Select Movie For Recommendation",
        movies['title'].values
    )

    if st.button('Recommend'):
        recommendations=recommend(selected_movie_name)
        st.subheader(f"Top 5 Recommendations for '{selected_movie_name}':")
        cols = st.columns(5)
        for idx, rec in enumerate(recommendations):
            with cols[idx]:
                st.info(f"**{idx + 1}.** {rec}")



# FOR EXPLORE TAB 

with tab_explore:
    st.subheader(" Explore Movie Database")
    
    search_query = st.text_input("Search movie by title:", "")
    
    filtered_df = movies.copy()
    if search_query:
        filtered_df = filtered_df[filtered_df['title'].str.contains(search_query, case=False, na=False)]
        
    st.dataframe(filtered_df, use_container_width=True, height=400)



# FOR ANALYSTICS TAB

with tab_analytics:
    st.subheader(" Dataset Overview & Statistics")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(movies))
    col2.metric("Unique Titles", movies['title'].nunique())
    col3.metric("Similarity Matrix Shape", f"{similarity.shape[0]} x {similarity.shape[1]}")
    
    st.markdown("### Random Spotlight")
    if st.button(" Pick a Random Movie"):
        random_movie = movies.sample(1).iloc[0]
        st.success(f"**Title:** {random_movie['title']}")
        if 'overview' in random_movie:
            st.write(f"**Overview:** {random_movie['overview']}")




# END AND CAPTION IN SIDEBAR 

st.sidebar.divider()
st.sidebar.caption("MovieMatch • Streamlit + Pandas + Scikit-learn")