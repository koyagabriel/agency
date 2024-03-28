# Balance Manager

The Balance Manager allows a collection agency to ingest data files provided by their clients.
The data file is a single CSV file containing account information about consumers and what they owe to a single client.

## Development

* [Django](https://www.djangoproject.com/start/overview/) -The web framework for perfectionists with deadlines.
* [Django Rest Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible
  toolkit for building Web APIs.
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - The SDK is composed of two key Python
  packages: Botocore (the library providing the low-level functionality shared between the Python SDK and the AWS CLI)
  and Boto3 (the package implementing the Python SDK itself).

## Installation

1. Start up your terminal (or Command Prompt on Windows OS).
2. Ensure that you've `python` installed on your PC.
3. Clone the repository by entering the command `hhttps://github.com/koyagabriel/agency` in the terminal.
4. Navigate to the project folder using `cd into the project folder` on your terminal (or command prompt)
5. After cloning, create a virtual environment then install the requirements with the command:
   `pip install -r requirements.txt`.
6. Create a `.env` file in your project directory as described in `.env.sample` file.

7. After creating the `.env`, Create the database and run the following these steps:

* `python manage.py makemigrations`
* `python manage.py db migrate`

## API Documentation

Balance Manager exposes its data via an Application Programming Interface (API), so developers can interact in a
programmatic way
with the application. This document is the official reference for that functionality.

### API Resource Endpoints

| EndPoint             | Functionality            |                 Query Params                 |
|----------------------|--------------------------|:--------------------------------------------:|
| **GET** `/consumers` | Gets a list of consumers | status,min_balance,max_balance,consumer_name |

### <a name="usage"></a>Usage

1. Get a list of comsumers:
   Input:
    ```cmd
    curl -i -X GET  https://agency-afa7fdea0e2a.herokuapp.com/consumers
    ```
   Output:
    ```
    {
        "consumers": [
            {
                "id": 220,
                "name": "thomas lynch",
                "ssn": "435-27-5002",
                "agency": 1,
                "balances": [
                    {
                        "id": 319,
                        "reference_no": "f404a9dc-5196-405e-9bc1-571e34efbf29",
                        "amount": "27715.86",
                        "status": "INACTIVE",
                        "created_at": "2024-03-28T09:14:21.697072Z"
                    },
                    {
                        "id": 561,
                        "reference_no": "3389eac9-ce2c-4bfc-9a59-6035d00bfe22",
                        "amount": "1365.34",
                        "status": "IN_COLLECTION",
                        "created_at": "2024-03-28T09:14:23.616321Z"
                    }
                ]
            }
        ],
        "metadata": {
            "links": {
                "next": null,
                "previous": null
            },
            "count": 1
        }
    }
    ```

### Heroku Endpoint

https://agency-afa7fdea0e2a.herokuapp.com

### Video Endpoint

https://drive.google.com/file/d/1eMuFoHhJoFfiHQE6CwUNi88H4kCleWZV/view?usp=sharing

### Running Tests

1. Navigate to the project directory.
2. Run `python manage.py test` to run test and check coverage.

## Authors

**Koya Gabriel.**
