# main.py

# Import the Flask module that has been installed.
import json
from flask import Flask, jsonify
import requests,logging

# Createing a "books" JSON / dict to emulate data coming from a database.
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]

api_url = "https://jsonplaceholder.typicode.com/todos"
api_posts = "https://jsonplaceholder.typicode.com/posts"

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.


@app.route("/", methods=["GET"])
# Generic Python functino that returns "Hello world!"
def index():
    response = requests.get(api_url)
    print(response)
    return response.text

@app.route("/posts", methods=["GET"])
# Generic Python functino that returns "Hello world!"
def posts():
    response = requests.get(api_posts)
    print(response.text)
    return response.text

# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/libros", methods=["GET"])
# Function that will run when the endpoint is hit.
def get_books():
    # Returns a JSON of the books defined above. jsonify is a Flask function that serializes the object for us.
    return jsonify(books)


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()
