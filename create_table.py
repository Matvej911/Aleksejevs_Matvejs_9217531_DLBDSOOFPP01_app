import sqlite3
from datetime import *

def create_connection(db_name = 'habits.db'):
    """
    Create a database connection.
    
    Parameters:
        db_name (str): The name of the database file.
        
    Returns:
        con: The database connection object.
    """
    con = None
    try:
        con = sqlite3.connect(db_name)
        return con
    except:
          print("Erorr database connection")
    return con

def create_table(con, sql_table):
    #  Create a table in the database.
    try:
        c = con.cursor()
        c.execute(sql_table)
    except:
        print('Erorr database execution')

def add_new_habit(name, description, repeat, timeCheck=None, streak=0):
    """
    Add a new habit to the database.

    Parameters:
        name (str): The name of the habit.
        description (str): The description of the habit.
        repeat (str): The frequency of habit repetition (e.g., 'daily', 'weekly', 'monthly').
        timeCheck (str, optional): The time of habit checking. If None, current time is used. Defaults to None.
        streak (int, optional): The streak count of the habit. Defaults to 0.
    """
    con = create_connection('habits.db')
    if con is not None:
        try:
            if timeCheck is None:
                timeCheck = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Habit (name, description, repeat, timeCheck, streak) VALUES (?, ?, ?, ?, ?)",
                           (name, description, repeat, timeCheck, streak))
            cursor.execute("INSERT INTO AnaliticsHabbit (name, timeCheck, streak) VALUES (?, ?, ?)",
                           (name, timeCheck, streak))
            con.commit()
            print("New habit added successfully")
        except sqlite3.Error as e:
            print("Error adding new habit:", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')


def modify_habit(name, description, repeat):
    """
    Modify an existing habit in the database.

    Parameters:
        name (str): The name of the habit to modify.
        description (str): The updated description of the habit.
        repeat (str): The updated frequency of habit repetition (e.g., 'daily', 'weekly', 'monthly').
    """
    con = create_connection('habits.db')
    if con is not None:
        try:
            timeCheck = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = con.cursor()
            cursor.execute("UPDATE Habit SET description=?, repeat=?, timeCheck=? WHERE name=?",
                           (description, repeat, timeCheck, name))
            cursor.execute("UPDATE AnaliticsHabbit SET timeCheck=? WHERE name=?",
                           (timeCheck, name))
            con.commit()
        except sqlite3.Error as e:
            print("Error modifying habit:", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')

                   
def delete_habit(name):
    """
    Delete a habit from the database.

    Parameters:
        name (str): The name of the habit to delete.
    """
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("DELETE FROM Habit WHERE name=?", (name,))
            cursor.execute("DELETE FROM AnaliticsHabbit WHERE name=?",(name,))
            con.commit()
        except sqlite3.Error as e:
            print("Error deleting habit:", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')


def habit_exists(name):
    # Check if a habit exists in the database.
    con = sqlite3.connect('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM Habit WHERE name=?", (name,))
        count = cursor.fetchone()[0]
        return count > 0
    except sqlite3.Error as e:
        print("Error checking habit existence:", e)
        return False
    finally:
        con.close()

def get_streak(name):
    #Get the current streak of a habit from the main Habit table.
  
    con = sqlite3.connect('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT streak FROM Habit WHERE name=?", (name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0  
    finally:
        con.close()

def get_streak_max(name):
    # Get the maximum streak of a habit from the AnalyticsHabit table.
    con = sqlite3.connect('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT streak FROM AnaliticsHabbit WHERE name=?", (name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0  
    finally:
        con.close()
    
def get_by_reapet(name):
    # #Get the repeat type of a habit from the Habit table.
    con = sqlite3.connect('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT repeat FROM Habit WHERE name=?", (name,))
        return cursor.fetchall()[0][0]
    finally:
        con.close()

def update_streak_in_db(name, streak, timeCheck):
    #Update the streak and timeCheck of a habit in the Habit table and its corresponding record in the AnalyticsHabit table.
    con = sqlite3.connect('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE Habit SET streak=?, timeCheck=? WHERE name=?", (streak, timeCheck, name))
        
        cursor.execute("SELECT streak FROM AnaliticsHabbit WHERE name=?", (name,))
        analitics_streak = cursor.fetchone()
        if analitics_streak is not None and streak > analitics_streak[0]:
            cursor.execute("UPDATE AnaliticsHabbit SET streak=?, timeCheck=? WHERE name=?", (streak, timeCheck, name))
            
        con.commit()
    finally:
        con.close()
    

def check_habit(name, timeCheck=None, streak=0):
    # Add an entry for habit checking to the AnalyticsHabit table.
    con = create_connection('habits.db')
    cursor = con.cursor()
    if timeCheck is None:
        timeCheck = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO AnaliticsHabbit VALUES(?,?,?)", (name, timeCheck, streak))
    con.commit()

def find_name(name):
    #Find a habit by its name in the Habit table.
    con = create_connection('habits.db')
    try:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM Habit WHERE name=?", (name,))
        return cursor.fetchone()
    finally:
        con.close()

def last_checked(name):
    # Retrieve the last checked timestamp for a habit from the Habit table.
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("SELECT timeCheck FROM Habit WHERE name=?", (name,)) 
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching last checked date for habit '{name}':", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')
        return None


def data_for_table(db_name='habits.db'):
    """
    Create the Habit and AnaliticsHabbit tables in the database if they do not exist.

    Parameters:
        db_name (str, optional): The name of the database file. Defaults to 'habits.db'.
    """

    con = create_connection(db_name)

    sql_data = """CREATE TABLE IF NOT EXISTS Habit (
    id integer PRIMARY KEY,
    name text,
    description text,
    repeat text,
    timeCheck text,
    streak integer ); """

    sql_data_analytics = """CREATE TABLE IF NOT EXISTS AnaliticsHabbit (
    name text,
    timeCheck text,
    streak integer,
    FOREIGN KEY (name) REFERENCES Habit(name))"""

    if con is not None:
        create_table(con, sql_data)
        create_table(con, sql_data_analytics)
    else: 
        print('Erorr database creation')


if __name__ == '__main__':
    data_for_table()


    