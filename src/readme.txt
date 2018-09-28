config.py defines the configuration for the Flask app to run with. 

run.py is the run script for the Flask app.

test.py is the test script for the Flask app. This file tests all the necessary functionality. (create task, delete task(s), get task)

todo/__init__.py defines the Flask app instance. 

todo/models.py is defines the models of the application and parses the needed information of the task.

todo/routes.py defines all the routes (a.k.a. endpoints) that users will be able to interact with in order to create todo list items, delete todo list items, and list todo list items.