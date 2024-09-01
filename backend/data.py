import requests

# Define a list of employee data
employee_data_list = [
    {
        "name": "John Doe 1",
        "address": "123 Oak St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "50000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 2",
        "address": "456 Pine St, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "55000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 3",
        "address": "789 Elm St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "45000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 4",
        "address": "321 Main St, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "60000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 5",
        "address": "654 Oak St, Anyplace City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "52000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 6",
        "address": "987 Pine St, Somewhere Else",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "57000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 7",
        "address": "159 Elm St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "48000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 8",
        "address": "753 Oak Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "62000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 9",
        "address": "369 Pine St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "47000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 10",
        "address": "852 Elm Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "65000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 11",
        "address": "159 Oak St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "49000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 12",
        "address": "753 Pine Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "58000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 13",
        "address": "369 Elm St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "51000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 14",
        "address": "852 Oak Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "60000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 15",
        "address": "159 Pine St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "46000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 16",
        "address": "753 Elm Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "63000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 17",
        "address": "369 Oak St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "53000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 18",
        "address": "852 Pine Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "59000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 19",
        "address": "159 Elm St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "47000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 20",
        "address": "753 Oak Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "61000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 21",
        "address": "369 Pine St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "48000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 22",
        "address": "852 Elm Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "64000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 23",
        "address": "159 Oak St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "50000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 24",
        "address": "753 Pine Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "57000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 25",
        "address": "369 Elm St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "52000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 26",
        "address": "852 Oak Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "59000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 27",
        "address": "159 Pine St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "45000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 28",
        "address": "753 Elm Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "62000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 29",
        "address": "369 Oak St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "54000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 30",
        "address": "852 Pine Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "58000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 31",
        "address": "159 Elm St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "46000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 32",
        "address": "753 Oak Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "60000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 33",
        "address": "369 Pine St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "49000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 34",
        "address": "852 Elm Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "63000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 35",
        "address": "159 Oak St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "51000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 36",
        "address": "753 Pine Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "56000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 37",
        "address": "369 Elm St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "53000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 38",
        "address": "852 Oak Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "58000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 39",
        "address": "159 Pine St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "44000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 40",
        "address": "753 Elm Rd, Othertown USA",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "61000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 41",
        "address": "369 Oak St, Somewhere City",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "55000.00",
        "shift": "day",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 42",
        "address": "852 Pine Rd, Elsewhere Town",
        "qualification": "Master's Degree",
        "department": 2,
        "designation": 1,
        "salary": "57000.00",
        "shift": "night",
        "employee_type": "ot"
    },
    {
        "name": "John Doe 43",
        "address": "159 Elm St, Anytown USA",
        "qualification": "Bachelor's Degree",
        "department": 2,
        "designation": 1,
        "salary": "45000.00",
        "shift": "day",
        "employee_type": "ot"
    },
]

# Loop through the employee data list and make POST requests
for employee_data in employee_data_list:
    response = requests.post("http://127.0.0.1:8000/api/employees/", json=employee_data)
    if response.status_code == 201:
        print(f"Employee '{employee_data['name']}' added successfully!")
    else:
        print(f"Error adding employee '{employee_data['name']}': {response.status_code} - {response.text}")