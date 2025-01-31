# Starting Up the Server
After you’ve cloned the repo, you can run it in a shell, such as the Ubuntu terminal. First, change your directory to the repo, then create a virtual environment, using [these instructions](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment). Activate the virtual environment with this command:
```
source .venv/bin/activate
```

You should also make sure you have installed the dependencies (Flask and requests). Do so with this command:
```
pip install -r requirements.txt
```

You can start running the server with this command:
```
flask --app HelloWorld run
```

# GET and POST Requests
In order to access all available functions of this server, you can utilize curl commands on a separate terminal from the one you’re running the server on. 

Perform a GET request with the command below
```
curl -X GET http://127.0.0.1:5000
```
POST requests are performed with the command below, with the data you wish to post in place of "value"
```
curl -X POST -d “value” http://127.0.0.1:5000
```

To gain access to the Pokemon API, use the command below, replacing “name” with the Pokemon of your choice.
```
curl -X GET http://127.0.0.1:5000/pokemon/name
```

# Running Unit Tests
Unit tests verify that our server connects and performs requests properly.
The pytest command runs unit tests and shows if they were successful
A file must be named "test_...py" or "..._test.py" for this to work
Run the command below in the server's directory to execute unit tests
```
pytest
```
