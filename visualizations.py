from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def graph_medals(table, num):
    """
    Displays a bar plot of the distribution of total medals won
    by top n=num competing Olympic Committees (that often
    represent countries) in Olympian history.

    Args:
        table: A .csv file containing the distribution of all
               Olympic medals ever given
        num: An integer that represents how many of the top
             ranked countries should be displayed in the bar plot.
   
    Returns:
        This function does not return anything.
    """
    # convert pandas object into lists
    medals_for_all = [table.columns.values.tolist()] + table.values.tolist();
    
    # create lists that will hold the two variables
    countries = []
    medals =[]
    
    # populate the two lists with their corresponding values
    for row in medals_for_all[1:(len(medals_for_all)-1)]:
        country = row[0]
        countries.append(country)
        medal = int(row[15])
        medals.append(medal)
    
    # create a list that whole two-elemnt lists that represent
    # the country-medal pairs
    pairs = []
    i = 0
    for i in range(len(countries)):
        pairs.append([countries[i], medals[i]])
    
    # helper function that takes the second element, the total medals
    # that committee has won
    def takeMedal(pair):
        return pair[1]
    
    # sort the pairs list my medal count in descending order
    pairs.sort(key = takeMedal, reverse = True)
    
    # create new meda and country lists based on the sorted medals
    new_countries = []
    sorted_medals = []
    for pair in pairs:
        new_countries.append(pair[0])
        sorted_medals.append(pair[1])
    
    # code to format bar plot (taken from the internet)    
    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))
    # Horizontal Bar Plot
    ax.barh(new_countries[0:num + 1], sorted_medals[0:num + 1])
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    # Add x, y gridlines
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    # Show top values
    ax.invert_yaxis()
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(round((i.get_width()), 2)),
                 fontsize = 8, fontweight ='bold',
                 color ='grey')

    # Add Plot Title
    ax.set_title('Distribution of Olympic Medals by Country',
                 loc ='left', fontweight ='bold', fontsize = 20)

    # display plot
    plt.xlabel('Total Medals Won', fontweight ='bold', fontsize = 15)
    plt.ylabel('Countries', fontweight ='bold', fontsize = 15)
    plt.show()
    
    
