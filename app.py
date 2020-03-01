import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
postgresStr = ("sqlite:///Resources/hawaii.sqlite")
engine = create_engine(postgresStr)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")
    

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of percipitation"""
    # Query percipitation
    yearback= dt.date(2017,8,23)-dt.timedelta(days= 365)

    rain = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= yearback).order_by(Measurement.date).all()



    measuredprcp = []
    for date, prcp in rain:
        precipitation_dict={}
        precipitation_dict[date] = prcp
        measuredprcp.append(precipitation_dict)

    return jsonify(measuredprcp)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs"""
    # Query temp observations

    yearback= dt.date(2017,8,23)-dt.timedelta(days= 365)
    tempq = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= yearback).order_by(Measurement.date).all()
                     

    tempobs = []
    for date, tobs in tempq:
        temps_dict={}
        temps_dict[date] = tobs
        tempobs.append(temps_dict)


 

    return jsonify(tempobs)

@app.route("/api/v1.0/<date>")
def start(date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Start"""
    # Query start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date).all()
    return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Ranged"""
    # date range
    start_date = dt.date(start)
    end_date = dt.date(end)
    start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()



    return jsonify(start_end)

if __name__ == "__main__":
    app.run(debug=True)