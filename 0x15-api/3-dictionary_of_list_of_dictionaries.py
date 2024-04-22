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

    # Dictionary to store tasks for all employees
    all_employees_tasks = {}

    # Iterate through each user
    for user in users_data:
        name = user.get('username')
        userid = user.get('id')

        # Fetch tasks for the current employee
        todos_url = '{}todos?userId={}'.format(api_url, userid)
        todos_response = requests.get(todos_url)
        tasks_data = todos_response.json()

        # List to store tasks for the current employee
        tasks_list = []

        # Iterate through each task for the current employee
        for task in tasks_data:
            dict_task = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(dict_task)

        # Add tasks for the current employee to the dictionary
        all_employees_tasks[str(userid)] = tasks_list

    # Create a JSON file with tasks for all employees
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function to get and display TODO list progress
    get_employee_progress(employee_id)
