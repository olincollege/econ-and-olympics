# econ-and-olympics
A computational essay and its supporting code that delves into the relationship between economics and the prestigious Olympic games.

## Implementation

The Python file data_tables.py contains functions that output Pandas DataFrames that represent tables of relevant data from Wikipedia, i.e. Olympic medal history of countries and various measures of economic development for countries.

The Python file visualizations.py contains functions that print bar plots and correlation plots of the data passed to them from functions in data_tables.py. Each correltion-plot function also returns two lists representing the x and y data points being plotted.

The Python file analysis.py holds one function that calculates the Spearman Correlation Coefficient between two equally sized sets of data (the x and y points outputted by a correlation plot function in visualizans.py). It prints a statement that declares the correlation coefficient, and p-value of the staistical hypothesis test.