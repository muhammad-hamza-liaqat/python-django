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
git clone https://github.com/your/repo.git
cd your_project_folder

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate
```

### On Windows (CMD or PowerShell)

```bash
# 1. Clone the repo (or create your project folder)
git clone https://github.com/your/repo.git
cd your_project_folder

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# For CMD
venv\Scripts\activate

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
pip install python-decouple
```

In `settings.py`, load like this:
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
```

---

## ⚙️ Running the Django Server

Run the development server:

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Basic Commands

| Task                            | Command                          |
|---------------------------------|----------------------------------|
| Start a new app                 | `python manage.py startapp appname` |
| Make migrations                 | `python manage.py makemigrations` |
| Apply migrations                | `python manage.py migrate`       |
| Create superuser                | `python manage.py createsuperuser` |
| Collect static files (prod)    | `python manage.py collectstatic` |

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
