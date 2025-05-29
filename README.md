# 📝 My Blog - Django Web Application

- A fully functional web blog app was built using Django. 
- Users can register, log in, create blog posts, edit their profiles, and browse content by other users.
---

## 🚀 Features

- User Registration and Authentication (Login / Logout)
- Blog Post CRUD (Create, Read, Update, Delete)
- Pagination and Search
- User Profiles with Profile Pictures
- Public User Profiles at `/users/<username>/`
- Author Listing Page at `/authors/`
- Clean, Bootstrap-based responsive UI

---

## 🌐 Live Demo

👉 [View Live App](https://my-blog-app-patr.onrender.com)


---

## 💻 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (can be swapped with PostgreSQL)
- **Storage:** Django Media & Static file management
- **Deployment:** [Render](https://render.com) / [Vercel](https://vercel.com)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/my-blog-app.git
cd my-blog-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 👨‍💼 Admin Access

Create a superuser for admin login:

```bash
python manage.py createsuperuser
```

Log in at: `/admin/`

---

## 📸 Screenshots


### 🏠 Homepage

![Homepage](screenshots/home.png)

### 👤 User Profile

![Profile Page](screenshots/profile.png)

### 📝 Create Blog Post

![New Post](screenshots/new_post.png)

### 🌐 Public Profile

![Public Profile](screenshots/public_profile.png)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Thanks to Django, Bootstrap, and the open-source community 💙

---

## 👤 Author

**Yellanuru Madasi Pranay Kumar**
[GitHub](https://github.com/YOUR_USERNAME)

