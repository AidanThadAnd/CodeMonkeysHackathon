from flask import Flask

# Create an instance of the Flask Class
app = Flask(__name__)

# Define a route for the root URL ('/') that returns a "Hello, World!"
@app.route('/')
def hello_world():
        return 'Hello, World!'

# Run the application if this script is executed
if __name__ == '__main__':
        app.run(debug=True)