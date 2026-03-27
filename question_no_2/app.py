
#2. Create a new branch named <your_name>_new (e.g., Tutedude_new).
#                git branch nikita_new
#Update the content of the JSON file used for the /api route in this branch.
#                updated contect of JSON files
#                git add app.py
#                git commit -m "app.py"
#                git push 
#Merge the <your_name>_new branch into the main branch.
#                git switch master
#                git merge nikita_new
#                git push
#If there are conflicts during the merge, resolve them by accepting the changes from the <your_name>_new branch.
#Add the resolved changes to the staging area, commit them, and push the updates to the remote repository.
#               there was no conflict as I created new repo


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