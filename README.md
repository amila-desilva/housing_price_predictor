# Housing Price Predictor

The following repository contains a simple application to predict housing prices using historical data. The project is set up to use Python and Poetry for dependency management, and includes tests to ensure the functionality is correct.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 3.12](https://www.python.org/downloads/).
- You have installed [Poetry](https://python-poetry.org/docs/#installation) for dependency management.

## Installation

1. **Fork the Repository**:
   - Fork this repository to your GitHub account.

2. **Clone the Repository**:
   - Clone the forked repository to your local machine:
     ```
     git clone https://github.com/YOUR-USERNAME/housing_price_predictor.git
     cd housing_price_predictor
     ```

3. **Install Dependencies**:
   - Install the project dependencies using Poetry:
     ```
     poetry install
     ```

4. **Activate the Poetry Environment**:
   - Activate the Poetry virtual environment:
     ```sh
     poetry shell
     ```

## Running the Application

To run the application, follow these steps:

1. **Navigate to the Project Directory**:
   ```sh
   cd housing_price_predictor/housing_price_predictor
   ```

2. **Run the Application**:
    Execute the main script:
    ```sh
    python main.py
    ```

3. **Expected Output**:
    You should see the output of the Fibonacci function, which is a part of the dummy method for demonstration purposes:
    ```sh
    Fibonacci number at position 10 is 34
    ```

## Running Tests
To run the tests included in the repository, follow these steps:

1. **Set the Python Path**:
Ensure the project root is included in the Python path:
```sh
export PYTHONPATH=$(pwd)
```

2. **Run Tests Using Poetry**:
```sh
poetry run pytest
```

3. **Expected Output**:
You should see the test results indicating whether the tests passed or failed.


## Project Structure
The project directory structure is as follows:

```css
housing_price_predictor/
├── housing_price_predictor/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── test_main.py
├── pyproject.toml
└── README.md
```

- housing_price_predictor/: Contains the main application code.
- tests/: Contains the test files.
- pyproject.toml: Contains project dependencies and configuration for Poetry.
- README.md: Provides documentation for the project.

## License
None, for now (b ᵔ▽ᵔ)b