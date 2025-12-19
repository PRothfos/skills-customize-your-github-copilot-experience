"""
FastAPI Book Library Starter Code
Complete the TODOs to create a functional REST API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Book Library API")

# TODO: Define a Pydantic model for Book with fields: id, title, author, year
class Book(BaseModel):
    pass


# In-memory database (list of books)
books_db: List[Book] = []


# TODO: Create a GET endpoint at "/" that returns a welcome message


# TODO: Create a GET endpoint at "/books" that returns all books


# TODO: Create a GET endpoint at "/books/{book_id}" that returns a single book
# Hint: Raise HTTPException with status_code=404 if book not found


# TODO: Create a POST endpoint at "/books" that adds a new book
# Hint: Generate a new ID based on the current length of books_db


# TODO: Create a PUT endpoint at "/books/{book_id}" that updates an existing book


# TODO: Create a DELETE endpoint at "/books/{book_id}" that removes a book


# Run with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
