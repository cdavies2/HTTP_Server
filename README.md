# Starting Up the Server
After you’ve downloaded the server and virtual environment, you can run them in a Linux command line, such as the Ubuntu terminal. First, change your directory to HTTP_Server, and activate the virtual environment with the command “source .venv/bin/activate.” You can start running the server with the command “flask --app HelloWorld run 

# GET and PUSH Requests
In order to access all available functions of this server, you will need to utilize curl commands on a separate terminal from the one you’re running the server on. The command “curl -X GET http://127.0.0.1:5000” opens the server, push requests are performed with “curl -X POST -d “value” http://127.0.0.1:5000” (with the data you wish to post in parenthesis), and to gain access to the Pokemon API, use “curl -X GET http://127.0.0.1:5000/pokemon/{type}” (replacing “type” with the Pokemon of your choice).

