import sys
import json
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from surprise import Reader, Dataset, SVD

# Load the User-Movie-Rating Dataset
def load_ratings_data(ratings_filepath, movies_filepath):
    # Load ratings data
    ratings_df = pd.read_csv(ratings_filepath)

    # Load movie data
    movies_df = pd.read_csv(movies_filepath)

    # Merge datasets to associate movie titles with ratings
    merged_df = pd.merge(ratings_df, movies_df, left_on='Movie ID', right_on='id', how='left')

    return merged_df

# Preprocess the Data
def preprocess_data(merged_df):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(merged_df[['User ID', 'Movie ID', 'Rating']], reader)
    return data

# Recommend Movies
# Recommend Movies
# Recommend Movies
import json

# Helper function to parse genres
def parse_genres(genres_str):
    try:
        genres_list = json.loads(genres_str.replace("'", "\""))
        return [genre['name'] for genre in genres_list]
    except json.JSONDecodeError:
        return []

# Recommend Movies
def recommend_movies(model, user_id, merged_df, num_recommendations=5):
    # Get a list of all movie IDs
    movie_ids = merged_df['Movie ID'].unique()

    # Get a list of movie IDs that the user has already rated
    rated_movies = merged_df[merged_df['User ID'] == user_id]['Movie ID'].unique()

    # Predict ratings for all movies that the user hasn't rated yet
    predictions = [model.predict(user_id, movie_id) for movie_id in movie_ids if movie_id not in rated_movies]

    # Sort the predictions in descending order of the predicted rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top N predictions
    top_predictions = predictions[:num_recommendations]

    # Fetch movie titles and genres for the top predictions
    recommendations = []
    for pred in top_predictions:
        movie_info = merged_df[merged_df['Movie ID'] == pred.iid].iloc[0]
        genres_str = movie_info['genres']
        genres = parse_genres(genres_str)
        title = movie_info['title']
        recommendations.append(f"[{', '.join(genres)}] - {title}")

    return recommendations

class MovieRecommenderGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Load and preprocess the dataset
        self.merged_data = load_ratings_data("ratings.csv", "movie_data.csv")
        self.data = preprocess_data(self.merged_data)
        self.model = SVD()
        self.model.fit(self.data.build_full_trainset())

        # GUI layout and elements
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # User ID Input
        self.userIdInput = QLineEdit(self)
        self.userIdInput.setPlaceholderText("Enter User ID")
        layout.addWidget(self.userIdInput)

        # Get Recommendations Button
        self.btn = QPushButton('Get Recommendations', self)
        self.btn.clicked.connect(self.on_click)
        layout.addWidget(self.btn)

        # Recommendations Display Area
        self.recommendationsDisplay = QTextEdit(self)
        self.recommendationsDisplay.setReadOnly(True)
        layout.addWidget(self.recommendationsDisplay)

        self.setLayout(layout)
        self.setWindowTitle('Movie Recommender')

    def on_click(self):
        user_id = self.userIdInput.text()
        try:
            user_id = int(user_id)
            recommendations = recommend_movies(self.model, user_id, self.merged_data)
            self.recommendationsDisplay.setText("Recommended movies:\n" + "\n".join(recommendations))
        except ValueError:
            self.recommendationsDisplay.setText("Please enter a valid user ID.")

def main():
    app = QApplication(sys.argv)
    ex = MovieRecommenderGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()