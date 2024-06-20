# RestAPI Test Automation

This project contains tests for the PoetryDB and Cat-Facts APIs.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest tests/
```

## Test Structure

- `tests/`: Contains the test cases for the APIs.

## Test Cases

### PoetryDB

1. `test_poem_random()`
    - **Description**: Tests the `/random` endpoint for fetching a random poem.
    - **Expected Result**: The response status code should be 200. The response should be a list containing a poem with a title and an author.

2. `test_poem_author()`
    - **Description**: Tests the `/author/{author}` endpoint for fetching poems by a specific author.
    - **Expected Result**: The response status code should be 200. The response should be a list of poems by the specified author.

### Cat-Facts

1. `test_random_cat_fact()`
    - **Description**: Tests the `/facts/random` endpoint for fetching a random cat fact.
    - **Expected Result**: The response status code should be 200. The response should contain a text field and a type field with the value "cat".

2. `test_all_cat_facts()`
    - **Description**: Tests the `/facts` endpoint for fetching all cat facts.
    - **Expected Result**: The response status code should be 200. The response should be a list of facts, each containing a text field and a type field with the value "cat".
