Django comes with a **built-in user authentication system** — a powerful and secure framework that handles **user accounts**, **permissions**, and **authentication workflows** right out of the box.

Let’s go through it clearly 👇

---

## 🧠 What It Is

Django’s **authentication system** is part of the app called:

```python
django.contrib.auth
```

It provides ready-to-use tools for:

* User login and logout
* Password hashing and validation
* User registration and profile management
* Permissions and groups
* Authentication backends (like email, username, OAuth, etc.)
* Admin integration for user management

---

## 👤 The `User` Model

The core of this system is the **`User` model**:

```python
from django.contrib.auth.models import User
```

This model includes fields like:

* `username`
* `password` (hashed securely)
* `email`
* `first_name`, `last_name`
* `is_active`, `is_staff`, `is_superuser`
* `date_joined`

You can also **extend or replace** this model with a custom one using `AbstractUser` or `AbstractBaseUser`.

---

## ⚙️ Key Components

| Component                       | Description                                                         |
| ------------------------------- | ------------------------------------------------------------------- |
| **`User` model**                | Stores user data (username, password, email, etc.)                  |
| **Authentication backends**     | Define how users are authenticated (default is username + password) |
| **`authenticate()`**            | Verifies a user’s credentials                                       |
| **`login()` / `logout()`**      | Manage sessions for logged-in users                                 |
| **`PermissionsMixin`**          | Adds permissions and group functionality                            |
| **`@login_required` decorator** | Restricts access to logged-in users                                 |
| **`django.contrib.auth.forms`** | Provides ready forms like `UserCreationForm`, `AuthenticationForm`  |
| **`Password management`**       | Handles password reset via email, hashing, etc.                     |

---

## 🔑 Example Usage

### ✅ 1. **Authenticate and Log In a User**

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # user is now logged in
    else:
        # invalid credentials
```

---

### ✅ 2. **Log Out**

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
```

---

### ✅ 3. **Restrict Access**

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

---

### ✅ 4. **User Registration (with built-in form)**

```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
```

---

## ⚙️ Passwords — Secure by Default

Django never stores raw passwords.
They’re always **hashed** using strong algorithms like **PBKDF2**, **bcrypt**, or **Argon2**.

---

## 🔒 Permissions and Groups

Django supports role-based access control:

```python
user.has_perm('app_name.permission_code')
user.groups.add(group)
```

You can define **permissions per model** (like add, change, delete, view).

---

## 🌍 Admin Integration

The Django Admin panel automatically includes user and group management:

```
/admin/auth/user/
```

You can create users, reset passwords, and assign permissions right there.

---

## 🧩 Extending or Customizing the User Model

If you need extra fields (like phone number or profile picture):

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
```

Then set in `settings.py`:

```python
AUTH_USER_MODEL = 'myapp.CustomUser'
```

---

## ✅ Summary

| Feature           | Built-in Support        |
| ----------------- | ----------------------- |
| User model        | ✅                       |
| Registration      | ✅ (via forms or custom) |
| Login/logout      | ✅                       |
| Password hashing  | ✅                       |
| Permissions       | ✅                       |
| Groups            | ✅                       |
| Admin integration | ✅                       |
| Extendable        | ✅                       |

---

If you want, I can show you **how to customize Django’s authentication** — e.g., using **email instead of username** for login, or integrating **Google OAuth**.

Would you like that next?
