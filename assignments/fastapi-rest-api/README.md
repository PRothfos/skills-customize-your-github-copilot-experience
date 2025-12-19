# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a simple book library API that handles CRUD operations (Create, Read, Update, Delete) and understand the fundamentals of web service development.

## 📝 Tasks

### 🛠️	Create Basic API Structure

#### Description
Set up a FastAPI application with basic endpoints to manage a collection of books. Each book should have an ID, title, author, and publication year.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create an in-memory list to store books
- Implement a GET endpoint to retrieve all books
- Implement a GET endpoint to retrieve a single book by ID
- Use appropriate HTTP status codes


### 🛠️	Implement CRUD Operations

#### Description
Extend your API with full Create, Update, and Delete functionality for managing books in the library.

#### Requirements
Completed program should:

- Implement a POST endpoint to add new books
- Implement a PUT endpoint to update existing books
- Implement a DELETE endpoint to remove books
- Validate input data using Pydantic models
- Return appropriate error messages for invalid operations
- Test all endpoints using the automatic interactive documentation
