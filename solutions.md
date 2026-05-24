# Flask API Solutions - All 10 Problems

## Problem 1: Basic Flask Welcome Website
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to My Flask Website!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 2: Random Motivational Quote Website
**Issues Fixed:**
- Changed `import flask from flask` to `from flask import Flask`
- Changed `app = flask(__name__)` to `app = Flask(__name__)`

```python
from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there."
]

@app.route('/')
def get_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 3: Reverse Word API
**Issues Fixed:**
- Changed `from flask import Flask, requests, jsonify` (removed incorrect `requests`)
- Fixed indentation - route decorator and function must be at the same level
- Moved the `if __name__` block outside of the route function

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Reverse Word API! Use the /reverse/<word> endpoint to reverse a word.'

@app.route('/reverse/<word>')
def reverse(word):
    reversed_word = word[::-1]
    return jsonify({'original': word, 'reversed': reversed_word})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 4: Create Employee Database
```python
from flask import Flask
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return 'Employee Database ready!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 5: Insert Employee Records
**Issues Fixed:**
- Changed `from flask import flask` to `from flask import Flask`
- This script should be run separately before starting the Flask app

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

def insert_employee(name, department, salary):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, department, salary)
        VALUES (?, ?, ?)
    ''', (name, department, salary))
    conn.commit()
    conn.close()

# Check if employees already exist before inserting
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM employees')
count = cursor.fetchone()[0]
conn.close()

if count == 0:
    insert_employee('John Doe', 'HR', 50000)
    insert_employee('Jane Smith', 'IT', 60000)
    insert_employee('Bob Johnson', 'Finance', 55000)
    insert_employee('Alice Brown', 'Marketing', 52000)
    insert_employee('Eve Davis', 'Sales', 58000)
    print('Employee records inserted successfully!')
else:
    print('Employee records already exist!')
```

## Problem 6: GET API – Fetch All Employee Records
```python
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_all_employees():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    
    employee_list = []
    for emp in employees:
        employee_list.append({
            'id': emp[0],
            'name': emp[1],
            'department': emp[2],
            'salary': emp[3]
        })
    return employee_list

@app.route('/')
def home():
    return 'Welcome to the Employee API! Use /employees to get all employees.'

@app.route('/employees')
def employees():
    return jsonify(get_all_employees())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 7: GET API – Fetch Employee by ID
**Issues Fixed:**
- Fixed indentation of route decorator
- Fixed `return jsonify` syntax error (was incomplete)
- Moved `if __name__` block outside function

```python
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_employee_by_id(employee_id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM employees WHERE id = ?
    ''', (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    
    if employee:
        employee_data = {
            'id': employee[0],
            'name': employee[1],
            'department': employee[2],
            'salary': employee[3]
        }
        return jsonify(employee_data)
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/')
def home():
    return 'Welcome to the Employee API! Use /employees/<id> to get employee details.'

@app.route('/employees/<int:employee_id>')
def employee(employee_id):
    return get_employee_by_id(employee_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 8: Current Date and Time API
**Issues Fixed:**
- Removed duplicate route definitions
- Fixed missing `jsonify` import
- Removed unreachable code (return statement before datetime logic)

```python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Current Date and Time API! Use the /time endpoint to get the current date and time.'

@app.route('/time')
def get_current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time': current_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 9: Calculator API
**Issues Fixed:**
- Fixed indentation of route decorator (was inside home function)
- Moved `if __name__` block outside function

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Calculator API! Use the /calculate/<num1>/<num2> endpoint to perform arithmetic operations.'

@app.route('/calculate/<int:num1>/<int:num2>')
def calculate(num1, num2):
    if num2 == 0:
        return jsonify({'error': 'Cannot divide by zero'})
    
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    
    return jsonify({
        'sum': sum_result,
        'difference': difference,
        'product': product,
        'quotient': quotient
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Problem 10: Random Movie Suggestion API
**Issues Fixed:**
- Fixed indentation of route decorator (was inside home function)
- Moved `if __name__` block outside function

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

movies = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    'Pulp Fiction',
    'The Lord of the Rings: The Return of the King'
]

@app.route('/')
def home():
    return 'Welcome to the Movie Suggestion API! Use the /movie endpoint to get a random movie suggestion.'

@app.route('/movie')
def get_random_movie():
    random_movie = random.choice(movies)
    return jsonify({'movie': random_movie})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## Summary of Common Issues Fixed

1. **Import Errors**: `import flask from flask` → `from flask import Flask`
2. **Indentation Issues**: Route decorators were nested inside other functions
3. **Unreachable Code**: Early return statements prevented actual logic execution
4. **Missing Imports**: `jsonify` not imported when needed
5. **Syntax Errors**: Incomplete statements like `return jsonify` without arguments
6. **Variable Naming**: Used `sum` (Python built-in) as variable name → changed to `sum_result`
7. **Missing Route Decorators**: Some functions were missing `@app.route()` decorators
8. **Duplicate Routes**: Problem 8 had duplicate `/time` routes
