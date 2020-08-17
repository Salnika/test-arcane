# Technical Test in python for Arcane

The goal of this test is to make a simple api that allow user to browse, publish and modify goods.

### Prerequisites

- python3
- pipenv `pip install pipenv`

### Setup

- start the environment with `pipenv shell`
- install all packages with `pipenv install`
- generate the database and seed it with `python3 generate_db_and_seed.py`

Then you will be apple to run the project with `pyton3 app`, you should be able to access the diferents endpoints on `http://localhost:5000`

### Endpoints

#### Authentication

```
- /auth:
  POST:
  description: return a JWT token
  parameters: username, password
  example:
  {
    "password": "s3cr3t",
    "username": "alex"
}
```

####Users:

```
- /user:
  POST:
  description: create a new user
  parameters: username, firstname, lastname, birthdate, password
  example:
  {
  "firstname": "Alexis",
  "lastname": "Martin",
  "birthdate": "11/02/1999",
  "password": "poulet",
  "username": "alor"
}

  PUT:
  description: update the current user
  authentication: required
  parameters: username, firstname, lastname, birthdate, password
  example:
  {
  "firstname": "Alexis",
  "lastname": "Martin",
  "birthdate": "11/02/1999",
  "password": "poulet",
  "username": "alop"
}

  DELETE:
  description: delete the current user
  authentication: required

- /user/<id>
  GET:
  description: get user information

```

#### Goods

```
- /goods
  POST:
  description create a good
  authentication: required
  parameters: name, description, good_type, city, room_nb, owner_name
  example:
  {
    "name": "super maison a la plage",
    "description": "en bord de plage",
    "good_type": "house",
    "room_nb": 3,
    "owner_name": "Alexis Martin",
    "city": "Paris"
}

  GET:
  description: return all the goods of the current user
  authentication: required

- /goods/<id>
  PUT:
  description update a good
  authentication: required
  parameters: name, description, good_type, city, room_nb, owner_name
  example:
  {
    "name": "super immeuble a la plage",
    "description": "en bord de super plage plage",
    "good_type": "studio",
    "room_nb": 1,
    "owner_name": "Alexis Martin",
    "city": "Deauville"
}

  DELETE:
  description: delete a good
  authentication: required

- /good/search/<city>
  GET:
  description: return the list of good in this city
```
