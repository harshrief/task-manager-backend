🛠️ Task Manager — Django Backend API
Welcome to the Task Manager Backend, a RESTful API built using Django and Django REST Framework (DRF). This API serves as the backend for the Task Manager application and supports user authentication and full task management features.

🖥️ Frontend Repo: task-manager-frontend

✨ Features
🔐 User Registration & JWT Authentication

✅ Secure login/logout flow

📦 Task CRUD (Create, Read, Update, Delete)

🗂️ Task categorization and filtering

📄 JSON-based REST API

🔄 CORS-enabled for frontend communication

🧱 Tech Stack
| Tech                              | Purpose                              |
| --------------------------------- | ------------------------------------ |
| **Django**                        | Web framework                        |
| **Django REST Framework**         | API development                      |
| **djangorestframework-simplejwt** | JWT Authentication                   |
| **SQLite** (default)              | Lightweight database for development |
| **CORS Headers**                  | Allow cross-origin requests          |

📂 Project Structure
```
task_manager_backend/
├── manage.py
├── task_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
└── users/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── urls.py
```

🚀 Getting Started
1. Clone the repository
       - git clone https://github.com/harshrief/task-manager-backend.git
       - cd task-manager-backend
2. Create and activate virtual environment
       - python -m venv venv
       - source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies
       - pip install -r requirements.txt
4. Run migrations
      - python manage.py migrate
5. Start the development server
      - python manage.py runserver
      - Your backend will be running at: http://127.0.0.1:8000/api/

🔐 API Endpoints Overview

| Endpoint              | Method         | Description               |
| --------------------- | -------------- | ------------------------- |
| `/api/register/`      | POST           | User registration         |
| `/api/token/`         | POST           | Obtain JWT access/refresh |
| `/api/token/refresh/` | POST           | Refresh JWT token         |
| `/api/tasks/`         | GET/POST       | Task list & creation      |
| `/api/tasks/<id>/`    | GET/PUT/DELETE | Task details              |

🧪 Testing the API :

You can test the API using:
1.Postman
2.Insomnia
3.curl
4.or directly from the React frontend

📝 License :

This project is licensed under the MIT License.



