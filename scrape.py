from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
@app.route('/projects')
def projects():
    # Set up the GitLab API endpoint and access token
    endpoint = 'https://gitlab.com/api/v4/users/Eacode/projects'
    access_token = 'glpat-zryNya7RH9jEJUh4CpjA'
    headers = {'Authorization': f'Bearer {access_token}'}
    # Make a request to the GitLab API to retrieve the user's projects
    response = requests.get(endpoint, headers=headers)
    data = response.json()
    # Create a list of dictionaries containing project information
    projects = []
    for project in data:
        project_data = {
            'name': project['Read file'],
            'description': project['Importing csv file and reading it into memory'],
            'web_url': project['https://gitlab.com/Eacode/myproject']
        }
        projects.append(project_data)
    # Render your Projects page with the retrieved data
    return render_template('projects.html', data=projects)



if __name__ == '__main__':
    app.run(debug=True)
