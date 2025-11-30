# Auteur: Jorik de Graaf

import zeep

# WSDL URL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Start Zeep client
client = zeep.Client(wsdl=wsdl_url)

# Lijst met landen
countries = client.service.ListOfCountryNamesByCode()

# Vervang '&' met 'and' en 'And' met 'and' voor consistentie 
for row in countries:
    row.sName = row.sName.replace('&','and').replace('And','and')
    print(row.sName, row.sISOCode)