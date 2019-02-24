from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'surveys'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def create_user():
    print("Got Post Info")
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birthday = request.form['birthday']
    email = request.form['email']
    initial_password = request.form['initial_password']
    confirm_password = request.form['confirm_password']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    
    return render_template('result.html')

@app.route('/result', methods=['POST'])
def formSubmitted():
    import datetime
    y = request.form['initial_password']
    z = request.form['birthday']
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['initial_password']) < 8 or len(request.form['confirm_password']) < 8 or request.form['initial_password'] != request.form['confirm_password'] or len(request.form['comment']) > 120 or type(request.form['first_name']) == int or type(request.form['last_name']) == int or any(x.isupper() for x in y) == False or any(char.isdigit() for char in y) == False or z >= datetime.today().date():
        flash("First/last names, and e-mail cannot be empty, birthday must be in the past, passwords must match, be at least 8 characters long, and have at least 1 uppercase letter and 1 number, and comment box cannot be more than 120 characters long.")
        return redirect('/')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birthday = request.form['birthday']
        email = request.form['email']
        initial_password = request.form['initial_password']
        confirm_password = request.form['confirm_password']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template('result.html')

@app.route('/danger')
def dangerFunction():
    print ("a user tried to visit /danger")
    return redirect("/")

@app.route('/restart', methods=['GET'])
def startAgain():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    
    app.run(debug=True) 