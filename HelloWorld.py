from flask import Flask, request
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
        if request.method=='GET':
              return "Hello, World!"
        if request.method=='POST':
              return request.get_data()

@app.route('/pokemon/<type>', methods=['GET'])
def pokemon(type):
       if request.method=='GET':
              return 'https://pokeapi.co/api/v2/pokemon/' + type + "  "