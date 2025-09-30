# app.py - Minimal Flask Application for Testing Demonstration
from flask import Flask, render_template, jsonify, request, session
import os

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Needed for session management

# Import your models
try:
    from models.book import Book, BookManager
    from models.cart import ShoppingCart
except ImportError:
    # Fallback for testing environment
    print("Note: Running in test mode without full model imports")

@app.route('/')
def home():
    """Home page - book catalog"""
    return "Online Bookstore - Home Page (Book catalog functionality to be implemented)"

@app.route('/books')
def list_books():
    """API endpoint to list all books (for testing)"""
    # This would normally connect to your BookManager
    sample_books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 12.99},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 14.99}
    ]
    return jsonify(sample_books)

@app.route('/cart')
def view_cart():
    """Shopping cart page"""
    return "Shopping Cart - Add, remove, and manage your books"

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    """API endpoint to add book to cart"""
    # Cart functionality would be implemented here
    return jsonify({"status": "success", "message": "Item added to cart"})

@app.route('/search')
def search_books():
    """Search functionality endpoint"""
    query = request.args.get('q', '')
    # Search logic would be implemented here
    return jsonify({"query": query, "results": []})

# Basic health check endpoint for testing
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Online Bookstore API is running"})

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)