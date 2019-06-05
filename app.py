from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import persist

app = Flask(__name__)

@app.route("/")
def home():
  userlist = persist.get_users()
  return render_template("home_template.html", userlist=userlist)

@app.route("/submit_name", methods=["POST"])
def submit_name():
  # do the stuff to add the name
  submittedName = request.form["name"]
  persist.add_user(submittedName)
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run()
