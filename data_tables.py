import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_medals_all():
    page = requests.get("https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table")
    soup = BeautifulSoup(page.content, 'html.parser')
    target_data = soup.find(id="mw-content-text")
    tables = target_data.find_all(class_ = "wikitable sortable")
    unranked_medals = tables[0]

    # the head will form our column names
    rows = unranked_medals.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head_row = rows[1]; # 0th item is the header row
    body_rows = rows[2:]; # All other items becomes the rest of the rows


    headings = ["Team (IOC code)", "SG Partcipated", "Gold", "Silver", "Bronze", "Total",
                "WG Partcipated", "Gold", "Silver", "Bronze", "Total",
               "Combined Total", "Gold", "Silver", "Bronze", "Total"]


    all_rows = []
    for row_num in range(len(body_rows)-1): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)

    bottom_row = body_rows[len(body_rows)-1].find_all("th")
    row = []
    for row_item in bottom_row: #loop through all row entries
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        row.append(aa)
    all_rows.append(row)


    df = pd.DataFrame(data=all_rows,columns=headings)
    return df

def get_medals_top10():
    page = requests.get("https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table")
    soup = BeautifulSoup(page.content, 'html.parser')
    target_data = soup.find(id="mw-content-text")
    tables = target_data.find_all(class_ = "wikitable")
    top10_medals = tables[7]

    # the head will form our column names
    rows = top10_medals.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head_row = rows[0]; # 0th item is the header row
    body_rows = rows[1:]; # All other items becomes the rest of the rows
    

    headings = ["Rank", "Nation", "Gold", "Silver", "Bronze", "Total"]


    all_rows = []
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        rank = body_rows[row_num].find("th")
        row.append(re.sub("(\xa0)|(\n)|,","",rank.text))
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)


    df = pd.DataFrame(data=all_rows,columns=headings)
    return df

def get_GDP_PPP():
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)")
    soup = BeautifulSoup(page.content, 'html.parser')
    target_data = soup.find(id="mw-content-text")
    tables = target_data.find_all(class_ = "wikitable sortable")
    ranked_GDP = tables[1]

    # the head will form our column names
    rows = ranked_GDP.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head_row = rows[0]; # 0th item is the header row
    body_rows = rows[1:]; # All other items becomes the rest of the rows


    headings = ["Rank", "Country/Territory", "GDP (in millions)"]


    all_rows = []
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)


    df = pd.DataFrame(data=all_rows,columns=headings)
    return df

def get_GDP_per_Capita():
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita")
    soup = BeautifulSoup(page.content, 'html.parser')
    target_data = soup.find(id="mw-content-text")
    tables = target_data.find_all(class_ = "wikitable sortable")
    ranked_GDP = tables[1]

    # the head will form our column names
    rows = ranked_GDP.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head_row = rows[0]; # 0th item is the header row
    body_rows = rows[1:]; # All other items becomes the rest of the rows


    headings = ["Rank", "Country/Territory", "Int$"]


    all_rows = []
    orig_rows = []
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)
        orig_rows.append(row)
    
    
    # remove unranked prvinces considered as dependents of outher countries
    for row in orig_rows:
        if row[0] == "—":
            all_rows.remove(row)

    df = pd.DataFrame(data=all_rows,columns=headings)
    return df


def get_IHDIs():
    page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_inequality-adjusted_HDI")
    soup = BeautifulSoup(page.content, 'html.parser')
    target_data = soup.find(id="mw-content-text")
    ranked_HDI = target_data.find(class_ = "wikitable sortable")

    # the head will form our column names
    rows = ranked_HDI.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head_rows = rows[0:2]; # 0th item is the header row
    body_rows = rows[3:]; # All other items becomes the rest of the rows


    headings = ["Rank", "Country", "IHDI", "HDI", "Overall loss (%)", "Growth since 2010"]


    all_rows = []
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(aa)
        all_rows.append(row)
    
    # remove header rows inside the table that do not correspond to countries, but categories
    for row in all_rows:
        if len(row) == 0:
            all_rows.remove(row)
            


    df = pd.DataFrame(data=all_rows,columns=headings)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    return df