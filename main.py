from flask import Flask, render_template, request
from app import Habit
from analytics import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        repeat = request.form['repeat']
        
        # Check if the habit already exists
        existing_habits = get_all_habits()
        if any(habit[1] == name for habit in existing_habits):
            error_message = f"Habit '{name}' already exists."
            return render_template('create.html', error_message=error_message)
        
        # If the habit doesn't exist, add it
        new_habit = Habit(None, name, description, repeat, None, 0)
        new_habit.add_habit()
        
        success_message = f"Habit '{name}' created successfully!"
        return render_template('create.html', success_message=success_message)

    return render_template('create.html')


@app.route('/remove', methods=['GET', 'POST'])
def remove_habit():
    message = None
    
    if request.method == 'POST':
        name = request.form["name"]
        
        if not habit_exists(name):
            message = f"Habit '{name}' does not exist."
        else:
            habit_to_remove = Habit(id=None, name=name, description=None, repeat=None, timeCheck=None, streak=0)
            habit_to_remove.remove_habit()
            message = f"Habit '{name}' deleted successfully."
    
    return render_template('remove.html', message=message)

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    modify_message = None
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        repeat = request.form['repeat']
        
        # Update the habit
        new_habit = Habit(None, name, description, repeat, None, 0)
        new_habit.update_habit()
        
        modify_message = f"Habit '{name}' modified successfully!"
    
    # Get all habits from the database
    habits = get_all_habits()
    return render_template('modify.html', habits=habits, modify_message=modify_message)
    

@app.route('/check_off', methods=['GET', 'POST'])
def check_off():
    check_messages = []
    if request.method == 'POST':
        name = request.form['name']
        new_habit = Habit(None, name, None, None, None, 0)
        check_messages = new_habit.complete_habit()
    habits = get_all_habits()
    return render_template('check_off.html', habits=habits, check_messages=check_messages)


@app.route('/analyse')
def analyse():
    return render_template('analyse.html')


@app.route('/all_habits')
def all_habits():
    habits = get_all_habits()
    return render_template('all_habits.html', habits=habits)


@app.route('/habits_by_repeat', methods=['GET', 'POST'])
def habits_by_repeat():
    if request.method == 'POST':
        repeat = request.form['repeat']
        habits = get_habits_by_period(repeat)
        return render_template('habits_by_repeat.html', habits=habits)
    else:
        return render_template('habits_by_repeat.html')
    
@app.route('/longest_streak_all')
def longest_streak_all():
    habits = table_with_longest_streak()
    return render_template('longest_streak_all.html', habits=habits)


@app.route('/longest_streak', methods=['GET', 'POST'])
def longest_streak():
    if request.method == 'POST':
        name = request.form['name']
        streak = get_longest_run_streak_for_habit(name)
        return render_template('longest_streak.html', name=name, streak=streak)
    else:
        return render_template('longest_streak.html')



predefined_habits = [
    Habit(id=1, name='Eat Vegetables', description='Eat a serving of vegetables with each meal', repeat='daily', timeCheck=None, streak=0),
    Habit(id=2, name='Run', description='Run 5 kilometers', repeat='daily', timeCheck=None, streak=0),
    Habit(id=3, name='Yoga', description='Practice yoga for one hour', repeat='weekly', timeCheck=None, streak=0),
    Habit(id=4, name='Read', description='Read a book for 30 minutes', repeat='daily', timeCheck=None, streak=0),
    Habit(id=5, name='Learn New Skill', description='Spend one hour learning a new skill', repeat='monthly', timeCheck=None, streak=0)
]

for habit in predefined_habits:
    if not habit_exists(habit.name):
        habit.add_habit()


if __name__ == '__main__':
    app.run(debug=True)


