import flask
import authentication
import randomizer
app = flask.Flask(__name__)
app.template_folder = "."
app.static_folder = "."
app.static_url_path = "/static/"
@app.route("/login")
def login():
    return flask.render_template("html/index.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if (flask.request.method == "POST"):
        user = flask.request.form['username']
        password = flask.request.form['password_hash']
        authentication.Register().processRegister({"username": user, "passwordHash": password})
        return flask.render_template("html/profile.html")
    else:
        return flask.render_template("html/register.html")

@app.route("/preferences")
def preferences():
    return flask.render_template("html/preferences.html")

@app.route("/aboutus")
def aboutus():
    return flask.render_template("html/aboutus.html")

@app.route("/diceRoll")
def getDiceRoll():
    #user = randomizer.pickUsers(1)
    event = randomizer.pickEvent()
    venue = randomizer.pickVenue()
    return flask.render_template("html/roll_results.html",who="Todd Jones",what=event.attrib["name"],where=venue.attrib["name"],who_image="pp.jpg",what_image= "static/imgs/" + event.attrib["image"],where_image= "static/imgs/" + venue.attrib["image"])

app.run(host="127.0.0.1",port=80)