def plot_MedalsvGDP(table1, table2):
    """
    Displays a correlation plot between the 

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    
    #creates list that holds two variables
    new_medals = []
    new_GDPs = []
    
    #To pull the GDPs of the medals table-more GDPs than countries with medals
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
   # puts row 2 from GDPS into points for the x_axis             
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
        
    #puts row 15 from Medals into points for the y_axis  
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
        
    #??????????????????        
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    #puts the new points into a scatter plot
    plt.scatter(xpoints, ypoints)
    
    #Gives the labels and title of 
    plt.title("Correlation between a Country’s GDP (PPP) and Total Medals Won", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    #display plot
    plt.show()
    
    return [x_points, y_points]

    
def plot_MedalsvGDP_noOutliers(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    
    #remove outliers, which happened to be the top 3 ranking nations in GDP
    GDPs = GDPs[4:]
    
    #creates list that holds two variables
    new_medals = []
    new_GDPs = []
    
    #To pull the GDPs of the medals list
for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
    #puts row 2 of new_GDPs into points for the x_axis                       
    x_points = []
    for row in new_GDPMarkdowns:
        x_points.append(int(row[2]))
    #puts row 15 of new_Medals into points for the y_axis    
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
    #????????????????????    
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    #To put new points into a scatter plot
    plt.scatter(xpoints, ypoints)
    #Puts labels on the axis' and the title
    plt.title("Correlation between a Country’s GDP (PPP) and Total Medals Won (No Outliers)", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)
    #displays the graph
    plt.show()
    
    return [x_points, y_points]


def plot_Gold_MedalsvGDP(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    
    #puts lists into the two variables
    new_medals = []
    new_GDPs = []
    orig_x = []
    
    #Pulls the GPDs of the medals list 
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
    #puts row 2 of GDPS into points for the x_axis
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
    #put row 15 of medals into points for the y_axis
    y_points = []
    for row in new_medals:
        y_points.append(int(row[12]))
    #??????????????????????????????????
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    #Put both points into a scatter plot
    plt.scatter(xpoints, ypoints)
    #Gives labels for both axis' and gives the plot a title
    plt.title("Correlation between a Country’s GDP (PPP) and Total Gold Medals Won", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Total Gold Medals Won", fontweight ='bold', fontsize = 15)
    #display plot
    plt.show()
    
    return [x_points, y_points]


def plot_Gold_MedalsvGDP_noOutliers(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();

    #remove outliers, which happened to be the top 3 ranking nations in GDP
    GDPs = GDPs[4:]

    #puts the lists into the two variables
    new_medals = []
    new_GDPs = []
    orig_x = []
    #pulls GDPs of the medals list
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
    #puts row 2 of GDPS into points for the x_axis
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
    #put row 15 of medals into points for the y_axis
    y_points = []
    for row in new_medals:
        y_points.append(int(row[12]))
    #?????????????????????????
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    #places both points into a scatter plot
    plt.scatter(xpoints, ypoints)
    #Gives labels to both axis' and titles the plot
    plt.title("Correlation between a Country’s GDP (PPP) and Total Gold Medals Won (No Outliers)", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Total Gold Medals Won", fontweight ='bold', fontsize = 15)
    #display the plot
    plt.show()
    
    return [x_points, y_points]
    
    
def plot_MedalsvGDP_per_Capita(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    # creates the lists that will hold the two variables   
    new_medals = []
    new_GDPs = []
    orig_x = []
    # pulls the GPDs of the medals list
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
    # puts row 2 of new_GDPS into points for the x_axis            
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
    #puts row 15 of new_Medals into points for the y_axis    
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
    #???????????????????????????????????????        
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    #puts points into a scatter plot
    plt.scatter(xpoints, ypoints)
    
    #Gives labels to both axis and gives the graph a title
    plt.title("Correlation Between a Country’s 2019 GDP (PPP) per Capita and Total Medals Won", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP per Capita", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)
    #display the scatter plot
    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvGDP_per_Capita_noOutliers(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    # creates the lists that will hold the two variables   
    new_medals = []
    new_GDPs = []
    orig_x = []
    #pulls GDPs of the medals list
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
                
    # remove United States, the sole outlier
    i = 0
    for i in range(len(orig_x)):
        row = new_medals[i]
        if "United States" in row[0]:
            new_medals.remove(row)
            new_GDPs.remove(new_GDPs[i])
            break
    # puts row 2 of new_GDPS into points for the x_axis             
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
     #puts row 15 of new_Medals into points for the y_axis   
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
    #????????????????????????????????       
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    #puts points into a scatter plot
    plt.scatter(xpoints, ypoints)
    #Gives labels to both axis and gives the graph a title
    plt.title("2019 GDP per Capita vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP per Capita", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)
    
    #displays plot
    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvIHDI(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist(); # y
    IHDIs = [table2.columns.values.tolist()] + table2.values.tolist(); # x
    # creates the lists that will hold the two variables
    new_medals = []
    new_IHDIs = []
    #pulls IHDI of the medals list
    for y in medals[1:]:
        for x in IHDIs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_IHDIs.append(x)
    #puts row 2 of IHDI into the points for x_axis
    x_points = []
    for row in new_IHDIs:
        x_points.append(Decimal(row[2]))
    #puts row 15 of Medals into the points for y_axis
    y_points = []
    for row in new_medals:
        y_points.append(Decimal(row[15]))
    #?????????????????????????????????
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    #puts points into a scatter plot
    plt.scatter(xpoints, ypoints)
    #Gives labels to both axis and gives the graph a title
    plt.title("2019 IHDI vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 IHDI", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    #displays plot
    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvIHDI_noOutliers(table1, table2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist(); # y
    IHDIs = [table2.columns.values.tolist()] + table2.values.tolist(); # x
    
    # creates the lists that will hold the two variables
    new_medals = []
    new_IHDIs = []
    orig_x = []
    #pulls IHDI of the medals list
    for y in medals[1:]:
        for x in IHDIs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_IHDIs.append(x)
                orig_x.append(x)

    # remove United States, the sole outlier
    i = 0
    for i in range(len(new_medals)):
        row = new_medals[i]
        if "United States" in row[0]:
            new_medals.remove(row)
            new_IHDIs.remove(new_IHDIs[i])
            break
    #puts row 2 of IHDI into the points for x_axis            
    x_points = []
    for row in new_IHDIs:
        x_points.append(Decimal(row[2]))
    #puts row 15 of Medals into the points for y_axis
    y_points = []
    for row in new_medals:
        y_points.append(Decimal(row[15]))
    #???????????????????????????
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    #puts points into scatter plot
    plt.scatter(xpoints, ypoints)
    #Gives labels to both axis and gives the graph a title
    plt.title("2019 IHDI vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 IHDI", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    #display plot
    plt.show()
    
    return [x_points, y_points]
