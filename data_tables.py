import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_medals_all():
    """
    Using Beautfiul Soup, scrapes a table holding data of
    the All-Time record and distribution of Olympic Medals
    won by Olympic Committees and puts that data into a
    Pandas Dataframe and then saves it to a .csv file.

    Args:
        This function has no arguments.

    Returns:
        This function returns nothing.
    """
    # download the wikipedia page using the requests.get method
    page = requests.get("https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table")
    # create an instance of the BeautifulSoup class to parse the page
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the desired code by searchin for the div tag with unique id wanted
    target_data = soup.find(id="mw-content-text")
    # we find all the tables inside that tag
    tables = target_data.find_all(class_ = "wikitable sortable")
    # we know that table we want is the first one, so index = 0
    unranked_medals = tables[0]

    # <tr> represents table rows, so we grab all the rows
    rows = unranked_medals.find_all("tr")
    body_rows = rows[2:] # All other items become the rest of the rows

    # create a list of the column names
    headings = ["Team (IOC code)", "SG Partcipated", "Gold", "Silver", "Bronze", "Total",
                "WG Partcipated", "Gold", "Silver", "Bronze", "Total",
               "Combined Total", "Gold", "Silver", "Bronze", "Total"]


    #populate all_rows with the actual data within each
    #line of html code that represents the body rows of the table
    all_rows = []
    for row_num in range(len(body_rows)-1):
        row = [] #a list that represents all the data within one row
        for row_item in body_rows[row_num].find_all("td"): # loop through all cells in the row
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text) # get the string (actual number) in that cell
            row.append(aa) # add the cell data to the row list
            all_rows.append(row)# add the row list to the all_rows list
    #remove the bracketed letters that pop up next to country names
    for row in all_rows:
        country = row[0]
        index = country.index(")")
        row[0] = country[0:index+1]
    print(all_rows)
    
    #the bottom row is a table heading type (th) instead of a table
    #data type (td) so it must be added seperately
    bottom_row = body_rows[len(body_rows)-1].find_all("th")
    row = []
    for row_item in bottom_row: # loop through all row entries
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        row.append(aa)
    all_rows.append(row) # add the row data to all_rows

    # create a Pandas Dataframe with all_rows as the body and
    # heading list as the column names
    df = pd.DataFrame(data=all_rows,columns=headings)
    # write the Dataframe to a .csv file
    df.to_csv('all_medals.csv', index = False)

def get_GDP_PPP():
    """
    Using Beautfiul Soup, scrapes a table holding data of
    the 2019 Gross Domestic Product at Purchasing
    Power Parity of all the countries in the world and puts
    that data into a Pandas Dataframe and then saves it to 
    a .csv file.
    
    Args:
        This function has no arguments.

    Returns:
        This function returns nothing.
    """
    # download the wikipedia page using the requests.get method
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)")
    # create an instance of the BeautifulSoup class to parse the page
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the desired code by searchin for the div tag with unique id wanted
    target_data = soup.find(id="mw-content-text")
    # we find all the tables inside that tag
    tables = target_data.find_all(class_ = "wikitable sortable")
    # we know that table we want is the second one, so index = 1
    ranked_GDP = tables[1]

    #<tr> represents table rows, so we grab all the rows
    rows = ranked_GDP.find_all("tr")
    body_rows = rows[1:] #All other items become the rest of the rows

    # create a list of the column names
    headings = ["Rank", "Country/Territory", "GDP (in millions)"]

    # populate all_rows with the actual data within each
    # line of html code that represents the body rows of the table
    all_rows = []
    for row_num in range(len(body_rows)):
        row = []
        for row_item in body_rows[row_num].find_all("td"):#loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row) # add the row data to all_rows


    # create a Pandas Dataframe with all_rows as the body and
    # heading list as the column names
    df = pd.DataFrame(data=all_rows,columns=headings)
    # write the Dataframe to a .csv file
    df.to_csv('GDP_PPP.csv', index = False)


def get_GDP_per_Capita():
    """
    Using Beautfiul Soup, scrapes a table holding data of
    the 2019 Gross Domestic Product at Purchasing
    Power Parity per Capita of all the countries in the world
    and puts that data into a Pandas Dataframe and then saves
    it to a .csv file.

    Args:
        This function has no arguments.

    Returns:
        This function returns nothing.
    """
    # download the wikipedia page using the requests.get method
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita")
    # create an instance of the BeautifulSoup class to parse the page
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the desired code by searchin for the div tag with unique id wanted
    target_data = soup.find(id="mw-content-text")
    # we find all the tables inside that tag
    tables = target_data.find_all(class_ = "wikitable sortable")
    # we know that table we want is the second one, so index = 1
    ranked_GDP = tables[1]

    # <tr> represents table rows, so we grab all the rows
    rows = ranked_GDP.find_all("tr")
    body_rows = rows[1:]; # All other items becomes the rest of the rows

    # create a list of the column names
    headings = ["Rank", "Country/Territory", "Int$"]

    # populate all_rows with the actual data within each
    # line of html code that represents the body rows of the table
    all_rows = []
    # orig_rows is a placeholder list that will hold the unaltered data
    # of all_rows for later
    orig_rows = []
    for row_num in range(len(body_rows)):
        row = [] 
        for row_item in body_rows[row_num].find_all("td"):#loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row) # add the row data to all_rows
        orig_rows.append(row) # add the row data to orig_rows
        
    # remove unranked provinces considered as dependents of other countries
    for row in orig_rows:
        if row[0] == "—":
            all_rows.remove(row)

    # create a Pandas Dataframe with all_rows as the body and
    # heading list as the column names
    df = pd.DataFrame(data=all_rows,columns=headings)
    # write the Dataframe to a .csv file
    df.to_csv('GDP_PPP_per_Capita.csv', index = False)

def get_IHDIs():
    """
    Using Beautfiul Soup, scrapes a table holding data of
    the 2019 Inequality-adjusted Human Development Index of
    all the countries in the world and puts that data into
    a Pandas Dataframe and then saves it to a .csv file.

    Args:
        This function has no arguments.

    Returns:
        This function returns nothing.
    """
    # download the wikipedia page using the requests.get method
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_inequality-adjusted_HDI")
    # create an instance of the BeautifulSoup class to parse the page
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the desired code by searchin for the div tag with unique id wanted
    target_data = soup.find(id="mw-content-text")
    ranked_HDI = target_data.find(class_ = "wikitable sortable")

    # <tr> represents table rows, so we grab all the rows
    rows = ranked_HDI.find_all("tr")
    body_rows = rows[3:]; # All other items becomes the rest of the rows
    
    #create a list of the column names
    headings = ["Rank", "Country", "IHDI", "HDI", "Overall loss (%)", "Growth since 2010"]
    
    # populate all_rows with the actual data within each
    # line of html code that represents the body rows of the table
    all_rows = []
    for row_num in range(len(body_rows)): 
        row = [] 
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row) # add the row data to all_rows
    
            
    # remove header rows inside the table that do not correspond to countries, but categories
    for row in all_rows:
        if len(row) == 0:
            all_rows.remove(row)
            
    # create a Pandas Dataframe with all_rows as the body and
    # heading list as the column names
    df = pd.DataFrame(data=all_rows,columns=headings)
    # write the Dataframe to a .csv file
    df.to_csv('IHDIs.csv', index = False)

    