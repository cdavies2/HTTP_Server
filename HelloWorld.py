from flask import Flask, request
import requests
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
        if request.method=='GET':
              return "Hello, World!"
        if request.method=='POST':
              return request.get_data()

@app.route('/pokemon/<name>', methods=['GET'])
def pokemon(name):
       if request.method=='GET':
              poke=requests.get('https://pokeapi.co/api/v2/pokemon/' + name)
              return poke.json()
