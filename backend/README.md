# Backend
## RESTful API

This Application Programming Interface was built with Flask and SQLAlchemy in order to work with MySQL and respond to HTTP requests.

The endpoints can be seen below.

```
GET /api/v1/status
**Returns the status of the API

GET /api/v1/stats
**Retrieves the number of each objects by type
GET /api/v1/categories
**Retrieves the list of all Category objects

GET /api/v1/categories/<category_id>
**Retrieves a Category object
DELETE /api/v1/categories/<category_id>
**Deletes a Category object
POST /api/v1/categories
**Creates a Category
PUT /api/v1/categories/<category_id>
**Updates a Category object

GET /api/v1/expenses
**Retrieves the list of all Expense objects
GET /api/v1/expenses/<category_id>
**Retrieves a Expense object
DELETE /api/v1/expenses/<category_id>
**Deletes a Expense object
POST /api/v1/expenses
**Creates a Expense
PUT /api/v1/expenses/<category_id>
**Updates a Expense object

POST /api/v1/register
**Creates a User

POST /api/v1/login
**Logs in a User

POST /api/v1/logout
**Logs out a User

GET /apidocs
**Gets the documentation of the API built in Flasgger
```

## Authors
Clifford Mapesa - [Github](https://github.com/droffilc1) / [Twitter](https://twitter.com/droffilcasepam1)
