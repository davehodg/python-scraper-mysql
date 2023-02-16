#!/usr/local/bin/python

# create a list, then iterate it with a get in the loop
# mysql:
#   username: root
#   password: Rn045^bP

# essential modules
import requests
import mysql.connector

#utility modules
import json
from pprint import pprint

response = requests.get("https://world.openfoodfacts.org/api/v0/product/737628064502.json")


if response.status_code == 200:
    print(response.status_code)
    data = pprint(response.json())
    print (type(data))



def connect():
        dbh = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "your_password"
)