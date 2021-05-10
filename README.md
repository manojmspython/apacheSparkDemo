# apacheSparkDemo
This is simple Apache Spark demo where a Producer application pushes data into queue and consumer application consumes data and pushes into a postgres database.

# Environtment Setup (Works in Mac with python 3.6)
Run the following steps to get the application setup:
  1. Clone the repo locally and navigate to location where requirements.txt is present
  2. run "python3 -m venv env"
  3. run "source env/bin/activate"
  4. run "pip install -r requirements.txt"
  5. cd "aiven"
  6. Populate the config.py and test/config.py with appropriate details for connecting to KAFKA and postgres setup. 
  7. Run "python grant_permission.py" (Not necessary if all permissions are there)
  8. Run "python create_table" (Not necessary if table already present in postgres)

# Usage
Run the following steps to get th application running(assuming running inside virtaul env):
  1. open a commandline and run "python consumer.py" (To setup the consumer application)
  2. open another commandline and run "python producer.py" (To setup the producer application and send data it queue)
  3. Wait for few seconds and verify whether the data is pushed into postgres db by logging into pgAdmin and running the following query.
     "select * from public."Customers""
     
# Testing
The application has a simple test case solution to test producer and consumer are working as expected(assuming running inside virtaul env).
  1. cd "test"
  2. run "pytest -q"

# Special Thanks to following:
1. https://www.youtube.com/watch?v=R873BlNVUB4 : Well put video for understanding apache kafka.
2. https://pypi.org/project/kafka-python/ : Python Module which can interact with kafka seamlessly and given me idea so that i could produce simple python test case. 
  
That's it. Hope you enjoy this!



