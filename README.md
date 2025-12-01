Auteur: Jorik de Graaf

Datum: 01-12-2025

Betreft: Python coding assignment voor de NZA

## Opdracht
Deze opdracht bestaat uit het ophalen van data van een publiek beschikbare SOAP service. In een aantal 
landen namen staat “&”, vervang dit door “and”. Sla de data vervolgens op in een lokale database (MySQL 
of Postgresql). Tenslotte toon de eerste 10 landen met hun bijbehorende landencodes (alfabetisch gesorteerd)

## Stappen: 
1. Maak een tabel in je lokale database (MySQL of Postgresql) voor deze informatie, bij voorkeur in je python script
2. Haal de data op van de SOAP service en sla deze data op in de database
3. Voer een query uit om de eerste tien landen met bijbehorende ISO code te tonen
4. Gebruik Docker om te database te runnen

## Docker code snippet:
docker run -d -p 3306:3306 \
 --name mysql-docker-container \
 -e MYSQL_ROOT_PASSWORD=w8woord \
 -e MYSQL_DATABASE=codetest \
 -e MYSQL_USER=gebruikersnaam \
 -e MYSQL_PASSWORD=w8woord \
 mysql/mysql-server:latest


# Processtappen 

## Docker:
## Hier maak je een Docker container aan om een MySQL database in te runnen. Daar maak je een tabel aan om de data in te laden. 

 1. Run bovenstaande Docker code snippet voor aanmaken container
 2. Connect naar container:
     docker exec -it mysql-docker-container mysql -u gebruikersnaam -p
 3. Maak tabel aan
     CREATE TABLE countries (name VARCHAR(200), iso_code VARCHAR(10));

## Python:
## Dit Python script connect naar de SOAP, haalt de data op, doet een cleanse en schrijft de data weg in de MySQL database in de Docker container
NB Het Python script maakt gebruik van een .env file waarin de credentials staan. De .env zit in .gitignore dus is niet zichtbaar in Git. Niet echt nodig want ze staan ook hierboven, maar is toch goede practice :)

1. Run main.py

## SQL
## De eerste tien landen toon je middels een SQL query.

1. Open de Docker container:
    docker exec -it mysql-docker-container mysql -u gebruikersnaam -p
2. gebruik de juiste database:
    use codetest;
3. Voer de SQL query uit:
   select * from countries limit 10;
