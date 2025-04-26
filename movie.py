from flask import Flask, render_template, request
import pandas as pd
from collections import defaultdict

# Initialize Flask app
app = Flask(__name__)

# Load movie dataset
filepath = "C:/Users/hello/Music/imdb_with_mood_mapping_final.csv"
imdb_data = pd.read_csv(filepath)

# Define mood mapping (you can fine-tune these genres for uniqueness)
mood_mapping = {
    "Happy": ["Comedy", "Feel-good", "Adventure", "Family"],
    "Sad": ["Inspirational", "Romantic", "Drama", "War"],
    "Excited": ["Thriller", "Action", "Sci-Fi", "Mystery"],
    "Angry": ["Revenge", "Crime", "Thriller"],
    "Relaxed": ["Slice-of-life", "Musical", "Fantasy", "Documentary"],
    "Bored": ["Mystery", "Horror", "Fantasy"],
    "Nostalgic": ["Western", "Classics", "History", "Biography"]
}

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    questions = [
        ("What type of activity would you prefer right now?",
         ["Relaxing", "Thrilling", "Family time", "Nostalgic reflection", "Socializing"]),
        ("What’s your ideal movie setting?",
         ["Futuristic", "Historical", "Everyday life", "Adventurous", "Romantic"]),
        ("What kind of pace do you enjoy in a movie?",
         ["Slow and emotional", "Fast-paced", "Balanced", "Suspenseful"]),
        ("How would you describe your energy level right now?",
         ["High", "Low", "Calm", "Restless"]),
        ("What’s your favorite type of ending?",
         ["Happy", "Open-ended", "Inspiring", "Dramatic", "Suspenseful Ending"]),
    ]

    mood_logic_mapping = {
        "Relaxing": "Relaxed",
        "Thrilling": "Excited",
        "Family time": "Happy",
        "Nostalgic reflection": "Nostalgic",
        "Socializing": "Happy",
        "Futuristic": "Excited",
        "Historical": "Nostalgic",
        "Everyday life": "Relaxed",
        "Adventurous": "Excited",
        "Romantic": "Sad",
        "Slow and emotional": "Sad",
        "Fast-paced": "Excited",
        "Balanced": "Happy",
        "Suspenseful": "Angry",
        "High": "Excited",
        "Low": "Sad",
        "Calm": "Relaxed",
        "Restless": "Angry",
        "Happy": "Happy",
        "Open-ended": "Nostalgic",
        "Inspiring": "Sad",
        "Dramatic": "Angry",
        "Suspenseful Ending": "Excited"
    }

    # Weighted mood scoring
    mood_scores = defaultdict(int)
    weights = [1, 1, 1, 1, 1]

    for i, (question, options) in enumerate(questions):
        user_response = request.form.get(question)
        if not user_response:
            return render_template('error.html', message=f"Missing response for: {question}")
        for mood in mood_logic_mapping.get(user_response, "").split(", "):
            mood_scores[mood] += weights[i]

    # Choose the highest scored mood
    sorted_moods = sorted(mood_scores.items(), key=lambda x: x[1], reverse=True)
    user_mood = sorted_moods[0][0]

    # Filter movies by inferred mood genres
    def filter_movies_by_mood(mood, dataset, mood_mapping):
        genres_to_include = mood_mapping.get(mood, [])
        if not genres_to_include:
            return pd.DataFrame()
        filtered = dataset[dataset['Genre'].str.contains('|'.join(genres_to_include), na=False, case=False)]
        return filtered

    filtered_movies = filter_movies_by_mood(user_mood, imdb_data, mood_mapping)

    # Randomize and limit to 10
    if not filtered_movies.empty:
        sample = filtered_movies.sample(n=10) if len(filtered_movies) >= 10 else filtered_movies
        movies_html = sample[['Series_Title', 'Released_Year', 'IMDB_Rating', 'Poster_Link']].to_dict(orient='records')
        return render_template('recommend.html', mood=user_mood, movies=movies_html)
    else:
        return render_template('recommend.html', mood=user_mood, movies="No recommendations found.")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
