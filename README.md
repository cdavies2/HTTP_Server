# Starting Up the Server
After you’ve downloaded the server, you can run it in a Linux command line, such as the Ubuntu terminal. First, change your directory to HTTP_Server, then create a virtual environment, using [these instructions](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment). Activate the virtual environment with the command “source .venv/bin/activate.” You should also make sure you have pip installed [Flask](https://flask.palletsprojects.com/en/2.3.x/installation/), and [requests](https://pypi.org/project/requests/). You can start running the server with the command “flask --app HelloWorld run "

# GET and PUSH Requests
In order to access all available functions of this server, you will need to utilize curl commands on a separate terminal from the one you’re running the server on. 

Open the server with the command 
```
curl -X GET http://127.0.0.1:5000
```
Push requests are performed with the command below, with the data you wish to post in place of "value"
```
curl -X POST -d “value” http://127.0.0.1:5000
```

To gain access to the Pokemon API, use the command below, replacing “type” with the Pokemon of your choice.
```
curl -X GET http://127.0.0.1:5000/pokemon/{type}
```

