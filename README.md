# Professional ATM Management System

An interview-ready, object-oriented Python application simulating a robust ATM system.

## 🌟 Features
- **Object-Oriented Design**: Clean separation of concerns using Models, Services, UI, and Storage layers.
- **Security**: User PINs are securely hashed using SHA-256 before storage.
- **Data Persistence**: Uses a Repository pattern over JSON file storage to persist transactions securely across sessions.
- **Error Handling**: Custom robust exception handling for invalid banking operations (e.g., insufficient funds).
- **Unit Testing**: Includes an automated test suite utilizing `pytest` to ensure core banking logic remains reliable.
- **Dependency Injection**: Promotes loose coupling, making the system highly testable and extensible.

## 🏗 Project Architecture
```text
ATM-Management-System/
├── atm/
│   ├── __init__.py     # Package initialization
│   ├── cli.py          # Command Line Interface presentation layer
│   ├── models.py       # Data models (Account, Transaction)
│   ├── services.py     # Business logic layer (authentication, banking math)
│   └── storage.py      # Data persistence layer
├── tests/
│   └── test_services.py# Unit tests for the business logic
├── data/               # Persistent data storage (users.json generated here)
├── run.py              # Application entry point
└── requirements.txt    # Project dependencies
```

## 🚀 Setup & Execution

### Prerequisites
- Python 3.8+

### Installation
1. Clone the repository and navigate into the project directory.
2. It's recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
Start the ATM command-line application:
```bash
python run.py
```

### Running Tests
Execute the unit tests to verify the business logic:
```bash
pytest tests/
```
