
# FastAPI Todo Application

A simple Todo application built with FastAPI, showcasing user authentication and CRUD operations for managing todo items. This project demonstrates the use of FastAPI for creating a RESTful API with an SQLite database.

## Project Structure

```
.
├── main.py
├── models.py
├── database.py
├── routers
│   ├── auth.py
│   └── todos.py
└── README.md
```

### Key Components

- **`main.py`**: The main entry point of the application. It initializes the FastAPI app, sets up the database, and includes routers for authentication and todos.

- **`models.py`**: Contains SQLAlchemy models for the database tables `Users` and `Todos`.

- **`database.py`**: Configures the SQLite database connection and provides a session maker for database operations.

- **`routers/auth.py`**: Implements user authentication, including creating users, logging in, and generating JWT tokens.

- **`routers/todos.py`**: Handles CRUD operations for todo items, allowing authenticated users to create, read, update, and delete their todos.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **Passlib**: A password hashing library for Python, used to securely store user passwords.
- **PyJWT**: A Python library that allows encoding and decoding of JSON Web Tokens (JWT).

## Features

- **User Authentication**: Register new users and login using JWT tokens for secure access to protected endpoints.
- **Todo Management**: Create, read, update, and delete todo items. Each todo is associated with a specific user, ensuring data privacy and integrity.
- **Data Validation**: Uses Pydantic for validating request data, ensuring robustness and preventing errors from invalid input.
- **Dependency Injection**: Utilizes FastAPI's dependency injection system for managing database sessions and user authentication.

## Future Enhancements

- **Frontend Integration**: Add a frontend interface using React or another JavaScript framework for a complete web application experience.
- **Testing**: Implement unit and integration tests to ensure the reliability and correctness of the application.
- **Advanced Authentication**: Add features such as password reset, email verification, and OAuth integration for social logins.

## Contributing

Contributions to the project are welcome! If you find a bug or want to add a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
