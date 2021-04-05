from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def graph_medals(table):
    # convert pandas object into lists
    medals_for_all = [table.columns.values.tolist()] + table.values.tolist();
    
    countries = []
    medals =[]

    for row in medals_for_all[1:(len(medals_for_all)-1)]:
        country = row[0]
        countries.append(country)
        medal = int(row[15])
        medals.append(medal)
    
    pairs = []
    i = 0
    for i in range(len(countries)):
        pairs.append([countries[i], medals[i]])
    
    def takeMedal(pair):
        return pair[1]
    
    pairs.sort(key = takeMedal, reverse = True)
    
    new_countries = []
    sorted_medals = []
    for pair in pairs:
        new_countries.append(pair[0])
        sorted_medals.append(pair[1])
    
    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))

    # Horizontal Bar Plot
    ax.barh(new_countries[0:31], sorted_medals[0:31])

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
                 fontsize = 10, fontweight ='bold',
                 color ='grey')

    # Add Plot Title
    ax.set_title('Distribution of Olympic Medals by Country',
                 loc ='left', fontweight ='bold', fontsize = 20)

    plt.xlabel('Total Medals Won', fontweight ='bold', fontsize = 15)
    plt.ylabel('Countries', fontweight ='bold', fontsize = 15)
    plt.show()
    
    
def plot_MedalsvGDP(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    
    new_medals = []
    new_GDPs = []
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
        
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
            
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    plt.scatter(xpoints, ypoints)
    
    plt.title("2019 GDP(PPP) vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]

    
def plot_MedalsvGDP_noOutliers(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
    
    #remove outliers, which happened to be the top 3 ranking nations in GDP
    GDPs = GDPs[4:]
    
    new_medals = []
    new_GDPs = []
    orig_x = []
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
                
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
        
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
           
    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    plt.scatter(xpoints, ypoints)
    
    plt.title("2019 GDP(PPP) vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]


def plot_Gold_MedalsvGDP(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();

    new_medals = []
    new_GDPs = []
    orig_x = []
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)

    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))

    y_points = []
    for row in new_medals:
        y_points.append(int(row[12]))

    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)

    plt.scatter(xpoints, ypoints)

    plt.title("2019 GDP(PPP) vs. Gold Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Total Gold Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]


def plot_Gold_MedalsvGDP_noOutliers(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();

    #remove outliers, which happened to be the top 3 ranking nations in GDP
    GDPs = GDPs[4:]

    new_medals = []
    new_GDPs = []
    orig_x = []
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)

    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))

    y_points = []
    for row in new_medals:
        y_points.append(int(row[12]))

    x_points = [x_point / 1000 for x_point in x_points]
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)

    plt.scatter(xpoints, ypoints)

    plt.title("2019 GDP(PPP) vs. Gold Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP(PPP)(in billions)", fontweight ='bold', fontsize = 15)
    plt.ylabel("Total Gold Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]
    
    
def plot_MedalsvGDP_per_Capita(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
        
    new_medals = []
    new_GDPs = []
    orig_x = []
    for y in medals[1:]:
        for x in GDPs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_GDPs.append(x)
                orig_x.append(x)
                
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
        
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
            
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    
    plt.scatter(xpoints, ypoints)
    
    plt.title("2019 GDP per Capita vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP per Capita", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvGDP_per_Capita_noOutliers(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist();
    GDPs = [table2.columns.values.tolist()] + table2.values.tolist();
        
    new_medals = []
    new_GDPs = []
    orig_x = []
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
                
    x_points = []
    for row in new_GDPs:
        x_points.append(int(row[2]))
        
    y_points = []
    for row in new_medals:
        y_points.append(int(row[15]))
           
    xpoints = np.array(x_points)
    ypoints = np.array(y_points)
    

    plt.scatter(xpoints, ypoints)
    
    plt.title("2019 GDP per Capita vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 GDP per Capita", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvIHDI(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist(); # y
    IHDIs = [table2.columns.values.tolist()] + table2.values.tolist(); # x

    new_medals = []
    new_IHDIs = []
    for y in medals[1:]:
        for x in IHDIs[1:]:
            if x[1] in y[0]:
                new_medals.append(y)
                new_IHDIs.append(x)
    
    x_points = []
    for row in new_IHDIs:
        x_points.append(Decimal(row[2]))

    y_points = []
    for row in new_medals:
        y_points.append(Decimal(row[15]))

    xpoints = np.array(x_points)
    ypoints = np.array(y_points)

    plt.scatter(xpoints, ypoints)

    plt.title("2019 IHDI vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 IHDI", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]
    

def plot_MedalsvIHDI_noOutliers(table1, table2):
    # convert pandas object into lists
    medals = [table1.columns.values.tolist()] + table1.values.tolist(); # y
    IHDIs = [table2.columns.values.tolist()] + table2.values.tolist(); # x

    new_medals = []
    new_IHDIs = []
    orig_x = []
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
                
    x_points = []
    for row in new_IHDIs:
        x_points.append(Decimal(row[2]))

    y_points = []
    for row in new_medals:
        y_points.append(Decimal(row[15]))

    xpoints = np.array(x_points)
    ypoints = np.array(y_points)

    plt.scatter(xpoints, ypoints)

    plt.title("2019 IHDI vs. Medals", fontweight ='bold', fontsize = 20)
    plt.xlabel("2019 IHDI", fontweight ='bold', fontsize = 15)
    plt.ylabel("Totals Medals Won", fontweight ='bold', fontsize = 15)

    plt.show()
    
    return [x_points, y_points]
