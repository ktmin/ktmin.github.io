import os
import json
import sqlite3
from todo import models
from models import Model

# From: https://goo.gl/YzypOI
def singleton(cls):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls()
    return instances[cls]
  return getinstance

class DB(object):
    """
    DB driver for the Todo app - deals with writing entities
    to the DB and reading entities from the DB
    """

    def __init__(self):
        self.conn = sqlite3.connect("todo.db", check_same_thread=False)
        self.create_user_table()
        # TODO - Create all other tables here
        #self.set_up_routines()

    def set_up_routines(self):
        self.create_routines_table()
        self.add_routine("Routine 1", "Weight Loss", "Easy", "Band Pull Apart", "Standing Military Press","Upright Barbell", "15 reps, 3 sets", "8-12 reps, 5sets", "8-12 reps,3 sets", "https://www.bodybuilding.com/content/your-4-week-plan-for-guaranteed-fat-loss.html" )
        self.add_routine("Routine 2", "Weight Loss", "Medium", "Band Standing Abductions", "Lateral Band Walk", "Standing Leg Curl", "15 reps, 3 sets", "15 reps, 3 sets", "8-12 reps, 3-5 sets", "https://www.bodybuilding.com/content/your-4-week-plan-for-guaranteed-fat-loss.html")
        self.add_routine("Routine 3", "Weight Loss", "Hard", "Wide-Grip Lat Pulldown", "Bent Over Barbell Row", "Leverage High Row","12 reps, 5 sets", "12 reps, 5 sets","15 reps, 5 sets", "https://www.bodybuilding.com/content/your-4-week-plan-for-guaranteed-fat-loss.html")
        self.add_routine("Routine 4", "Stay Fit", "Easy", "Barbell Bench Press", "Medicine-Ball Push-Up", "Lateral Band Walk","Medium Grip 7 reps, 1 set",  "20 reps, 4 sets","15 reps, 4 sets", "https://www.bodybuilding.com/content/how-to-lose-100-pounds-and-keep-it-off.html")
        self.add_routine("Routine 5", "Stay Fit", "Medium", "Barbell Squat To A Box", "Barbell Reverse Lunge", "Pallof Press","7 reps, 1 set",  "10 reps, 4 sets", "12 reps, 3 sets", "https://www.bodybuilding.com/content/how-to-lose-100-pounds-and-keep-it-off.html"  )
        self.add_routine("Routine 6", "Stay Fit", "Hard", "Dumbbell Bench Press", "T-Bar Row", "Triceps Overhead Extension with Rope","6 reps, 3 sets", "20 reps, 4 sets", "30, 15, 15, 15 reps, 4 sets", "https://www.bodybuilding.com/content/how-to-lose-100-pounds-and-keep-it-off.html")
        self.add_routine("Routine 7", "Strength", "Easy", "FRONT BARBELL SQUAT", "STANDING HIP-CONTROLLED ARTICULAR ROTATION", "ROMANIAN DEADLIFT", "3 sets of 5 reps, no rest", "3 sets of 2 reps per side, no rest", "3 sets of 5 reps, no rest", "https://www.bodybuilding.com/fun/use-inefficiency-to-burn-more-calories.html")
        self.add_routine("Routine 8", "Strength", "Medium", "BENCH PRESS", "SIDE-TO-SIDE HURDLE HOP", "SINGLE-LEG BARBELL SQUAT", "3 sets of 6 reps, no rest", "3 sets of 30 sec., rest 30 sec.", "3 sets of 6 reps per side, no rest", "https://www.bodybuilding.com/fun/use-inefficiency-to-burn-more-calories.html")
        self.add_routine("Routine 9", "Strength", "Hard", "BARBELL DEADLIFT", "HALF-KNEELING DUMBBELL SHOULDER PRESS", "SEATED DUMBBELL PRESS", "3 sets of 5 reps, no rest","3 sets of 30 seconds work with a weight you can do for 15-20 reps, rest 30 sec.", "3 sets of 5 reps, no rest", "https://www.bodybuilding.com/fun/use-inefficiency-to-burn-more-calories.html")

    def create_user_table(self):
    # TODO - Implement this to create a user table
        try:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS USERS
            (Name TEXT NOT NULL,
            Height INT NOT NULL,
            Weight INT NOT NULL,
            Age INT NOT NULL,
            Gender TEXT NOT NULL)
            """)
        except Exception as e: print e

    def create_routines_table(self):
    # TODO - Implement this to create a user table
      try:
        self.conn.execute("""
          CREATE TABLE IF NOT EXISTS ROUTINES
          (ID TEXT NOT NULL,
          CATEGORY TEXT NOT NULL,
          INTENSITY TEXT NOT NULL,
          EXERCISE1 TEXT NOT NULL,
          EXERCISE2 TEXT NOT NULL,
          EXERCISE3 TEXT NOT NULL,
          DURATION1 TEXT NOT NULL,
          DURATION2 TEXT NOT NULL,
          DURATION3 TEXT NOT NULL,
          URL TEXT NOT NULL)
        """)
      except Exception as e: print e

    def get_list_of_routines(self):
        cursor = self.conn.execute("""
            SELECT * FROM ROUTINES;
          """)
        list = []
        for row in cursor:
          routine = row[0]
          category = row[1]
          intensity = row[2]
          exercise1 = row[3]
          exercise2 = row[4]
          exercise3 = row[5]
          duration1 = row[6]
          duration2 = row[7]
          duration3 = row[8]
          url = row[9]
          dictionary = {
            "routine": routine,
            "category": category,
            "intensity": intensity,
            "exercise1": exercise1,
            "exercise2": exercise2,
            "exercise3": exercise3,
            "duration1": duration1,
            "duration2" : duration2,
            "duration3" : duration3,
            "url": url
          }

          list.append(dictionary)
        self.conn.execute("""
                DROP TABLE ROUTINES;
                """)
        self.conn.commit()
        return list


    def add_user(self, name, height, weight, age, gender):
    # Add a task to the table.
    #self.create_user_table()

      self.conn.execute("""
        INSERT INTO USERS
        (Name, Height, Weight, Age, Gender)
        VALUES(?,?,?,?,?);
        """, (name, height, weight, age, gender)
        )
      self.conn.commit()

    def add_routine(self, id, category, intensity, exercise1, exercise2, exercise3, duration1, duration2, duration3, url):
    #self.create_routine_table()

      self.conn.execute("""
        INSERT INTO ROUTINES
        (ID, CATEGORY, INTENSITY, EXERCISE1, EXERCISE2, EXERCISE3, DURATION1, DURATION2, DURATION3, URL)
        VALUES(?,?,?,?,?,?,?,?,?,?);
        """, (id, category, intensity, exercise1,exercise2,exercise3, duration1, duration2, duration3, url)
        )
      self.conn.commit()

    def delete_users_table(self):
    # TODO - Implement this to delete a task table
      self.conn.execute("""
        DROP TABLE USERS;
        """)
      self.conn.commit()

    def delete_user(self, name):
        #Delete specific task from the table
      self.conn.execute("""
        DELETE FROM USERS WHERE Name = (?) """,
        (name))
      self.conn.commit()

    def get_user_info_by_name(self, name):
    #Acquire a task by its ID
      cursor = self.conn.execute("""
        SELECT * FROM USERS WHERE Name = (?)""",
        (name,))
      self.conn.commit()
      for row in cursor:
        name = row[0]
        height = row[1]
        weight = row[2]
        age = row[3]
        gender = row[4]
        user_to_return = models.User(name, height, weight, age, gender)
      return user_to_return.to_dict()

    def example_create_table(self):
        """
        Demonstrates how to make a table. Silently error-handles
        (try-except) because the table might already exist.
        """
        try:
            self.conn.execute("""
              CREATE TABLE example
              (ID INT PRIMARY KEY NOT NULL,
              NAME TEXT NOT NULL,
              ADDRESS CHAR(50) NOT NULL);
            """)
        except Exception as e: print e

    def example_query(self):
        """
        Demonstrates how to execute a query.
        """
        cursor = self.conn.execute("""
            SELECT * FROM example;
          """)
        dictionaries = []
        for row in cursor:
          print "ID = ", row[0]
          print "NAME = ", row[1]
          print "ADDRESS = ", row[2], "\n"
          dictionary = {
            "id": row[0],
            "name": row[1],
            "address": row[2]
          }
          dictionaries.append(dictionary)

    def example_insert(self):
        """
        Demonstrates how to perform an insert operation.
        """
        self.conn.execute("""
        INSERT INTO example (ID,NAME,ADDRESS)
        VALUES (1, "Joe", "Ithaca, NY");
          """)
        self.conn.commit()


    # Only <=1 instance of the DB driver
    # exists within the app at all times
