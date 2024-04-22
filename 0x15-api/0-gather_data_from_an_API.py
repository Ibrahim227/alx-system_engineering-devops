#!/usr/bin/python3
"""Import the required module and/or lib"""
import requests
import sys


def gather_data_from_api(emp_id):
    """Gather employee data fro an API"""
    b_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(b_url, emp_id)
    todo_url = "{}/todos?userId={}".format(b_url, emp_id)

    # fetch resp
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    emp_name = user_data.get('name')

    # Fetch todos list for the employee
    todo_resp = requests.get(todo_url)
    todo_data = todo_resp.json()

    # calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task.get("completed", False) for task in todo_data)

    # Display progress
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks, total_tasks), end='\n')

    # Display titles of completed tasks
    for task in todo_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
            sys.exit(1)

        # Extract employee ID from command-line arguments
        emp_id = int(sys.argv[1])

        gather_data_from_api(emp_id)
