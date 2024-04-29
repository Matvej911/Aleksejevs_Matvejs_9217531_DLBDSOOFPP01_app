from create_table import *

def get_all_habits():
    #Fetch all habits from the database.
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Habit")
            habits = cursor.fetchall()
            return habits
        except sqlite3.Error as e:
            print("Error fetching all habits:", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')
        return []


def get_habits_by_period(repeat):
    #Fetch habits with a specific repeat frequency from the database.
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Habit WHERE repeat=?", (repeat,))
            habits = cursor.fetchall()
            return habits
        except sqlite3.Error as e:
            print(f"Error fetching habits with periodicity '{repeat}':", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')
        return []


def table_with_longest_streak():
    #Fetch the longest streak for each habit from the analytics table.
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("SELECT name, timeCheck, MAX(streak) FROM AnaliticsHabbit GROUP BY name")
            longest_streaks = cursor.fetchall()
            return longest_streaks
        except sqlite3.Error as e:
            print("Error fetching longest run streak for all habits:", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')
        return None

    
def get_longest_run_streak_for_habit(name):
    #Fetch the longest streak for a specific habit from the analytics table.
    con = create_connection('habits.db')
    if con is not None:
        try:
            cursor = con.cursor()
            cursor.execute("SELECT MAX(streak), name FROM AnaliticsHabbit WHERE name=?", (name,))
            long_streak = cursor.fetchall()
            return long_streak
        except sqlite3.Error as e:
            print(f"Error fetching longest run streak for habit '{name}':", e)
        finally:
            con.close()
    else:
        print('Error: Database connection is not established')
        return None
