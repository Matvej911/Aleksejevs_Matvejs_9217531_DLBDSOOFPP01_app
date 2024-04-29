from app import Habit
from freezegun import freeze_time
from create_table import *
"""
Here is an example of tracking data for a period of 7 weeks: on 2024-09-01, the user started two new habits, 'listening to music' and 'learning'. 
Using the tests, you can see how their streaks changed (increased or reset).

!!!!It is not possible to add historical records to the table because the function only allows making one record for each habit name.
"""

class TestHabitStreak:
    def test_daily_habit_1(self):
        # Test case for daily habit: Increment streak when habit is completed on consecutive days
        
        with freeze_time("2024-09-01"):
            # Initialize a daily habit for listening to music
            habit1 = Habit(id=1, name='listen_music', description='Listen to music for 30 minutes', repeat='daily', timeCheck=None, streak=0)
            # Add the habit
            habit1.add_habit()
            # Complete the habit for the day
            habit1.complete_habit()
            
            # Assert that streak is incremented to 1
            assert get_streak('listen_music') == 1
            # Assert that the longest streak is also updated to 1
            assert get_streak_max('listen_music') == 1
            
    def test_daily_habit_2(self):
        # Test case for daily habit: Increment streak on the next day
    
        with freeze_time("2024-09-02"):
            habit1 = Habit(id=1, name='listen_music', description='Listen to music for 30 minutes', repeat='daily', timeCheck=None, streak=0)
            # Complete the habit for the day
            habit1.complete_habit()
            assert get_streak('listen_music') == 2
            assert get_streak_max('listen_music') == 2
            
    def test_daily_habit_3(self):
        # Test case for daily habit: Streak reset because the person did not check off the habit the previous day, but the longest streak is saved
        
        with freeze_time("2024-09-04"):
            habit1 = Habit(id=1, name='listen_music', description='Listen to music for 30 minutes', repeat='daily', timeCheck=None, streak=0)
            # Complete the habit for the day
            habit1.complete_habit()
            
            # Assert that streak resets to 1 as the habit is not completed consecutively
            assert get_streak('listen_music') == 1
            # Assert that the longest streak remains 2
            assert get_streak_max('listen_music') == 2

    def test_weekly_habit_1(self):
        # Test case for weekly habit: Increment streak when habit is completed on consecutive weeks
        
        with freeze_time("2024-09-01"):
            # Initialize a weekly habit for learning
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Add the habit
            habit1.add_habit()
            # Complete the habit for the week
            habit1.complete_habit()
            
            # Assert that streak is incremented to 1
            assert get_streak('learning') == 1
            # Assert that the longest streak is also updated to 1
            assert get_streak_max('learning') == 1
            
    def test_weekly_habit_2(self):
        # Test case for weekly habit: Increment streak on the next week
        
        with freeze_time("2024-09-08"):
        
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Complete the habit for the week
            habit1.complete_habit()
        
            assert get_streak('learning') == 2
    
            assert get_streak_max('learning') == 2
            
    def test_weekly_habit_3(self):
        # Test case for weekly habit:  Streak reset because the person did not check off the habit the previous week, but the longest streak is saved
        
        with freeze_time("2024-09-23"):
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Complete the habit for the week
            habit1.complete_habit()
            
            # Assert that streak resets to 1 as the habit is not completed consecutively
            assert get_streak('learning') == 1
            # Assert that the longest streak remains 2
            assert get_streak_max('learning') == 2

    def test_weekly_habit_4(self):
        # Test case for weekly habit: Start new streak
        
        with freeze_time("2024-10-02"):
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Complete the habit for the week
            habit1.complete_habit()
            
            assert get_streak('learning') == 2
            assert get_streak_max('learning') == 2
            
    def test_weekly_habit_5(self):
        # Test case for weekly habit: Continuation of streak, longest streak updated and now = 3 
        
        with freeze_time("2024-10-10"): 
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Complete the habit for the week
            habit1.complete_habit()
            
            # Assert that streak increments to 3 as the habit is completed consecutively
            assert get_streak('learning') == 3
            # Assert that the longest streak increments to 3 as well
            assert get_streak_max('learning') == 3

    def test_weekly_habit_6(self):
        # Test case for weekly habit: Streak reset because the person did not check off the habit the previous week, but the longest streak is saved
        
        with freeze_time("2024-10-25"): 
            habit1 = Habit(id=1, name='learning', description='Spend 1 hour on learning new skills', repeat='weekly', timeCheck=None, streak=0)
            # Complete the habit for the week
            habit1.complete_habit()
            
            #  Assert that streak resets to 1 as the habit is not completed consecutively
            assert get_streak('learning') == 1
            # Assert that the longest streak seved
            assert get_streak_max('learning') == 3



