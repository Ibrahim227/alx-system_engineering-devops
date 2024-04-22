#!/usr/bin/python3
"""Import required module and/or lib"""
import json
import requests
import sys


def get_employee_progress(employee_id):
    """ Fetches and displays TODO list progress for a given employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    username = user_data.get('username')

    # Create a list of tasks with relevant information
    tasks_list = []
    for task in todos_data:
        dict_task = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_list.append(dict_task)

    # Create a dictionary with the employee's tasks
    employee_tasks = {str(employee_id): tasks_list}

    # Create a JSON file with the employee's tasks
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function to get and display TODO list progress
    get_employee_progress(employee_id)
