from create_table import *
from app import Habit


def test_successfully_added():
    # Create a new habit and add it to the database
    habit6 = Habit(id=6, name='Sleep', description='Sleep 8 hours', repeat='daily', timeCheck=None, streak=0)
    habit6.add_habit()

    # Verify that the habit is added to the database
    name = 'Sleep'
    result = find_name(name)
    assert result is not None


def test_successfully_completed():
    habit7 = Habit(id=6, name='Learning_Python', description='Study Python', repeat='daily', timeCheck=None, streak=0)
    habit7.add_habit()
    habit7.complete_habit()
    assert get_streak("Learning_Python") == 1  # Check that streak increased after completion


def test_successfully_removed():
    habit8 = Habit(id=6, name='Reading_books', description='Read for one hour', repeat='daily', timeCheck=None, streak=0)
    habit8.add_habit()
    habit8.remove_habit()
    name = 'Reading_books'
    result = find_name(name)  # Check that habit was removed
    assert result is None


def test_successfully_updated():
    habit9 = Habit(id=6, name='Reading_articles', description='Read articles for one hour', repeat='daily', timeCheck=None, streak=0)
    habit9.add_habit()
    modify_habit("Reading_articles", 'Reading_magazines', 'weekly')  # Check modification
    assert get_by_reapet("Reading_articles") == 'weekly'


def test_daily_habit():
    # Test that you cannot check off the same habit more than once in one day
    habit = Habit(id=1, name='Reading_newspapers', description='Read newspapers for one hour', repeat='daily', timeCheck=None, streak=0)
    habit.add_habit()
    habit.complete_habit()
    assert habit.daily_habit() == 'Habit Already Checked Today. Come Again Tomorrow.'


def test_weekly_habit():
    # Test that you cannot check off the same habit more than once in one week
    habit = Habit(id=1, name='Learning_French', description='Study French for one hour', repeat='weekly', timeCheck=None, streak=0)
    habit.add_habit()
    habit.complete_habit()
    assert habit.weekly_repeat() == "Habit Already Checked this week. Come Again no the next week."


def test_monthly_habit():
    # Test that you cannot check off the same habit more than once in one month
    habit = Habit(id=1, name='Exercising', description='Exercise for one hour', repeat='monthly', timeCheck=None, streak=0)
    habit.add_habit()
    habit.complete_habit()
    assert habit.monthly_repeat() == "Habit Already Checked this month. Come Again in the next month."

