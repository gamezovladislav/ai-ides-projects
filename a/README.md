# Flask User API

A simple Flask application that manages user data.

## Requirements

- Python 3.8+
- pip package manager

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app
   ```
2. The application will be available at `http://localhost:5000`

## API Endpoints

- GET `/users/<id>` - Retrieve user by ID
```http request
  GET http://localhost:5000/users/42
```

## Testing

Run tests using pytest:
```bash
  python -m pytest tests/test_user_endpoint.py
```


# ISSUE
```text
AttributeError: 'NoneType' object has no attribute 'to_dict' while fetch user by Id
```
