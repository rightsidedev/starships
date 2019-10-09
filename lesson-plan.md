# Ahoy!

The year is 2364.
New start-up Ahoy!™ has hired you as a back-end software engineer to build their new Starship review site. It's currently only an MVP, and all they need is a REST API.
The data model should have *Ships*, *Users*, and *Reviews* of Ships left by *Users*.

Design a REST API using Flask, which uses a JSON file as a database. 
The JSON should have the following structure.

### Entity Relation Diagram

![starship_data_model](/Users/james/Documents/Cyber/starship_lesson/starship_data_model.png)



You might have seen one of these before. It's an entity relation diagram (ERD). This will become far more important when we get into SQL later but for now there are only a few things you need to gleam from this. Every review has a 'ship' property which stores the id of a starship, and a 'user' property used to identify a user. There are other also properties on each of the three **Models**.

How might we decide to structure this as a flat file database? (In this case I am just referring to using a single json file to store all our data, rather than a more extensive SQL or NoSQL database).


We want to aim to have it as _flat_ as possible, meaning that the array of ships, the array of users, and the array of reviews should all as follows.

## The JSON Structure

```json
{
  ships: [
    {
      id: '1', // Flask will have to assign these
      name: "Enterprise", // Required field when creating
      age: 68, // Unrequired field
      avgRating: 4 // Determined and updated when reviews are created
    }
  ],
  users: [
    {
      id: '1', // Flask assigned
      username: 'WRiker22', // Required
      firstName: 'William', // Required
      LastName: 'Riker', // Required
      reviewsCount: 22 // Determined by flask
    }
  ]
  reviews: [
    {
      id: '1' // Assigned by flask
  		ship: '1', // Required foreign key
      user: '1', // Required foreign key
      title: 'Best time ever', // Required
      body: 'Been chilling with my home boy Jean Luc and it\'s been the best time o\' me life', // Required
      rating: 5 // Required
    }
  ]
}
```



In some places these values will have to be entered by the user when they are creating a new User, Ship, or Review. In others, this will either need to assigned when the User, Ship, or Review is created (id) OR when there is a change made to the data (E.g. the average).

It is up to you to write the functions to **C**reate, **R**ead, **U**pdate, and **D**elete these three Models. These you will then use to create the following endpoints:



## The API

### Starships
| Method | Route                    | Description                            | Params `application/json`           |
|--------|--------------------------|----------------------------------------|-------------------------------------|
| GET    | /starships/              | Return array of all starships          |                                     |
| GET    | /starships/{id}/         | Return starship of id `id`             |                                     |
| GET    | /starships/{id}/reviews/ | Return reviews of starship of id `id`  |                                     |
| POST   | /starships/              | Create starship                        | `{ "name": string, "age": number }` |
| PUT    | /starships/{id}/         | Update starship of id with new details | `{ "name": string, "age": number }` |
| DELETE | /starships/{id}/         | Delete starship of id                  |                                     |

### Users
| Method | Route                | Description                        | Params `application/json`                                         |
|--------|----------------------|------------------------------------|-------------------------------------------------------------------|
| GET    | /users/              | Return array of all users          |                                                                   |
| GET    | /users/{id}/         | Return user of id `id`             |                                                                   |
| GET    | /users/{id}/reviews/ | Return reviews by user of id `id`  |                                                                   |
| POST   | /users/              | Create user                        | `{ "username": string, "firstName": string, "lastName": string }` |
| PUT    | /users/{id}/         | Update user of id with new details | `{ "username": string, "firstName": string, "lastName": string }` |
| DELETE | /users/{id}/         | Delete user of id                  |                                                                   |

### Reviews
| Method | Route          | Description                          | Params `application/json`                                                               |
|--------|----------------|--------------------------------------|-----------------------------------------------------------------------------------------|
| GET    | /reviews/      | Return array of all reviews          |                                                                                         |
| GET    | /reviews/{id}/ | Return review of id `id`             |                                                                                         |
| POST   | /reviews/      | Create review                        | `{ "ship": string, "user": string, "title": string, "body": string, "rating": number }` |
| PUT    | /reviews/{id}/ | Update review of id with new details | `{ "ship": string, "user": string, "title": string, "body": string, "rating": number }` |
| DELETE | /reviews/{id}/ | Delete review of id                  |                                                                                         |





### JSON: Revisited

In case you need a reminder in using JSON in python, here is some of the common operations again.

```python
import json

with open('db.json', '+') as f:
  db = json.load(f) # Load json as dictionary

  # Retrieve the user of id '3' from your database.
  for user in db['users']:
    if user['id'] == '3':
      selectedUser = user

  # Make sure you handle if someone cant be found
  if selectedUser == None:
    print('Could not find user of ID 3')
    quit()

  print(f'Retrived user {selectedUser["name"]}, changing their name to "Tobias"')

  selectedUser['name'] =  "Tobias" # Write to the name property of user of id '3' in users 

  json.dump(db, f) # Writes back to the flat file again
```

### Flask API revisited


Status Codes: http://www.flaskapi.org/api-guide/status-codes/

### Beast mode

There are a few places in which our approach is sub-optimal, especially as our dataset increases in size. Make any changes you wish to the code, or the implementation of the database. The only part that needs to stay the same is the endpoints and how they behave (E.g. expecting the same params, and returning the same JSON objects)
