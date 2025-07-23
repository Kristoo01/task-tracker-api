# Task Tracker API

A minimal RESTful API for basic task management, built using Python and Flask. This project was created as part of learning Python web development and Docker containerization.

---

## Features

* Create, view, update, and delete tasks
* Mark tasks as completed
* Simple in-memory storage (no database)
* Dockerized for easy setup and deployment

---

## Tech Stack

* Python 3
* Flask
* Docker

---

## API Endpoint

| Method | Endpoint            | Description            |
|--------|---------------------|------------------------|
| GET    | `/tasks`            | Retrieve all tasks     |
| POST   | `/tasks`            | Create a new task      |
| PUT    | `/tasks/<task_id>`  | Mark task as completed |
| PATCH  | `/tasks/<task_id>`  | Update task title      |
| DELETE | `/tasks/<task_id>`  | Delete a task          |

---

## Running the Project (with Docker)

### 1. Build the Docker image:

`docker build -t task-tracker-api .`

### 2. Run the container:

`docker run -p 5000:5000 task-tracker-api`

Note: If port 5000 is already in use (this happened during my setup), you can either:
* Free up port 5000 by stopping the process using it, or
* Run the container on an alternative port, for example:

`docker run -p 5001:5000 task-tracker-api`

In that case, your API will be accessible at: http://localhost:5001/tasks

### Example API Call

Using `curl` to create a task:

`curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Learn Docker"}'`

(If using port 5001, replace the URL accordingly.)

---

## Future Improvements

* Add persistent storage using SQLite or PostgreSQL
* User authentication
* Add unit tests

---

## Project Status

✅ Minimal viable project (MVP) complete.

---

## License

This project is licensed under the [MIT License](LICENSE).





