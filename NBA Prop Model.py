import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
import warnings
from sklearn.exceptions import DataConversionWarning

# Set seed for reproducibility
np.random.seed(42)

# Suppress DataConversionWarning
warnings.filterwarnings("ignore", category=DataConversionWarning)

# Function to get player ID by name
def get_player_id(player_name):
    player_list = players.find_players_by_full_name(player_name)
    if player_list:
        return player_list[0]['id']
    else:
        return None

# Function to extract opponent team from matchup
def get_opponent_team(matchup, team_mapping):
    opponent_team = team_mapping.get(matchup[-3:], None)
    return opponent_team

# Gradient Boosting Regressor function with MSE and hyperparameter tuning
def gradient_boosting_tune(X, Y):
    model = GradientBoostingRegressor()
    param_grid = {
        'n_estimators': [5, 10, 20, 50],  # Adjust as needed
        'learning_rate': [0.01, 0.05, 0.1, 0.2]  # Adjust as needed
    }
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X, Y)

    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    return best_model, best_params, best_score

# Gradient Boosting Predictor function
def gradient_boosting_predict(X, Y, input_values, best_model):
    # Check if input_values is a list or a single value
    if isinstance(input_values, list):
        input_array = np.array([input_values])
    else:
        input_array = np.array([input_values])

    # Ensure the input_array has the same number of features as the training data
    if input_array.shape[1] != X.shape[1]:
        # If there's a mismatch, remove the last column from input_array
        input_array = input_array[:, :-1]

    predicted_values = best_model.predict(input_array)
    mse = np.mean((Y - best_model.predict(X))**2)

    return predicted_values, mse

#Function to find opponent stats for inputs values
def search_opponent_stats(opponent_stats_df, search_term, column_numbers_list, x_columns_list, y_columns_list):
    try:
        # Find the row with the specified search term in column 'Team'
        row = opponent_stats_df[opponent_stats_df['TEAM'] == search_term]

        if not row.empty:
            values_list = []
            for column_numbers, x_columns, y_columns in zip(column_numbers_list, x_columns_list, y_columns_list):
                # Extract values for specified columns
                values = [float(row.iloc[0, col - 1]) for col in column_numbers]
                values_list.append(values)

            # Calculate the average of column 2 and add it to the values list
            average_column_2 = np.mean(opponent_stats_df.iloc[:, 2].values)
            for v_list in values_list:
                v_list.append(average_column_2)

            return values_list
        else:
            print(f"Did not find '{search_term}' in column 'Team'.")
            return None

    except FileNotFoundError:
        print(f"File not found.")
        return None

# Function to perform Gradient Boosting prediction and print the results
def predict_and_print(df, x_columns, y_columns, input_values, best_model, result_name):
    predicted_values, mse = gradient_boosting_predict(df.iloc[:, x_columns].values, df.iloc[:, y_columns].values, input_values, best_model)
    rounded_values = np.round(predicted_values, 2)

    # Print the input values
    #print(f"Input values for prediction ({', '.join(map(str, input_values))}):")

    # Print the predicted result
    print(f"Predicted {result_name}: {rounded_values[0]}")

# Gradient Boosting column indices and target variable indices
x_columns_1 = [22, 29, 28]      # DPTS, DFG%, D3PM
x_columns_2 = [23]              # DREB
x_columns_3 = [24]              # DAST
x_columns_4 = [28, 29, 22]      # D3PM, DFG%, DPTS
y_columns_1 = [18]              # Points
y_columns_2 = [12]              # Rebounds
y_columns_3 = [13]              # Assists
y_columns_4 = [6]               # 3PM

# Gradient Boosting column indices and target variable indices for opponent stats
column_numbers_opponent_stats = [4, 11, 10]   # DPTS, DFG%, D3PM
column_numbers_1_opponent_stats = [5]         # DREB
column_numbers_2_opponent_stats = [6]         # DAST
column_numbers_3_opponent_stats = [10, 11, 4] # D3PM, DFG%, DPTS

