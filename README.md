# Grafonix

Grafonix is a Grafana integration service for the SONIX project. This Flask application fetches and modifies JSON data from an external API, providing a simple interface for integration with Grafana.

## Features

- Fetches JSON data from an external API.
- Modifies the data and returns it in a structured format.
- Runs as a production-ready service using Gunicorn or uWSGI.

## Prerequisites

- Python 3.7 or higher
- poetry

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sonix-network/grafonix.git
   cd grafonix
   ```

2. Install the package in a venv and execute:

   ```bash
   ./run.sh
   ```

## Running the Application

You can run the Grafonix application using the installed command-line binary:

```bash
grafonix
```

This will start the Flask application, listening on all IPv6 addresses (`::`) at port 3001.

## Running Tests

1. Run the tests:

   ```bash
   poetry run pytest tests/
   ```

This will execute the tests located in the `tests` directory and provide you with a summary of the results.

## Project Structure

```
grafonix/
├── app.py              # Main application file
├── pyproject.toml      # Project configuration and dependencies
├── tests/              # Directory containing unit tests
│   └── test_app.py     # Unit tests for the application
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
