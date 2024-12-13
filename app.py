from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def Homepage():
    return render_template("index.html")

@app.route("/register_events", methods = ["GET","POST"])
def register_events():
    return render_template("register.html")

@app.route("/book_events", methods = ["GET","POST"])
def book_events():
    return render_template("bookevent.html")

@app.route("/bookings_events", methods = ["GET","POST"])
def bookings_events():
    return render_template("bookings.html")

@app.route("/cancel_events", methods = ["GET","POST"])
def cancel_events():
    return render_template("cancelbooking.html")

@app.route("/filter_events", methods = ["GET","POST"])
def filter_events():
    return render_template("filterevent.html")

@app.route("/search_events", methods = ["GET","POST"])
def search_events():
    return render_template("searchevent.html")

@app.route("/view_events", methods = ["GET","POST"])
def view_events():
    return render_template("viewevent.html")

@app.route("/viewb_events", methods = ["GET","POST"])
def viewb_events():
    return render_template("view_booking.html")

app.run(debug=True)