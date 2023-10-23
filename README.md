# 📦 Users and Groups Django Project
___

A Test Task for VNV Solutions

Welcome to the Users and Groups Django Project, a web application designed to manage users and groups. This project allows you to effortlessly create, update, and delete users and groups. Additionally, it comes equipped with some important features to ensure data integrity and consistency.

## 🚀 Installing via GitHub
___
```shell
git clone https://github.com/eduardhabryd/vnv_test_task.git
cd vnv_test_task
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate in Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## 🌟 Key Features
___

### Endpoints
The Users and Groups Django Project provides the following endpoints for managing users and groups:

- Users:
  - users/create: Create a new user.
  - users/<pk>/update: Update user information.
  - users/<pk>/delete: Delete a user.

- Groups:
  - groups/create: Create a new group.
  - groups/<pk>/update: Update group information.
  - groups/<pk>/delete: Delete a group.

### Data Integrity

The project enforces data integrity by preventing the deletion of a group that contains users. This ensures that your data remains consistent and accurate.

## 📺 Demo
___
Here are some visual representations of the project in action:
#### User List
![user-list](demo/users.png)
#### Group List
![group-list](demo/groups.png)
___
Explore the Users and Groups Django Project, and simplify your user and group management needs today! Feel free to contribute, report issues, or suggest enhancements to make it even better.




