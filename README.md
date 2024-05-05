
# Movie Recommendation System

This project, developed for the Data Mining class, implements a Collaborative Filtering Recommender System using Python and several machine learning libraries. The system is designed to predict user preferences for movies based on ratings provided by many users, harnessing the power of collective user behavior to make accurate recommendations.

## Project Overview

The Jupyter Notebook included in this repository encapsulates the entire workflow of the recommendation system, from initial data ingestion and preprocessing to model training and generating predictions. The system utilizes collaborative filtering techniques, particularly focusing on the Nearest Neighbors algorithm, to identify patterns in movie ratings and suggest movies that share similar user rating profiles.

### Key Components

- **Data Loading**: Movie and rating data are dynamically loaded from external URLs, ensuring the system uses the most up-to-date information.
- **Data Preprocessing**: Includes handling duplicates, managing missing values, and merging datasets to create a comprehensive view of user ratings and movie metadata.
- **Model Building**: Employs the Nearest Neighbors algorithm from scikit-learn, configured to measure cosine similarity among user rating vectors, to find movies similar to a user's historical preferences.
- **Recommendation Generation**: Provides personalized movie recommendations to users based on similar user preferences, thereby enhancing user experience and engagement.

## Technologies Used

- **Python**: Primary programming language for scripting and analysis.
- **Pandas**: For efficient data manipulation and aggregation.
- **NumPy**: Utilized for its powerful numerical array objects.
- **Scikit-learn**: For implementing machine learning algorithms and data processing tools.
- **Seaborn**: Incorporated for preliminary data exploration and visualization (though specific examples are not included in the notebook).
- **Ipywidgets**: For creating interactive elements within the Jupyter Notebook to dynamically display analysis results.

## Installation

Ensure Python is installed on your machine, then install the necessary libraries using the following commands:

```bash
pip install pandas numpy seaborn scikit-learn ipywidgets
```

## Usage

1. Clone the repository:
   ```bash
   git clone git@github.com:jrobin11/Movie-Recommendation.git
   ```
2. Navigate to the directory containing the notebook:
   ```bash
   cd path_to_notebook
   ```
3. Launch Jupyter Notebook to interact with the project:
   ```bash
   jupyter notebook "Collaborative Recommender Engine.ipynb"
   ```

Follow the detailed steps within the notebook to execute the data processing, model training, and recommendation phases.

## Acknowledgments

- Special thanks to the Data Mining class instructors and peers at Penn State University for their insights and feedback.
