Online Bookstore - Testing Implementation

Project Overview
This project contains the testing implementation for an Online Bookstore Website, including comprehensive unit tests for book management, shopping cart functionality, and search operations.

Features Tested
Book Management : (FR-001): Search, categorization, and inventory management
Shopping Cart:  (FR-002): Add, remove, update quantities, and price calculations
Search Functionality: Title, author, and category-based search














 Project Structure
online-bookstore-flask/
├── models/           
│                ├── __init__.py
│                 ├── book.py       # Book and BookManager classes
│                 └── cart.py        # ShoppingCart and CartItem classes
├── tests/           
│               ├──__init__.py
│              ├── test_books.py   # Book management tests (14 tests)
│              ├── test_cart.py       # Shopping cart tests (18 tests)
│               └── test_search.py  # Search functionality tests (12 tests)
├── .gitignore
├── README.md
├── app.py
└── requirements.txt






Installation & Setup
1. Clone or extract the project
   ```bash
   unzip your-project.zip
   cd online-bookstore-flask
2.Create virtual environment:
     python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
     pip install -r requirements.txt
Running Tests
Option 1: Using unittest
# Run all tests
 python -m unittest discover tests/

# Run specific test file
python -m unittest tests.test_books

# Verbose output
python -m unittest discover tests/ -v
Option 2: Using pytest
# Run all tests
pytest tests/

# Run with coverage report
pytest tests/ --cov=. --cov-report=html

# Generate HTML test report
pytest tests/ --html=report.html
Test Coverage
•	Total Tests: 44 comprehensive test cases
•	Coverage Areas: Unit testing, integration scenarios, edge cases
•	Requirements Covered: FR-001, FR-002 (100% core functionality)
Dependencies
•	Python 3.8+
•	Flask 2.3.3
•	pytest 7.4.2
•	coverage 7.2.7
Test Results
Expected output: All 44 tests should pass with 100% success rate.
________________________________________
Student: Rezene Ghebrehiwot
Student ID: 2415644
Course: Software Testing 
