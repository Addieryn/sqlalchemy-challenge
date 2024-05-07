# Import the dependencies.
from flask import Flask, jsonify, render_template

import datetime as dt
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_date).all()
    
    all_results = {}
    for date, prcp in results:
        all_results[date] = prcp
    
    session.close()

    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def Stations():
    results = session.query(Measurement.station).group_by(Measurement.station).all()

    all_names = list(np.ravel(results))

    session.close()

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def Temperature():
    last_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results =  session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_date).filter(Measurement.station == 'USC00519281').all()

    all_results = {}
    for date, tobs in results:
        all_results[date] = tobs

    session.close()
        
    return jsonify(all_results)

@app.route("/api/v1.0/<start>")
def input_start(start):
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date 
    >= start).first()
#results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= start).first()

    session.close()

    return jsonify(list(results))

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).first()
#results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= start).filter(Measurement.date <= end).first()
    session.close()

    return jsonify(list(results))
   
if __name__ == "__main__":
    app.run(debug=True)
