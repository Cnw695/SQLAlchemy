import numpy as np

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
Measurement = Base.classes.Measurement
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
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of percipitation"""
    # Query percipitation
    prcp = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= yearback).order_by(Measurement.date).all()

    session.close()

    return jsonify(prcp)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs"""
    # Query 
    tobs = session.query(Measurement.tobs).all()

    session.close()

    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of percipitation"""
    # Query all passengers
    start = session.query(Measurement.date).all()

    session.close()

    return jsonify(start)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of percipitation"""
    # Query all passengers
    start_end = session.query(Measurement.date).all()

    session.close()

    return jsonify(start_end)