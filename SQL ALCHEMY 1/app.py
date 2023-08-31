# Import necessary libraries
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create connection to the SQLite database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the measurement and station tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Initialize Flask
app = Flask(__name__)

# Create Flask Routes

# Create the root route
@app.route("/")
def welcome():
    return (
        "Welcome to the Climate API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation - Precipitation data<br/>"
        "/api/v1.0/stations - List of weather stations<br/>"
        "/api/v1.0/tobs - Temperature observations<br/>"
        "/api/v1.0/start - Minimum, average, and maximum temperature from a start date<br/>"
        "/api/v1.0/start/end - Minimum, average, and maximum temperature between start and end dates"
    )

# Create a route to get precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    session.close()

    # Convert query results to a dictionary
    precip_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precip_dict)

# Create a route to get a list of weather stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations = session.query(Station.station).all()

    session.close()

    # Convert query results to a list
    station_list = list(np.ravel(stations))
    return jsonify(station_list)

# Create a route to get temperature observations
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= prev_year).all()

    session.close()

    # Convert query results to a list of dictionaries
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {"date": date, "tobs": tobs}
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
# Define function, set "start" date entered by user as parameter for start_date decorator 
def start_date(start):
    session = Session(engine) 

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

    # Create query for minimum, average, and max tobs where query date is greater than or equal to the date the user submits in URL
    start_date_tobs_results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close() 

    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_date_tobs_values =[]
    for min, avg, max in start_date_tobs_results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min"] = min
        start_date_tobs_dict["average"] = avg
        start_date_tobs_dict["max"] = max
        start_date_tobs_values.append(start_date_tobs_dict)
    
    return jsonify(start_date_tobs_values)

# Create a route that when given the start date only, returns the minimum, average, and maximum temperature observed for all dates greater than or equal to the start date entered by a user

@app.route("/api/v1.0/<start>/<end>")

# Define function, set start and end dates entered by user as parameters for start_end_date decorator
def Start_end_date(start, end):
    session = Session(engine)

    """Return a list of min, avg and max tobs between start and end dates entered"""
    
    # Create query for minimum, average, and max tobs where query date is greater than or equal to the start date and less than or equal to end date user submits in URL

    start_end_date_tobs_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()
  
    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_end_tobs_date_values = []
    for min, avg, max in start_end_date_tobs_results:
        start_end_tobs_date_dict = {}
        start_end_tobs_date_dict["min_temp"] = min
        start_end_tobs_date_dict["avg_temp"] = avg
        start_end_tobs_date_dict["max_temp"] = max
        start_end_tobs_date_values.append(start_end_tobs_date_dict) 
    

    return jsonify(start_end_tobs_date_value)
    
# Run the app if executed as the main program
if __name__ == '__main__':
    app.run(debug=True)
