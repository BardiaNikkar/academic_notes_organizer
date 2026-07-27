# Academic Notes Organizer

## Overview

Academic Notes Organizer is a Django-based web application developed for the Advanced Programming course.

The project helps students organize their courses and lecture notes in one place. 
Users can create courses, manage notes, upload educational files, and quickly search through their content.

---

## Features

- User registration and authentication
- Course management (Create, Read, Update, Delete)
- Note management (Create, Read, Update, Delete)
- Dashboard
- Tree-style course and note navigation
- Search notes
- File upload (Media Files)
- Docker support

---
## Main Functionalities

- Authentication system using Django Authentication
- Course management
- Note management
- File uploading
- Search functionality
- Dashboard
- Dockerized deployment
---

## Technologies

- Python 3.12
- Django 6
- SQLite3
- Docker
- Docker Compose
- HTML
- CSS

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd academic_notes_organizer
```

---

## Run with Docker

Build and start the project:

```bash
docker compose up --build
```

For future runs:

```bash
docker compose up
```

Open your browser and visit:

```
http://localhost:8000
```

To stop the project:

```bash
docker compose down
```

---

## Project Structure

```
accounts/
courses/
notes/
templates/
static/
media/
Dockerfile
docker-compose.yml
requirements.txt
```

---

## Course Information

Advanced Programming Course

Computer Science Department

University of Guilan
