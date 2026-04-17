Modular RESTful API using Flask
Aim

To design and implement a modular RESTful API using Flask that performs full CRUD (Create, Read, Update, Delete) operations.

Technologies Used

Python

Flask

Postman (API Testing)

Render (Deployment)

Features

Create a student (POST)

Get all students (GET)

Get student by ID (GET)

Update student (PUT)

Delete student (DELETE)

Blueprint-based modular structure

JSON request and response handling

Proper HTTP status codes

In-memory data storage

Core Concepts

Flask Framework for building APIs

REST Architecture using GET, POST, PUT, DELETE

Blueprints for modular route organization

JSON Handling using request.get_json() and jsonify()

HTTP Status Codes (200, 201, 400, 404)

In-memory storage using Python list and current_id

API Endpoints

POST /students → Create student

GET /students → Get all students

GET /students/<id> → Get student by ID

PUT /students/<id> → Update student

DELETE /students/<id> → Delete student

Learning Outcomes

Implemented RESTful API using Flask

Handled JSON request and response

Used URL parameters (<int:student_id>)

Implemented input validation and error handling

Organized routes using Flask Blueprints

by: Jasmeen
Uid: 23BDA70075