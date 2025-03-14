# Cereal API

The project contains two main functionalities. 
One being the parsing of a csv into a sqlite database.
The other being the hosting of an API for Cereals

## Description
### csv_parser.py
This file is used to add Cereal entries from the Cereal.csv file into a database.
It goes through the Cereal.csv file and adds each entry to the database.

### Cereal API
The cereal api allows you to.
* Fetch a list of cereals from the database. Which allows for filtering.
* Post new cereals to the database
* Edit existing cereal information.
* Delete cereals from the database.
* Login - Which is required to get the very "secret" token needed to post, edit and delete.
* Fetch images from the database.

## Getting Started

### Dependencies
To run the Cereal API you need:
* Flask - ```pip install flask```
* Flasgger - ```pip install flasgger```

### Executing Program

To run the CSV Parser you run ```python csv_parser.py```

To run the Cereal API you run ```python cereal_api.py```

## Help

To get an overview of the API endpoints available and how to use them you can head run the cereal_api.py and go to:
* `localhost:5000/apidocs`