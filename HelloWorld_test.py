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
from flask import Flask, request
import requests
import unittest, json
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


# LLMs were asked to design unit tests for an HTTP server
# That used flask and requests      
class TestFlaskServer(unittest.TestCase):
       def setUp(self):
              # Flask Docs:
              # The setUp function is used to create a test client
              # Said client is called before each test function, creating a platform for testing
              self.app=app.test_client()
              self.app.testing=True
       def test_default_endpoint(self): #Modification of GPT-4 Test
              response=self.app.get('/') #make a get request to the default
              self.assertEqual(response.status_code, 200) #check the request was successful
              self.assertEqual(response.data.decode(), 'Hello, World!')
              #check the response to the default request is 'Hello, World', as written in the hello_world function
       def test_poke_endpoint(self): # not the same as any GPT-4 suggestions
              response=self.app.get('/pokemon/pikachu') #make a request to the pokemon api
              self.assertEqual(response.status_code, 200) #make sure the request works
              self.assertEqual(response.get_json(), requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()) 
              #make sure the response is from the appropriate part of the Pokemon API
              # response.get_json() ensures the response from the testing platform is in proper json format
       def test_invalid_request(self): #GPT-4 Test
              response=self.app.get('/invalid-endpoint') #send a request to nonexistant endpoint
              self.assertEqual(response.status_code, 404)
              #invalid request should have a status code of 404
       
       
if __name__=='__main__':
       unittest.main()
