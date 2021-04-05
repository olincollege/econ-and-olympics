from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def graph_medals(table):
    # convert pandas object into lists
    medals_for_all = [table.columns.values.tolist()] + table.values.tolist();
    
    countries =[]
    medals =[]

    for row in medals_for_all[1:]:
        country = row[0]
        countries.append(country)
        medal = int(row[15])
        medals.append(medal)
    
    sorted_medals = sorted(medals, reverse = True)
    
    new_countries = []
    for medal in sorted_medals:
        for row in medals_for_all[1:]:
            if int(row[15]) == medal:
                new_countries.append(row[0])
                medals_for_all.remove(row)
                break
                
    plt.figure(figsize=(15, 9))
    plt.bar(new_countries[0:31], sorted_medals[0:31])
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
    
    plt.title("2019 GDP(PPP) vs. Medals")
    plt.xlabel("2019 GDP(PPP)(in billions)")
    plt.ylabel("Totals Medals Won")

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
    
    plt.title("2019 GDP(PPP) vs. Medals")
    plt.xlabel("2019 GDP(PPP)(in billions)")
    plt.ylabel("Totals Medals Won")

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

    plt.title("2019 GDP(PPP) vs. Medals")
    plt.xlabel("2019 GDP(PPP)(in billions)")
    plt.ylabel("Total Gold Medals Won")

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

    plt.title("2019 GDP(PPP) vs. Medals")
    plt.xlabel("2019 GDP(PPP)(in billions)")
    plt.ylabel("Total Gold Medals Won")

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
    
    plt.title("2019 GDP per Capita vs. Medals")
    plt.xlabel("2019 GDP per Capita(")
    plt.ylabel("Totals Medals Won")

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
    
    plt.title("2019 GDP per Capita vs. Medals")
    plt.xlabel("2019 GDP per Capita(")
    plt.ylabel("Totals Medals Won")

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

    plt.title("2019 IHDI vs. Medals")
    plt.xlabel("2019 IHDI")
    plt.ylabel("Totals Medals Won")

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

    plt.title("2019 IHDI vs. Medals")
    plt.xlabel("2019 IHDI")
    plt.ylabel("Totals Medals Won")

    plt.show()
    
    return [x_points, y_points]