# Specify the file path
file_path = 'rotowire-NBA-defense-vs-pos (c5).csv' # Replace '("")' with players position 
# Read the NBA Opponent Stats CSV file
opponent_stats_df = pd.read_csv(file_path)

# Set the search term to the desired team name
search_term = 'CHA'  # Replace with opponent team abbreviation

# Call the search_opponent_stats function to get values for all specified columns
values_list = search_opponent_stats(opponent_stats_df, search_term,
                                     [column_numbers_opponent_stats, column_numbers_1_opponent_stats, column_numbers_2_opponent_stats, column_numbers_3_opponent_stats],
                                     [x_columns_1, x_columns_2, x_columns_3, x_columns_4],
                                     [y_columns_1, y_columns_2, y_columns_3, y_columns_4])

# Specify the player's name
player_name = 'Chet Holmgren'  # Replace with the desired player's name

# Get the player ID
player_id = get_player_id(player_name)

if player_id:
    # Get player game log for the current season
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2023-24')
    df = gamelog.get_data_frames()[0]

    # Select specific rows 
    df = df.head(5)

    # Drop specific columns
    columns_to_drop = ['SEASON_ID', 'Game_ID', 'WL', 'PLUS_MINUS', 'VIDEO_AVAILABLE', 'Player_ID', 'FTM', 'FT_PCT']
    df = df.drop(columns=columns_to_drop)

    # Simplified mapping dictionary for 'MATCHUP' and 'Team'
    team_mapping = {
        'ATL': 'ATL',
        'BOS': 'BOS',
        'BKN': 'BKN',
        'CHA': 'CHA',
        'CHI': 'CHI',
        'CLE': 'CLE',
        'DAL': 'DAL',
        'DEN': 'DEN',
        'DET': 'DET',
        'GSW': 'GSW',
        'HOU': 'HOU',
        'IND': 'IND',
        'LAC': 'LAC',
        'LAL': 'LAL',
        'MEM': 'MEM',
        'MIA': 'MIA',
        'MIL': 'MIL',
        'MIN': 'MIN',
        'NOP': 'NOP',
        'NYK': 'NYK',
        'OKC': 'OKC',
        'ORL': 'ORL',
        'PHI': 'PHI',
        'PHX': 'PHX',
        'POR': 'POR',
        'SAC': 'SAC',
        'SAS': 'SAS',
        'TOR': 'TOR',
        'UTA': 'UTA',
        'WAS': 'WAS',
        # Add additional mappings as needed
    }

    # Apply the mapping function to create a new 'Team' column in the player game log DataFrame
    df['TEAM'] = df['MATCHUP'].apply(lambda x: get_opponent_team(x, team_mapping))

    # Merge the DataFrames based on the 'Team' column
    merged_df = pd.merge(df, opponent_stats_df, on='TEAM', how='left')

    # Print the player name
    print(player_name)

    # Perform hyperparameter tuning for Gradient Boosting
    param_grid = {
        'n_estimators': [5, 10, 20, 50],  # Adjust as needed
        'learning_rate': [0.01, 0.05, 0.1, 0.2]  # Adjust as needed
    }

    # Create a list of result names
    result_names = ["Points", "Rebounds", "Assists", "3PM"]  # Add "3PM" to the result names

# Perform hyperparameter tuning for each prediction
for i, (x_cols, y_cols, values) in enumerate(zip([x_columns_1, x_columns_2, x_columns_3, x_columns_4],
                                                 [y_columns_1, y_columns_2, y_columns_3, y_columns_4],
                                                 values_list)):
    x_values = values[:-1]  # Extract x_values (input values)
    y_values = values[-1]   # Extract y_values (target variable for printing)

    best_model, best_params, best_score = gradient_boosting_tune(merged_df.iloc[:, x_cols].values,
                                                                 merged_df.iloc[:, y_cols].values)
    # Use the best model for prediction
    predict_and_print(merged_df, x_cols, y_cols, x_values, best_model, result_names[i])
