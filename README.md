# NBA Prop Model

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
   - Specify the player's position in the file path. Line 118.

     ```python
     # Specify the file path
     file_path = 'rotowire-NBA-defense-vs-pos (c).csv'  # corresponds with "Center" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (PG).csv'  # corresponds with "Point Guard" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (SG).csv'  # corresponds with "Shooting Guard" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (SF).csv'  # corresponds with "Small Forward" DvP data for Full Season
     file_path = 'rotowire-NBA-defense-vs-pos (PF).csv'  # corresponds with "Power Forward" DvP data for Full Season
     ```

   - Update Opponent Abbreviation. Line 123:

     ```python
     # Set the search term to the desired team name
     search_term = 'CHA'  # Replace with opponent team abbreviation
     ```

4. **Specify Player Name:**
   - Replace 'Chet Holmgren' in the `player_name` variable with the name of the player for whom you want to make predictions. Line 132.

5. **Run the Python Script:**
   - Run the script.

6. **View the Results:**
   - The script will print predictions for the specified player's name based on hyperparameter-tuned Gradient Boosting models.
   - Results for different categories (Points, Rebounds, Assists, 3PM) will be displayed.
