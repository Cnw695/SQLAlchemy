# SQLAlchemy
### Climate Analysis and Exploration

* Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis is done  using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.
* Plot the results using the DataFrame plot method.
 
### Station Analysis

* Design a query multiple data queries
* Plot the results as a histogram with `bins=12`.

### Climate App
* Designed a Flask API based on the queries that you have just developed.
* Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

### Temperature Analysis I
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

* Use the average temperature as the bar height.

* Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).






