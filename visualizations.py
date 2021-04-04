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
    
    
def plot_GDPvMedals(table1, table2):
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

    

def plot_GDPvMedals_noOutliers(table1, table2):
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
    
