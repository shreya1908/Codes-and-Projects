import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect   #the connected program in the db is attached below

parser= argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter no. of pages to parse:", type=int)
parser.add_argument("--dbname", help="Enter the name of db", type=str)
args= parser.parse_args()

oyo_url= "https://www.oyorooms.com/hotels-in-bangalore/?page=" # the URL for the site
page_num_MAX= args.page_num_max
scraped_info_list= []
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
  url= oyo_url+str(psge_num)
  print("Get request for:"+url)
  req= requests.get(url)
  content= req.content
  soup= BeautifulSoup(content, "html.parser")
  all_hotels= soup.find_all("div",{"class": "hotelCardListing:})
  
  for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"]= hotel.find("h3", {"class": "listingHotelDescription_hotelName"}).text
    hotel_dict["address"]= hotel.find("span", {"itemprop": "streetAddress"}).text
    hotel_dict["price"]= hotel.find("span", {"class": "listingPrice__finalPrice"}).text
 #try-except block to remove the error
    try:
      hotel_dict["rating"]= hotel.find("span",{"class": "hotelRating__ratingSummary"}).text
    except AttributeError:
      pass
                                   
    parent_amenities_element= hotel.find("div, {"class": "amenityWrapper"})
    amenities_list= []
    for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
      amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
                                         
    hotel_dict["amenities"]= ", ".join(amenities_list[:-1])
    scraped_info_list.append(hotel_dict)
                                         
dataFrame= pandas.DataFrame(scrapped_info_list)
print("Creating CSV file, processing.....")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)
                                         
                                         
                                         
                                         
#program for the database connecting part
import sqlite3
    
def connect(dbname):
  conn= sqlite3.connect(dbname)
  conn.execute("Create Table if not exists OYO_HOTELS (Name Text, Address Text, Price Int, Amenities Text, Rating Text)")
  print("Table created successfully")
  conn.close()    
                                         
def insert_into_table(dbname,values):
  conn= sqlite3.connect(dbname)
  insert_sql= "Insert into OYO_HOTELS (Name, Address, Price, Amenities, Rating) Values (?, ?, ?, ?, ?)"
  conn.execute(insert_sql,values)
  conn.commit()
  conn.close()
                                         
def get_hotel_info(dbname):
  conn= sqlite3.connect(dbname)
  cur= conn.cursor()
  cur.execute("Select * from OYO_HOTELS")
  table_data= cur.fetchall()
  for record in table_data:
    print(record)
                                         
  conn.close()                                
