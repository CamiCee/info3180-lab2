#! /usr/bin/env python
import datetime

from app import app
app.run(debug=True, host="0.0.0.0", port=8080)

def format_date_joined():
    now=datetime.datetime.now();
    date_joined=datetime.date(2018,2,6)
    print "Joined " + date_joined.strftime("%B, %Y")
