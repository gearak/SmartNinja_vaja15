from flask import Flask,render_template, request
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    some_text = 'Message from handler!'
    current_year = datetime.datetime.now().year
    cities = ["Boston", "Ljubljana", "Dunaj", "Beograd"]
    logged_in = True
    return render_template('index.html', some_text=some_text, current_year=current_year, cities=cities, logged_in=logged_in)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=["POST"])
def contact():
    contact_name= request.form.get('contact-name')
    contact_email = request.form.get('contact-email')
    contact_message = request.form.get('contact-message')
    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template('success.html')

if __name__ == '__main__':
    app.run()
