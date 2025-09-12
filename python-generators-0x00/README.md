# Python Generators — Advanced Data Handling

## About the Project

This project demonstrates advanced usage of **Python generators** to handle **large datasets**, process data in **batches**, and simulate **real-world data streaming scenarios**. It integrates database interactions with memory-efficient processing techniques, showcasing how to leverage Python’s `yield` keyword to build high-performance, scalable solutions for data-driven applications.


## Learning Objectives

-  **Master Python Generators**  
  Learn how to build and utilize generators for iterative data processing to optimize memory usage.

-  **Handle Large Datasets**  
  Implement batch processing and lazy loading for efficient handling of large volumes of data.

- **Simulate Real-world Scenarios**  
  Create solutions that simulate live data updates and apply them in streaming or paginated data systems.

- **Optimize Performance**  
  Use generators to perform memory-efficient operations like aggregations without loading full datasets into memory.

-  **Apply SQL Knowledge**  
  Use SQL with Python to dynamically fetch and process data from relational databases such as MySQL and SQLite.

## Requirements

Before starting, ensure you meet the following requirements:

- Python 3.7+
- MYSQL server installed and running locally
- Basic knowledge of Database schema design & Data seeding
- Python library:
```pip install mysql-connector-python


## Project Structure

```python-generators-0x00/
├── seed.py               # Sets up and seeds the MySQL database
├── 0-stream_users.py     # Generator to stream users row-by-row
├── 1-batch_processing.py # Generator for batch processing and filtering
├── 2-lazy_paginate.py    # Generator for lazy loading paginated data
├── 4-stream_ages.py      # Generator for memory-efficient aggregation
├── user_data.csv         # CSV file with sample user data
├── README.md             # Project documentation
├── 0-main.py             # Main test for seeding database
├── 1-main.py             # Test script for row streaming
├── 2-main.py             # Test script for batch processing
├── 3-main.py             # Test script for lazy pagination