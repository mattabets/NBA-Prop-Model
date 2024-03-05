# NBA-Prop-Model
Predicting basketball player performance statistics

To install and run the provided code on a new computer, follow these instructions:

### Prerequisites:
1. Ensure you have Python installed on your computer.
2. Install required Python packages using the following command in your terminal or command prompt:

```bash
pip install pandas nba_api scikit-learn numpy
```

### Steps to Run the Code:

1. **Download the Code:**
   - Copy the provided code.
   - Create a new file (e.g., `basketball_prediction.py`) on your computer.
   - Paste the code into the file.

2. **Download the Opponent Stats CSV File:**
   - Visit the provided Google Drive link: [DvP CSV Files.](https://drive.google.com/drive/folders/1i_t_nJHFfbDk7cENxkQ3NPwijEy9fzG5?usp=drive_link)
   - Manually download the necessary CSV files and save them in the same directory as your Python script.

3. **Run the Python Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing your Python script and the CSV file.
   - Run the script using the command:

     ```bash
     python basketball_prediction.py
     ```

4. **View the Results:**
   - The script will print predictions for the specified player's name based on hyperparameter-tuned Gradient Boosting models.
   - Results for different categories (Points, Rebounds, Assists, 3PM) will be displayed.

Note: Ensure you have a stable internet connection during the execution of the script, as it relies on the NBA API to fetch player and game data.
