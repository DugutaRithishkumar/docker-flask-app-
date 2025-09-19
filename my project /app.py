from flask import Flask

# Create an instance of the Flask class.
# __name__ is a special Python variable that gets the name of the current module.
app = Flask(__name__)

# A simple page that says hello
@app.route('/')
def hello():
    """Returns a simple greeting."""
    return 'Hello, World!'

# This block ensures the server only runs when the script is executed directly
# (and not when it's imported into another script).
if __name__ == "__main__":
    # Runs the app on host 0.0.0.0 to make it accessible from outside the container
    # and on the port you exposed in your Dockerfile.
    app.run(host="0.0.0.0", port=8000)
