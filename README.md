# NBA Player Stat Predictor

## Predicting Basketball Player Performance Statistics

To install and run the provided code on a new computer, follow these instructions:

### Prerequisites

- Ensure you have Python installed on your computer.
- Install required Python packages using the following command in your terminal or command prompt:

  ```bash
  pip install pandas nba_api scikit-learn numpy
  ```

### Steps to Run the Code

1. **Download the Code:**
   - Download and save the provided code: [NBA Prop Model.py](NBA%20Prop%20Model.py).

2. **Download the Opponent Stats CSV File:**
   - Visit the provided Google Drive link: [DvP CSV Files](https://drive.google.com/drive/folders/1i_t_nJHFfbDk7cENxkQ3NPwijEy9fzG5?usp=drive_link).
   - Manually download the necessary CSV files and save them in the same directory as your Python script.

3. **Adjust File Path and Team Abbreviation:**
   - Replace `'rotowire-NBA-defense-vs-pos (c).csv'` with the correct file path pointing to the Defense vs. Position (DvP) data file.
   - Specify the player's position in the file path.

     ```python
     # Specify the file path
     file_path = 'rotowire-NBA-defense-vs-pos (c).csv'  # corresponds with "Center" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (PG).csv'  # corresponds with "Point Guard" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (SG).csv'  # corresponds with "Shooting Guard" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (SF).csv'  # corresponds with "Small Forward" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (PF).csv'  # corresponds with "Power Forward" DvP data for Full Season
     ```

   - If adjusting timeframes, DvP data is available for Last 5 Games, Last 10 Games, and Full Season. Update the file path accordingly:

     ```python
     file_path = 'rotowire-NBA-defense-vs-pos (c10).csv'  # corresponds with "Center" DvP data Last 10 Games
     file_path = 'rotowire-NBA-defense-vs-pos (PG10).csv'  # corresponds with "Point Guard" DvP data Last 10 Games
     file_path = 'rotowire-NBA-defense-vs-pos (SG10).csv'  # corresponds with "Shooting Guard" DvP data Last 10 Games
     file_path = 'rotowire-NBA-defense-vs-pos (SF10).csv'  # corresponds with "Small Forward" DvP data Last 10 Games
     file_path = 'rotowire-NBA-defense-vs-pos (PF10).csv'  # corresponds with "Power Forward" DvP data Last 10 Games

     file_path = 'rotowire-NBA-defense-vs-pos (c5).csv'  # corresponds with "Center" DvP data Last 5 Games
     file_path = 'rotowire-NBA-defense-vs-pos (PG5).csv'  # corresponds with "Point Guard" DvP data Last 5 Games
     file_path = 'rotowire-NBA-defense-vs-pos (SG5).csv'  # corresponds with "Shooting Guard" DvP data Last 5 Games
     file_path = 'rotowire-NBA-defense-vs-pos (SF5).csv'  # corresponds with "Small Forward" DvP data Last 5 Games
     file_path = 'rotowire-NBA-defense-vs-pos (PF5).csv'  # corresponds with "Power Forward" DvP data Last 5 Games
     ```

   - Update Opponent Abbreviation:

     ```python
     # Set the search term to the desired team name
     search_term = 'CHA'  # Replace with opponent team abbreviation
     ```

4. **Specify Player Name:**
   - Replace 'Chet Holmgren' in the `player_name` variable with the name of the player for whom you want to make predictions.

5. **Run the Python Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing your Python script and the CSV file.
   - Run the script using the command:

     ```bash
     python NBA_Prop_Model.py
     ```

6. **View the Results:**
   - The script will print predictions for the specified player's name based on hyperparameter-tuned Gradient Boosting models.
   - Results for different categories (Points, Rebounds, Assists, 3PM) will be displayed.

**Note:** The code strategically focuses on the player's most recent 5 games and the defense data from their last 5 games. To adjust the timeframe for analysis, locate the "if player_id:" function and navigate to line 143. Change the number in 'head()' to the desired recent games (e.g., `df = df.head(10)` for the most recent 10 games). Comment the line to run for the full season, `#df = df.head(5)`.
