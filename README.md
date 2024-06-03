# Group Messaging and File Sharing System

## Overview

This project is a backend system for a group messaging and file-sharing application. It allows users to register, create groups, send messages (both individual and group messages), and share files within groups. The project is built using Django and Django REST framework (DRF).

## Features

- User Registration and Authentication
- Group Creation
- Sending Individual Messages
- Sending Group Messages
- Uploading and Sharing Files within Groups
- Listing Group Messages and Files

## Technologies Used

- Django
- Django REST Framework (DRF)
- SQLite (default database)
- Postman (for API testing)

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Step-by-Step Guide

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Arkutu/DjangoTests.git
    cd DjangoTests
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser (for accessing the admin panel):**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### User Registration

- **URL:** `/api/register/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    ```
- **Response:** Details of the created user.

### User Login

- **URL:** `/api/login/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```
- **Response:** Token, user ID, and email.

### Create Group

- **URL:** `/api/create_group/`
- **Method:** `POST`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Request Body:**
    ```json
    {
        "name": "testgroup",
        "members": [1, 2, 3] // Add user IDs
    }
    ```
- **Response:** Details of the created group.

### Send Group Message

- **URL:** `/api/send_group_message/`
- **Method:** `POST`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Request Body:**
    ```json
    {
        "group": 1, // Group ID
        "message": "Hello Group!"
    }
    ```
- **Response:** Message details.

### List Group Messages

- **URL:** `/api/group_messages/<group_id>/`
- **Method:** `GET`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Response:** List of messages in the group.

### Send Individual Message

- **URL:** `/api/send_message/`
- **Method:** `POST`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Request Body:**
    ```json
    {
        "receiver": 2, // Receiver User ID
        "message": "Hello!"
    }
    ```
- **Response:** Message details.

### List Individual Messages

- **URL:** `/api/messages/`
- **Method:** `GET`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Response:** List of individual messages.

### Upload File

- **URL:** `/api/upload_file/`
- **Method:** `POST`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Request Body (form-data):**
    - `uploader` (Text): Uploader User ID
    - `group` (Text): Group ID
    - `file` (File): File to upload
- **Response:** File details.

### List Group Files

- **URL:** `/api/group_files/<group_id>/`
- **Method:** `GET`
- **Headers:**
    ```sh
    Authorization: Token <your-token>
    ```
- **Response:** List of files in the group.

## Testing with Postman

1. **Open Postman** and create a new request.
2. **Set the request type** (GET, POST, etc.) and the URL for the endpoint.
3. **Add headers** if required (e.g., `Authorization` token).
4. **Set the request body** for POST requests (use `raw` and `JSON` format for JSON bodies).
5. **Send the request** and check the response.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

