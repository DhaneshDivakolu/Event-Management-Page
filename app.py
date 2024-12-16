from flask import Flask,render_template,request,redirect
import pymysql as sql

app = Flask(__name__)
my_connection = sql.connect(
    host="localhost",
    user ="dhanesh",
    password="dhanesh@4811",
    database="event-management"
)
my_cursor = my_connection.cursor()
table_query = """create table if not exists events (event_id int primary key auto_increment,
                event_name varchar(45), event_type varchar(45), event_desc varchar(200),
                org_email varchar(45), org_num varchar(15),max_seats int);
                """
my_cursor.execute(table_query)

book_table_query = """create table if not exists booking (booking_id int primary key auto_increment,
                    event_id int, book_date date, req_seats int, contact_email varchar(45) );
                    """
my_cursor.execute(book_table_query)

@app.route("/", methods = ["GET"])
def Homepage():
    return render_template("index.html")

@app.route("/register_events", methods = ["GET","POST"])
def register_events():
    if request.method == "POST":
        event_name = request.form["event_name"]
        event_type = request.form["type"]
        event_desc = request.form["event_desc"]
        org_email =request.form["org_email"]
        org_num = request.form["org_num"]
        max_seats = request.form["max_seats"]

        insert_query = """
                        insert into events(event_name,event_type,event_desc,org_email,org_num,max_seats) 
                        values(%s,%s,%s,%s,%s,%s);
                        """
        values=[event_name, event_type, event_desc, org_email, org_num, max_seats]
        my_cursor.execute(insert_query, values)
        my_connection.commit()
        return redirect("/register_events")

    return render_template("register.html")

@app.route("/view_events", methods = ["GET"])
def view_events():
    read_query = """
                    select * from events
                    """
    my_cursor.execute(read_query)
    raw = my_cursor.fetchall()
    return render_template("viewevent.html", output = raw)

@app.route("/book_events", methods = ["GET","POST"])
def book_events():
    if request.method == "POST":
        event_id = int(request.form["event_id"])
        b_date = request.form["date"]
        req_seats = int(request.form["req_seats"])
        c_email =  request.form["c_email"]

        check_query ="""
                        select max_seats from events where event_id=%s"""
        values = [event_id]
        my_cursor.execute(check_query,values)
        feached = my_cursor.fetchall()

        if not feached:
            return "Invalid Event Id"
        else:
            check_query="""
                            select book_date from booking where event_id=%s and book_date=%s
                            """
            values = [event_id,b_date]
            my_cursor.execute(check_query,values)
            booked=my_cursor.fetchall()
            if booked:
                return "slots not Available"
            max_seats = feached[0][0]
            if req_seats>max_seats:
                return f"Cannot book seats more than {max_seats}"
            else:
                insert_query ="""
                        insert into booking (event_id, book_date, req_seats, contact_email) 
                        values(%s,%s,%s,%s);
                    """
                values = [event_id, b_date, req_seats, c_email]
                my_cursor.execute(insert_query,values)
                my_connection.commit()
                return "Booking Successful"
            
    return render_template("bookevent.html")

@app.route("/bookings_events", methods = ["GET","POST"])
def bookings_events():
    read_query ="""select * from booking"""
    my_cursor.execute(read_query)
    raw = my_cursor.fetchall()
    return render_template("bookings.html", output= raw)

@app.route("/cancel_events", methods = ["GET","POST"])
def cancel_events():
    if request.method == "POST":
        b_id = int(request.form["b_id"])
        delete_query = """delete from booking where booking_id= %s """
        values = [b_id]
        my_cursor.execute(delete_query,values)
        my_connection.commit()
        return "Cancelled Successfully"
    return render_template("cancelbooking.html")

@app.route("/filter_events", methods = ["GET","POST"])
def filter_events():
    if request.method == "POST":
        d = request.form["book_date"]
        read_query = """select * from booking where book_date = %s """
        Values = [d]
        my_cursor.execute(read_query,Values)
        raw = my_cursor.fetchall()
        print(raw)
        return render_template("filterevent.html", output = raw)
    return render_template("filterevent.html")

@app.route("/search_events", methods = ["GET","POST"])
def search_events():
    if request.method == "POST":
        b_id = int(request.form["b_id"])
        search_query = """select * from booking where booking_id= %s """
        values = [b_id]
        my_cursor.execute(search_query,values)
        raw = my_cursor.fetchall()
        print(raw)
        return render_template("searchevent.html", output = raw)
    return render_template("searchevent.html")

app.run(debug=True)