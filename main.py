import sys
import pandas as pd
import json
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, \
    QMessageBox, QGridLayout
from PyQt5.QtCore import Qt

# Load and preprocess the data
def load_data(filepath):
    column_names = ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview',
                    'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime',
                    'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']
    df = pd.read_csv(filepath, names=column_names)

    def parse_json(json_string):
        try:
            return json.loads(json_string.replace("'", "\""))
        except json.JSONDecodeError:
            return []

    df['genres'] = df['genres'].apply(parse_json)
    df['genre_names'] = df['genres'].apply(lambda items: [item['name'].lower() for item in items])

    return df[['id', 'original_title', 'genre_names', 'vote_average', 'vote_count']]


# Function to get movie recommendations based on genre
def get_recommendations_by_genre(genre_preference, data, top_n=5):
    filtered_movies = data[data['genre_names'].apply(lambda genres: genre_preference.lower() in genres)]
    if len(filtered_movies) > top_n:
        recommended_movies = filtered_movies.sample(n=top_n)
    else:
        recommended_movies = filtered_movies
    return recommended_movies

# Function to get a list of unique genres
def get_unique_genres(data):
    return sorted(set([genre for sublist in data['genre_names'] for genre in sublist]))

class MovieRecommenderGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.data = load_data("movie_data.csv")
        self.unique_genres = get_unique_genres(self.data)

        # GUI layout and elements
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget { font-size: 14px; }")

        mainLayout = QVBoxLayout()

        # Genre Grid
        self.genreGrid = QGridLayout()
        self.genreGrid.setSpacing(10)
        mainLayout.addLayout(self.genreGrid)

        # Populate the grid with genre labels
        self.populate_genre_grid()

        # Genre Input
        inputLayout = QHBoxLayout()
        self.genreInput = QLineEdit(self)
        self.genreInput.setPlaceholderText("Enter a movie genre")
        self.genreInput.setStyleSheet("padding: 5px;")
        inputLayout.addWidget(self.genreInput)

        # Get Recommendations Button
        self.btn = QPushButton('Get Recommendations', self)
        self.btn.clicked.connect(self.on_click)
        self.btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 10px; border: none; } QPushButton:hover { background-color: #45a049; }")
        inputLayout.addWidget(self.btn)

        mainLayout.addLayout(inputLayout)

        # Result Area
        self.resultArea = QTextEdit(self)
        self.resultArea.setReadOnly(True)
        self.resultArea.setStyleSheet("padding: 5px; border: 1px solid #ccc;")
        mainLayout.addWidget(self.resultArea)

        self.setLayout(mainLayout)
        self.setWindowTitle('Movie Recommender')
        self.setGeometry(300, 300, 600, 400)

    def populate_genre_grid(self):
        row = 0
        col = 0
        for genre in self.unique_genres:
            label = QLabel(genre.title())
            label.setStyleSheet("margin: 5px; padding: 2px;")
            self.genreGrid.addWidget(label, row, col)
            col += 1
            if col > 1:  # Adjust this value to change the number of columns
                row += 1
                col = 0

    def on_click(self):
        genre = self.genreInput.text().lower()
        if not genre:
            QMessageBox.warning(self, 'Input Error', 'Please enter a genre.', QMessageBox.Ok)
            return

        if genre not in self.unique_genres:
            QMessageBox.warning(self, 'Genre Not Found', f'No movies found for the genre "{genre.title()}". Please try a different genre.', QMessageBox.Ok)
            return

        recommendations = get_recommendations_by_genre(genre, self.data)
        self.display_recommendations(recommendations)

    def display_recommendations(self, recommendations):
        self.resultArea.clear()
        if recommendations.empty:
            self.resultArea.setText("No movies found for this genre.")
            return

        result_text = "🎬 Recommended Movies:\n\n"
        for _, movie in recommendations.iterrows():
            result_text += f"🌟 {movie['original_title']} (Genre: {', '.join(movie['genre_names']).title()}, Rating: {movie['vote_average']} / 10)\n"
        self.resultArea.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MovieRecommenderGUI()
    ex.show()
    sys.exit(app.exec_())
