# Auteur: Jorik de Graaf
# port 3306
# x protocol port 33060

import zeep
import mysql.connector
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)

# WSDL URL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Start Zeep client
client = zeep.Client(wsdl=wsdl_url)

# Lijst met landen
countries = client.service.ListOfCountryNamesByCode()

# Vervang '&' met 'and' + 'And' met 'and' voor consistentie (behave Andorra)
for row in countries:
    if row.sName == 'Andorra':
        continue
    else:
        row.sName = row.sName.replace('&','and').replace('And','and')
        # print(row.sName, row.sISOCode)

# Connect
cursor = conn.cursor()

# Insert statement
sql = """
    INSERT INTO countries (iso_code, name)
    VALUES (%s, %s)"""

# Loop over alle rows
for c in countries:
    cursor.execute(sql, (c.sISOCode, c.sName))

# Commit en sluit connection
conn.commit()
cursor.close()
conn.close()

# Finish
print("Inserted all rows.")