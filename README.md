# Housing Price Predictor

This repository contains a Python application designed to predict housing prices using historical data. The project utilizes the 'pandas' library for data manipulation and 'pytest' for testing. The repository is configured with 'Poetry' for dependency management, ensuring that the environment is isolated and all dependencies are handled consistently.

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
   cd housing_price_predictor
   ```

2. **Run the Application**:
    Execute the main script:
    ```sh
    python src/main.py
    ```

3. **Expected Output**:
    You should see the output from operations performed on the dataset, such as filtering, updating, and deleting house records.

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
You should see test results indicating whether the tests passed or failed. The tests cover functionality for reading and writing files, as well as operations on house records.


## Project Structure
The project directory structure is as follows:

```css
housing_price_predictor/
├── docs/
├── housing_price_predictor/
│   ├── dataset/
│   │   └── data.xlsx
├── src/
│   ├── classes/
│   │   └── House.py
│   ├── utils/
│   │   ├── read_from_file.py
│   │   └── write_to_file.py
│   └── main.py
├── tests/
│   ├── test_house.py
│   ├── test_read_from_file.py
│   └── test_write_to_file.py
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```
- housing_price_predictor/: Contains the core application, including the dataset and __init__.py.
- src/: Contains the main source code, including classes, utility functions, and the main script:
   - classes/: Contains the House.py class.
   - utils/: Contains utility functions for reading from and writing to files.  
- tests/: Contains test files for unit testing.
- poetry.lock: Records the exact versions of dependencies used in the project.
- pyproject.toml: Contains project dependencies and configuration for Poetry.
- README.md: Provides documentation for the project.

## Documentation
For detailed documentation on the functions and methods implemented in this project, refer to the following files:
- docs/README.md: A detailed explanation of how each function works and the expected inputs/outputs.
- Inline comments in src/main.py, src/classes/House.py, src/utils/read_from_file.py, and src/utils/write_to_file.py.

## License
None, for now (b ᵔ▽ᵔ)b