# 💰 Finance Tracker API

A REST API built using FastAPI to manage income and expenses.

## Features
- Create transactions
- Get all transactions
- Delete transactions
- Get summary (income, expense, balance)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## How to Run

1. Create virtual environment
python -m venv venv

2. Activate environment
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run server
uvicorn main:app --reload

5. Open browser
http://127.0.0.1:8000/docs

## API Endpoints

GET /transactions  
POST /transactions  
DELETE /transactions/{id}  
GET /summary  

## Example Request

{
  "amount": 500,
  "type": "expense",
  "category": "food",
  "date": "2026-04-02",
  "note": "lunch"
}

## Author
Bhuvaneshwar Reddy