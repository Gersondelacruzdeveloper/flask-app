import os
import json 
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template('index.html', page_title="home Gerson")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", 'r') as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title="about Gerson", list_of_numbers = [1,2,3,4,5], company=data)



@app.route("/about/<member_name>")
def about_name(member_name):
    member = {}
    with open("data/company.json", 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    return render_template('detail.html', detail=member)


@app.route("/contact",methods=["GET", "POST"] )
def contact():
    if request.method == 'POST':
        # print(request.form.get('name'))
        # print(request.form['email'])
        flash("Thanks {}, we have received your message!".format(request.form.get("name")))
    return render_template('contact.html', page_title="contact Gerson")


@app.route("/careers")
def careers():
    return render_template('careers.html', page_title='careers gerson')

if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get("port", '500')),
        debug = False
)
