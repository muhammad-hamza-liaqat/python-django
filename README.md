# 🐍 Django Starter Project

This is a basic setup guide for starting a new Django project. It includes instructions for both **macOS** and **Windows** environments.

---

## 📦 Prerequisites

- Python 3.7+
- pip (comes with Python)
- [Git (optional)](https://git-scm.com/)
- Text Editor like VS Code

---

## 🖥️ Setting up the Virtual Environment

### On macOS / Linux

```bash
# 1. Clone the repo (or create your project folder)
git clone https://github.com/muhammad-hamza-liaqat/python-django.git
cd your_project_folder

# 2. Create virtual environment
python3 -m venv env

# 3. Activate virtual environment
source env/bin/activate
```

### On Windows (CMD or PowerShell)

```bash
# 1. Clone the repo (or create your project folder)
git clone https://github.com/muhammad-hamza-liaqat/python-django.git
cd your_project_folder

# 2. Create virtual environment
python -m venv env

# 3. Activate virtual environment
# For CMD
env\Scripts\activate

# For PowerShell
venv\Scripts\Activate.ps1
```

---

## 📁 Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt` yet, generate one after installing Django:

```bash
pip install django
pip freeze > requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory of your project:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
```

> You can use `python-decouple` or `dotenv` to load `.env` in `settings.py`.

Install:

```bash
pip install python-dotenv
```

In `settings.py`, load like this:

```python
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
```

---

## ⚙️ Running the Django Server

Run the development server:

```bash
python manage.py runserver
```

To run the seeders, to create super_user

```bash
python manage.py run_seeders
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Basic Commands

| Task                        | Command                             |
| --------------------------- | ----------------------------------- |
| Start a new app             | `python manage.py startapp appname` |
| Make migrations             | `python manage.py makemigrations`   |
| Apply migrations            | `python manage.py migrate`          |
| Create superuser            | `python manage.py createsuperuser`  |
| Collect static files (prod) | `python manage.py collectstatic`    |
| run the seeders superuser   | `python manage.py run_seeders`      |

---

## ✅ Best Practices

- Always use a virtual environment
- Keep your `SECRET_KEY` and credentials in `.env` (do not commit it)
- Use `.gitignore` to exclude `venv/`, `.env`, `__pycache__/`, etc.

Add a `.gitignore`:

```gitignore
venv/
__pycache__/
*.pyc
*.sqlite3
.env
.DS_Store
```

---

## 🧪 Testing

Run tests using:

```bash
python manage.py test
```

---

## 🚀 Deployment

For production, use:

- `DEBUG=False`
- `ALLOWED_HOSTS=['yourdomain.com']`
- Consider deploying on **Render**, **Heroku**, or **DigitalOcean**

---

## 📎 License

This project is licensed under the MIT License.
