#!/usr/bin/python3
"""Import required module and/or lib"""
import json
import requests


def get_employee_progress():
    """ Fetches and displays TODO list progress for a given employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users".format(base_url)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Dictionary to store tasks for all employees
    all_employees_tasks = {}

    # Iterate through each user
    for user in user_data:
        name = user.get('username')
        userid = user.get('id')

        # Fetch tasks for the current employee
        todos_url = '{}todos?userId={}'.format(base_url, userid)
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
    # Call the function
    get_employee_progress()
