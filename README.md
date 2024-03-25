# MongoDB Database Manager

## Overview

The database manager in this project is a Python class designed to interact with MongoDB. It provides various methods for managing data stored in MongoDB collections. The manager facilitates operations such as creating tables, adding data, retrieving existing relations, deleting rows, loading data, searching, updating records, and generating statistics based on relationships.

## Prerequisites

- Python 3.x
- MongoDB installed and running on `localhost` (default port: `27017`)

## Installation

1. Install Python (if not already installed).
2. Install the required Python packages using pip:

```
pip install pymongo
```

## Usage

1. Import the `DatabaseManager` class into your Python script.
2. Instantiate the `DatabaseManager` class:

```python
from mongo_db import DatabaseManager

database_manager = DatabaseManager()
```

3. Use the various methods provided by the `DatabaseManager` class to perform database operations.

## Notes

- Ensure that MongoDB is running on `localhost` and accessible on the default port `27017`.
- Adjust the MongoDB connection parameters in the `DatabaseManager` class if necessary.
- Make sure to handle exceptions appropriately for error scenarios such as database connection failures or invalid input data.
