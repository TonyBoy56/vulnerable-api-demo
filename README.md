# Vulnerable API Demo

This project is a deliberately vulnerable API built with Flask. The purpose of this project is to practice identifying, exploiting, and fixing common security vulnerabilities in web applications. It’s an educational resource for developers and cybersecurity enthusiasts to learn secure coding practices.

---

## Features

- A simple API with endpoints for user registration and login.
- **Deliberate Vulnerabilities**: Includes common flaws such as:
  - Insecure password storage (plaintext passwords).
  - Lack of input validation.
  - Vulnerable authentication mechanisms.
- Example security fixes to demonstrate remediation techniques.

---

## Project Structure

```plaintext
vulnerable-flask-api/
├── README.md                # Overview of the project
├── LICENSE                  # License file (e.g., MIT)
├── requirements.txt         # Python dependencies
├── app/
│   ├── __init__.py          # Initializes Flask app
│   ├── routes.py            # API endpoints with vulnerabilities
│   ├── models.py            # Data models (if using a database)
│   ├── utils.py             # Helper functions (e.g., input validation)
│   ├── static/              # Static assets (optional)
│   └── templates/           # HTML templates (if any)
├── tests/
│   ├── __init__.py          # Initialize test package
│   ├── test_routes.py       # Tests for API endpoints
│   └── test_security.py     # Tests for security features (e.g., hashed passwords)
├── .gitignore               # Ignore unnecessary files
└── run.py                   # Entry point to run the app
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TonyBoy56/vulnerable-api-demo
   cd vulnerable-api-demo
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Access the API at `http://127.0.0.1:5000`.

---

## Vulnerabilities to Practice

1. **Insecure Password Storage**
   - Passwords are stored in plaintext.
   - Fix: Use bcrypt to hash passwords before storing them.

2. **Lack of Input Validation**
   - API does not validate user input, making it prone to SQL injection or XSS attacks.
   - Fix: Implement input validation with Python libraries like `validators` or use an ORM.

3. **Weak Authentication**
   - No token-based authentication.
   - Fix: Implement JWT (JSON Web Tokens) for secure authentication.

4. **Bad .gitignore**
    - Directories and files that are included in the .gitignore but are commented out, and are part of the commit history of the project.

---

## Goals and Learning Outcomes

- Understand common vulnerabilities in web applications.
- Learn how to exploit these vulnerabilities ethically in a safe environment.
- Practice fixing vulnerabilities and improving API security.
- Build a project that demonstrates secure coding skills.

---

## Contributing

If you’d like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions such as additional vulnerabilities, fixes, or documentation improvements are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Disclaimer

This project is for educational purposes only. Do not use the techniques or vulnerabilities demonstrated in this project for malicious purposes.

