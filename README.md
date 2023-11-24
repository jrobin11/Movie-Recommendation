
# Movie Recommendation Engine

## Overview
The Movie Recommendation Engine is a collaborative filtering-based system designed to provide personalized movie suggestions. Utilizing the MovieLens dataset, this engine analyzes user preferences to recommend movies.

## Setup Instructions

### Ensure Python is Installed
First, make sure Python is installed on your system. You can download and install Python from [python.org](https://www.python.org/).

### Cloning the Repository
To set up this project on your local machine, you need to clone the repository. Use the following command in your terminal:

```
git clone git@github.com:jrobin11/MovieRecommendation.git
```

### Creating a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment for your project. This keeps your project dependencies separate from your global Python installation. Here's how you can do it:
- Open your terminal or command prompt.
- Navigate to your project directory:
  ```
  cd path/to/your/project
  ```
- Create a virtual environment named `venv` (or any name you prefer):
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows:
    ```
    .\venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```
    source venv/bin/activate
    ```

### Installing Dependencies
With your virtual environment activated, install the required packages using pip and the `requirements.txt` file:
```
pip install -r requirements.txt
```

### Running the Application
Navigate to the directory where you cloned the repository and run the main Python script:
```
python main.py
```

## Requirements
- Python 3.x
- pandas
- PyQt5
- scikit-surprise

## Data Mining Techniques Used
- Collaborative Filtering
  * The Movie Recommendation Engine employs Collaborative Filtering, a popular and effective method in recommendation systems. This approach is based on the idea that users who agreed in the past will agree in the future about certain preferences.

- Singular Value Decomposition (SVD):
  * Functionality: SVD is a matrix factorization technique used to predict unknown preferences in a user-item association matrix. In the context of our engine, it decomposes the matrix of user ratings for various movies into several matrices representing latent factors. These factors could represent underlying variables that affect user preferences, such as movie genres, themes, or general appeal.
  * Prediction of User Preferences: The SVD algorithm predicts how a user would rate a movie they haven't seen based on the ratings of similar users. It calculates a set of scores for each user and each item in these latent factor spaces and predicts a rating by combining these scores. This helps in recommending movies that a user is likely to enjoy, based on their previous ratings and the ratings of others with similar tastes.

- Code Functionality and File Integration:
  * movie_data.csv: This file contains detailed information about each movie, such as titles and genres. It's crucial for providing context to the movie IDs used in the ratings data.
  * ratings.csv: The main dataset for the engine, containing user ratings for different movies. It includes user IDs, movie IDs, and the ratings provided by users.
  * ratingTest.py: This could be a script for testing the rating predictions of the engine, ensuring that the model is providing accurate recommendations.

- Workflow:
  * Loading Data: The load_ratings_data function reads data from ratings.csv and movie_data.csv, merging them to form a comprehensive dataset that associates movie titles and genres with user ratings.
  * Preprocessing: The preprocess_data function then prepares this data for analysis. It structures the data in a format that the SVD algorithm can work with, essentially shaping it into a user-item rating matrix.
  * Model Training: The SVD model is trained on this prepared dataset, learning to associate users with their rating patterns and latent preferences.
  * Making Recommendations: The recommend_movies function uses the trained model to predict ratings for movies that a user hasn't rated yet. It then recommends the top movies with the highest predicted ratings.
  * GUI Interaction: The MovieRecommenderGUI class creates a user interface where users can input their IDs, and the system fetches and displays personalized movie recommendations.

- Featurability of the System
  * Personalization: The system provides personalized recommendations based on individual user preferences.
  * Scalability: It can handle large datasets efficiently due to the use of matrix factorization, making it scalable for extensive user bases.
  * Adaptability: The system can adapt to new ratings, continuously refining its recommendations as it receives more data.
