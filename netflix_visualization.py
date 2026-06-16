import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Chart 1 - Movies vs TV Shows
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("movies_vs_tvshows.png")
plt.close()

print("Chart 1 Created")
# Chart 2 - Top 10 Countries

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("top_countries.png")
plt.close()

print("Chart 2 Created")
# Chart 3 - Top 10 Genres

top_genres = df['listed_in'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_genres.plot(kind='bar')

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.savefig("top_genres.png")
plt.close()

print("Chart 3 Created")
# Chart 4 - Ratings Distribution

top_ratings = df['rating'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_ratings.plot(kind='bar')

plt.title("Netflix Content Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("ratings_distribution.png")
plt.close()

print("Chart 4 Created")