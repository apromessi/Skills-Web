from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("application-form.html")

@app.route("/application-form", methods = ["POST"])
def application_form():
	firstname_in_python = request.form["firstname"]
	lastname = request.form["lastname"]
	position = request.form["position"]
	
	if request.form["salary"]:
		salary = request.form["salary"]
	else:
		salary = "[I guess you don't care about making money? Great, you're hired!]"
	
	return render_template("application-confirmation.html", 
		firstname_in_html=firstname_in_python,
		lastname=lastname, salary=salary,
		position=position)

if __name__ == "__main__":
    app.run(debug=True)