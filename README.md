# apacheSparkDemo
This is simple Apache Spark demo where a Producer application pushes data into queue and consumer application consumes data and pushes into a postgres database.

# Environtment Setup (Works in Mac with python 3.6)
Run the following steps to get th application running:
  1. Clone the repo locally and navigate to location where requirements.txt is present
  2. run "python3 -m venv env"
  3. run "source env/bin/activate"
  4. run "cd energy"
  5. run "pip install -r requirements.txt"
  6. run "python3 manage.py migrate"
  7. run "python3 manage.py load_nem_file <filepath>" where filepath refers to the nem13 filepath

# Test Usage.
run "python3 manage.py test"

# Usage


That's it. Hope you enjoy this!



