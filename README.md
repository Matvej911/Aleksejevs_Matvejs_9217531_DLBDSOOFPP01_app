# Habit Tracking App

## Introduction

The Habit Tracker is a Python application designed to help users establish and track daily, weekly, or monthly habits. It provides functionalities for adding, removing, modifying, and tracking habits, along with analyzing streaks and progress over time.

### Features

- **Add New Habit**: Users can add new habits along with their descriptions and repeat frequencies (daily, weekly, or monthly).
- **Remove Habit**: Existing habits can be removed from the tracker.
- **Modify Habit**: Users can update the description and repeat frequency of existing habits.
- **Track Habit Completion**: Users can mark habits as completed, and the tracker automatically keeps track of streaks.
- **Analytics**: The application provides analytics to view all current habits, the longest run streaks for all habits or a specific habit.

## Testing

To test the application:

1. Clone the repository to your local machine.
2. Create a virtual environment.
3. Install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the following command to create a database table:

   ```bash
   python create_table.py
   ```

5. Run the test file to test the functions:

   ```bash
   pytest test.py
   ```

6. Run the second test file to test analytics:

   ```bash
   pytest test_predifined.py
   ```

7. After the tests are completed, delete the `habits.db` file, as all testing data is now stored in this database.

## Usage

To use the Habit Tracker:

1. Clone the repository to your local machine.
2. Create a virtual environment.
3. Install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the following command to create a table in the database:

   ```bash
   python create_table.py
   ```

5. Run the following command to start the Flask application:

   ```bash
   python main.py
   ```

6. You will see a link in the terminal. Click on it to open the application.

### How to Use

1. **Add New Habit**:

   - Navigate to the "Create" button.
   - Enter the habit name, description, and select the repeat frequency.
   - Click on "Create Habit" to add the habit to the database.

2. **Remove Habit**:

   - Navigate to the "Remove" button.
   - Enter the habit name you want to remove.
   - Click on "Remove" to delete the habit from the database.

3. **Modify Habit**:

   - Navigate to the "Modify" button.
   - Select the habit you want to modify from the dropdown menu.
   - Update the description and/or repeat frequency.
   - Click on "Modify Habit" to save the changes.

4. **Track Habit Completion**:

   - Navigate to the "Check Off" button.
   - Select the habit you want to mark as completed from the dropdown menu.
   - Click on "Done" to mark the habit as completed for the day, week or month.

5. **Analytics**:
   - Explore the "Analytics" section to view all habits, the longest run streaks for all habits or a specific habit and view habits by their repeat.
   - Analyze your progress over time and identify areas for improvement.

## Development

The project uses Python with Flask for the backend and SQLite for the database. It leverages FreezeGun for time manipulation during testing.

## Author

- [Matvejs Aleksejevs](https://github.com/Matvej911) - Project Developer

.
