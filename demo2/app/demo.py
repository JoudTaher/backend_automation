from flask import Flask, render_template, request, flash
import os, socket, requests

app = Flask(__name__)

app.secret_key = os.environ.get('APP_SECRET_KEY', 'my_default_secret_key')  # Secret key for Flask to use flash()
function1_url = 'https://functionapp_name.azurewebsites.net/api/function_name' # Azure Function URL
function1_key = os.environ.get('FUNCTION1_KEY', 'MY_AZURE_FUNCTION_KEY') # Azure Function key. Better to read from environment variable

hostname = socket.gethostname()

# Homepage route to render the form
@app.route('/')
def index():
    return render_template('index.html', record=None)  # By default, no record is passed

# Form submission route
@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve name and state from the form
    name = request.form.get('name')
    state = request.form.get('state')

    # Define the Azure Function URL and append the parameters
    azure_function_url = 'https://http2mysqlfunc1instructor.azurewebsites.net/api/HTTP2MySQL'
    params = {
        'code': function1_key,
        'name': name,
        'state': state
    }

    # Send a request to the Azure Function
    try:
        response = requests.get(azure_function_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses

        # Pass the data back to the form so it can be displayed
        record = response.json()
        flash("Record inserted successfully!", "success")
        return render_template('index.html', record=record)

    except requests.exceptions.RequestException as e:
        flash(f"An error occurred: {e}", "error")
        return render_template('index.html', record=None)

if __name__ == '__main__':
    app.run()
