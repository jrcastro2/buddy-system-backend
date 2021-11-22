# buddy-system-backend

RESTful API for BuddySystem web application.

## How to install

Install the required packages:
```bash
$ pip install -r requirements.txt 
```
Create the database:
```bash
$ python create-db.py
# You can populate the DB with
$  python populate-db.py
```

Run the server locally:
```bash
$ ./scripts/run.sh
```

## How to use

### Onboardings

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /onboardings          | List all onboardings      |
| GET           | /onboardings/ID       | Fetch an onboarding       |
| POST          | /onboardings          | Creates an onboarding     |
| DELETE        | /onboardings/ID       | Deletes an onboarding     |
| PUT           | /onboardings/ID       | Edit an onboarding        |


### Modules

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /modules              | List all modules          |
| GET           | /modules/ID           | Fetch a module            |
| POST          | /modules              | Creates a module          |
| DELETE        | /modules/ID           | Deletes a module          |
| PUT           | /modules/ID           | Edit a module             |


### Roles

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /roles                | List all roles            |
| GET           | /roles/ID             | Fetch a role              |
| POST          | /roles                | Creates a role            |
| DELETE        | /roles/ID             | Deletes a role            |
| PUT           | /roles/ID             | Edit a role               |


### Sections

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /sections             | List all sections         |
| GET           | /sections/ID          | Fetch a section           |
| POST          | /sections             | Creates a section         |
| DELETE        | /sections/ID          | Deletes a section         |
| PUT           | /sections/ID          | Edit a section            |


### Tasks

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /tasks                | List all tasks            |
| GET           | /tasks/ID             | Fetch a task              |
| POST          | /tasks                | Creates a task            |
| DELETE        | /tasks/ID             | Deletes a task            |
| PUT           | /tasks/ID             | Edit a task               |


### Teams

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /teams                | List all teams            |
| GET           | /teams/ID             | Fetch a team              |
| POST          | /teams                | Creates a team            |
| DELETE        | /teams/ID             | Deletes a team            |
| PUT           | /teams/ID             | Edit a team               |


### Templates

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /templates            | List all templates        |
| GET           | /templates/ID         | Fetch a template          |
| POST          | /templates            | Creates a template        |
| DELETE        | /templates/ID         | Deletes a template        |
| PUT           | /templates/ID         | Edit a template           |


### Trainings

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /trainings            | List all trainings        |
| GET           | /trainings/ID         | Fetch a training          |
| POST          | /trainings            | Creates a training        |
| DELETE        | /trainings/ID         | Deletes a training        |
| PUT           | /trainings/ID         | Edit a training           |


### Users

| Method        | URI                   | Action                    |
| ------------- | --------------------- | ------------------------- |
| GET           | /users                | List all users            |
| GET           | /users/ID             | Fetch a user              |
| POST          | /users                | Creates a user            |
| DELETE        | /users/ID             | Deletes a user            |
| PUT           | /users/ID             | Edit a user               |