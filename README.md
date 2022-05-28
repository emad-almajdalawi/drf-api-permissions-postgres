# Snacks API (Permissions & Postgresql)

Author: Emad Almajdalawi

Date: 25/5/2022

Application Vesrsion: 0.2.0

Overview:

Snacks API is a RESTful API created by Django framework and it is used to create, update, delete and retrieve Snacks. In v0.2.0 the API is connected to Postgresql database and the permissions are implemented.

To use this API:

- Clone the repository
- Instal the dependencies (you can find them in requirements.txt or pyproject.toml)
- Run the server locally by the command python `manage.py runserver`
Enter one of the following URLs:
    - To view (GET) or create (POST) new object: http://127.0.0.1:8000/api/snacks-list/
    - To edit (PUT) or delete (DELETE) an existing object: 'http://127.0.0.1:8000/api/< id >

<br>

[GitHub Pull Requests](https://github.com/emad-almajdalawi/drf-api-permissions-postgres/pull/1)