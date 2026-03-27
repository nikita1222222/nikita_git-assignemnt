
#2. Create a new branch named <your_name>_new (e.g., Tutedude_new).
#      nikita_new
#Update the content of the JSON file used for the /api route in this branch.
# updated contect of JSON files
#Merge the <your_name>_new branch into the main branch.
#If there are conflicts during the merge, resolve them by accepting the changes from the <your_name>_new branch.
#Add the resolved changes to the staging area, commit them, and push the updates to the remote repository.


#1. Create a Flask application with an /api route. When this route is accessed, 
#it should return a JSON list. The data should be stored in a backend file, read from it, 
#and sent as a response. 


from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():

    day = datetime.today().strftime('%A')
    date = datetime.today()
    return render_template('index.html', day=day, date=date)


@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')

    age = int (age)
    result = {
        'name': name, 
        'age': age,
    }
    return result

if __name__=="__main__":
    app.run(debug=True)