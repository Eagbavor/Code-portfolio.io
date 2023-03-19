from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Define the index route
@app.route('/')
def index():
    return render_template("C:\Users\Eliab\Downloads\Portfolio website\Eliab's Portfolio.html")

# Define the contact route
@app.route('/contact')
def contact():
    return render_template('C:\Users\Eliab\Downloads\Portfolio website\Contact Me.html')

# Define the submit route
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save the data to the database
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    conn.close()

    # Redirect to the thank you page
    return render_template('C:\Users\Eliab\Downloads\Portfolio website\thank_you.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)
