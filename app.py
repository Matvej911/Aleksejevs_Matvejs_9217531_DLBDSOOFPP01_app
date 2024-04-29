from datetime import *
from create_table import *
from analytics import *

class Habit:
    def __init__(self, id, name, description, repeat, timeCheck, streak):
        #Initialize a Habit object with the provided attributes.
        self.id = id
        self.name = name
        self.description = description
        self.repeat = repeat
        self.timeCheck = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.streak = 0
    
    def add_habit(self):
        #Add a new habit to the database.
        existing_habits = get_all_habits()
        if any(habit[1] == self.name for habit in existing_habits):
            print(f"Habit '{self.name}' already exists.")
        else:
            add_new_habit(self.name, self.description, self.repeat, self.timeCheck, self.streak)
    
    def remove_habit(self):
        #Remove a habit from the database.
        existing_habits = get_all_habits()
        if any(habit[1] == self.name for habit in existing_habits):
            delete_habit(self.name)
            print(f"Habit '{self.name}' deleted successfully")
        else:
            print(f"Habit '{self.name}' does not exist.")
    

    def update_habit(self):
        #Update a habit in the database.
        existing_habits = get_all_habits()
        if any(habit[1] == self.name for habit in existing_habits):
            modify_habit(self.name, self.description, self.repeat)
            print(f"Habit '{self.name}' updated successfully.")
        else:
            print(f"Habit '{self.name}' does not exist.")

    def increase(self):
        #Increase the streak for the habit.
        self.streak = get_streak(self.name)
        self.streak += 1
        update_streak_in_db(self.name, self.streak, self.timeCheck)
    
    def reset_streak(self):
        #Reset the streak for the habit.
        self.streak = 1
        update_streak_in_db(self.name, self.streak, self.timeCheck)

    def complete_habit(self):
        #Mark the habit as completed.
        messages = []
        streak = get_streak(self.name)
        repeat = get_by_reapet(self.name)
        
        if repeat == 'daily':
            if streak == 0:
                self.increase()
                messages.append("Habit checked off successfully!")
            else:
                self.daily_habit()
                messages.append("Habit already checked today. Come again tomorrow.")
        elif repeat == 'weekly':
            if streak == 0:
                self.increase()
                messages.append("Habit checked off successfully!")
            else:
                self.weekly_repeat()
                messages.append("Habit already checked this week. Come again next week.")
        elif repeat == 'monthly':
            if streak == 0:
                self.increase()
                messages.append("Habit checked off successfully!")
            else:
                messages.append("Habit already checked this month. Come again next month.")
                self.monthly_repeat()
        else:
            messages.append("You can choose only daily, weekly, or monthly habits.")

        return messages

    def daily_habit(self):
        #Mark the habit as completed for the day.
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.name)
        
        if last:
            last_check = datetime.strptime(last[-1][0], format).date()
            if today - last_check < timedelta(days=1):
                return "Habit Already Checked Today. Come Again Tomorrow."
            elif today - last_check < timedelta(days=2):
                self.increase()
                return "Habit marked as completed for today."
            else:
                self.reset_streak()
                return "Streak reset. Habit marked as completed for today."
        else:
            self.increase()
            return "Habit marked as completed for today."

    def weekly_repeat(self):
        #Mark the habit as completed for the week.
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.name)
        
        if last:
            last_check = datetime.strptime(last[-1][0], format).date()
            if today - last_check < timedelta(days=7):
                return "Habit Already Checked this week. Come Again no the next week."
            elif today - last_check < timedelta(days=14):
                self.increase()
            else:
                self.reset_streak()
        else:
            self.increase()
    
    def monthly_repeat(self):
        #Mark the habit as completed for the month.
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.name)
        
        if last:
            last_check = datetime.strptime(last[-1][0], format).date()
            if today.month == last_check.month:
                return "Habit Already Checked this month. Come Again in the next month."
            elif today.year == last_check.year and today.month - last_check.month == 1:
                self.increase()
            else:
                self.reset_streak()
        else:
            self.increase()


     
     

    