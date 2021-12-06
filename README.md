# buddy-system-backend

RESTful API for BuddySystem web application.

## Requirements
- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

After installing the requirements you should be able to check the versions:
```bash
$ git --version
git version 2.25.1

$ docker --version
Docker version 20.10.11, build dea9396

$ docker-compose --version
docker-compose version 1.29.2, build 5becea4c
```

## How to install

Clone the repository:
```bash
$ cd <my directory e.g. myprojects>/
$ git clone https://github.com/jrcastro2/buddy-system-backend 
buddy-system-backend
$ cd buddy-system-backend
```

## How to run

```bash
$ cd <my directory e.g. myprojects>/buddy-system-backend
$ docker-compose up
```

## How to use

There is a CLI that provides some utilities:

```bash
# Make sure you are in the project directory
$ cd <my directory e.g. myprojects>/buddy-system-backend
# Create database
$ docker-compose exec web python buddy_system_backend/cli.py create-db
# Populate database with demo data
$ docker-compose exec web python buddy_system_backend/cli.py populate-db
# Clean database by deleting all the data
$ docker-compose exec web python buddy_system_backend/cli.py clean-db
# Destroy database
$ docker-compose exec web python buddy_system_backend/cli.py destroy-db
# Recreate database with demo data
$ docker-compose exec web python buddy_system_backend/cli.py recreate-db
```

If you need a shell you can launch one with:
```bash
$ cd <my directory e.g. myprojects>/buddy-system-backend
$ docker-compose exec web python buddy_system_backend/cli.py shell
```

## Endpoints

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