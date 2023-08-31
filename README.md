# sqlalchemy_challenge
I completed the two-part SQL ALCHEMY challenge which involved:

Part 1: Climate Data Analysis
In this section, I utilized Python, SQLAlchemy, Pandas, and Matplotlib to analyze and explore a climate database. Using the provided files (climate_starter.ipynb and hawaii.sqlite), I connected to the SQLite database, reflected tables as classes with automap_base(), established a SQLAlchemy session, and conducted both precipitation and station analyses.

Part 2: Climate App Design
After the initial analysis, I designed a Flask API with the following routes:

/api/v1.0/precipitation: This route converted query results into a dictionary with dates as keys and precipitation as values, then returned the JSON representation of the dictionary.
/api/v1.0/stations: This route returned a JSON list of stations from the dataset.
/api/v1.0/tobs: I queried temperature observations for the most-active station over the previous year and returned a JSON list of the data.
/api/v1.0/<start> and /api/v1.0/<start>/<end>: For these routes, I returned JSON lists containing minimum, average, and maximum temperatures. Calculations were done for either a specific start date or a start-end date range.

During the challenge, I enhanced my understanding by researching and watching YouTube videos on SQLAlchemy. I faced an obstacle with a corrupted file that prevented my website from running, but after using the correct file from the resource folder, everything functioned well.. Overall, I found the challenge enjoyable, particularly the climate app design aspect.
