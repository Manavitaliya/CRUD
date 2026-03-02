# Django Student Management System

A **Django-based Student Management System** with full **CRUD functionality**, login/logout authentication, search. This project uses **SQLite3** as the database backend.

---

## Features

1. **Admin Login/Logout**
   - Only authenticated admins can access the system.
   - Logout redirects to login page.

2. **Student CRUD Operations**
   - **Create:** Add new student records with fields:
     - Name
     - Study / Course
     - Percentage (00.00 format, 0–100 validation)
     - Mobile Number (10-digit validation)
     - Address (single-line input)
     - City
     
   - **Read:** List all students with a search bar for real-time filtering (by name, study, city).
   - **Update:** Edit existing student records.
   - **Delete:** Delete student records with a confirmation popup.

3. **Validation**
   - Mobile number must be exactly 10 digits.
   - Percentage must be between 0.00 and 100.00 with up to 2 decimal places.
   - Address and other fields are properly formatted.

4. **Django Admin Panel Integration**
   - Student model is registered in the admin.
   - Allows managing student records directly from Django’s admin interface.

5. **Search Functionality**
   - Search by name, study, or city on the student list page.

6. **Database**
   - SQLite3 database (`db.sqlite3`) for storing student records.

---

## Project Installation and Setup

1. **Create folder Locally**
    - Open the folder in VS code
       
2. **Create and activate virtual environment**

        python -m venv CRUD
        CRUD\Scripts\activate
3. **Install dependencies**

        pip install django
4. **pip install django**

        python manage.py makemigrations
        python manage.py migrate
5. **Create superuser (admin)**

        python manage.py createsuperuser
6. **Run the server**

        python manage.py runserver
7. **Access the application**
   
   - Open browser at http://127.0.0.1:8000/ → login page appears.
   - Admin panel is available at http://127.0.0.1:8000/admin/.
