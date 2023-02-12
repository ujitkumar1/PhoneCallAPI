## PhoneCallAPI: A Python app that allows to manage and track their calls

### Description:

A RESTful API built with Python Flask that enables users to manage and track their phone calls. The API includes an
endpoint for retrieving all calls associated with a specific phone number and allows for viewing call information.

### Prerequisites:

1. Python Programming language
2. MySql
3. flask
4. flask_restful
5. json

### Installation:

To install the required packages and libraries, run the following command in your current working directory:

command

pip install -r requirements.txt

This command will install all the necessary dependencies listed in the requirements.txt file, allowing you to run the
project without any issues.

### Usage:

To run the application, execute the following command in the src directory

Command

python main.py

This will start the application, and you should be able to use it. (or) Directly run the main.py file

#### Endpoint Working:

1. Initiate-call(http://127.0.0.1:5000/initiate-call)

    - Endpoint for initiating a call report based on the form phone number and to phone number.

    - Example:

      Input:
      Json_data = {
      "from_number":9935567501,
      "to_number":1234567810
      }

      Output:"Data saved from number: 9935567501 to number: 1234567811"

    * A call will be initiated from 9935567501 to 1234567810, the information will be then stored in the database.

2. call_report(http://localhost:5000/call-report?phone=1234567812)

    - Endpoint for retrieving call report based on phone number.

    - Example:

      Resquest_url : http://localhost:5000/call-report?phone=1234567812

      Output:
      {
      "Success": true,
      "data": [
      {
      "id": 1,
      "from_number": 1234567812,
      "to_number": 1234567814,
      "start_time": "2023-02-12 16:10:27.651245"
      }
      ],
      "next_url": "http://localhost:5000/call-report?phone=1234567812&page=2"
      }

    - next_url refers the url to the next pagination

### Contact:

Name : Ujit Kumar

Email : ujitkumar1@gmail.com