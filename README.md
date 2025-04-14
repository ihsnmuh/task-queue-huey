
# 🗓️ Task Reminder App with Django & Huey

A simple task management web app built with **Django**, **Huey**, and **Tailwind CSS** via **DaisyUI**. It allows users to create tasks with due dates, and automatically schedules reminders before the deadline.

## 🚀 Features

- ✅ User authentication (Login & Logout)
- 📌 Create, view, and mark tasks as done
- ⏰ Automatic notifications scheduled using **Huey**
- 🎨 Responsive UI with **Tailwind CSS + DaisyUI**
- 📬 Notifications shown on the website (no external service required)

---

## 🛠️ Tech Stack

- [Django](https://www.djangoproject.com/)
- [Huey](https://github.com/coleifer/huey) (task queue)
- Tailwind CSS + DaisyUI (UI framework)
- Postgresql (database)

---

## 📂 Project Structure

```
.
├── apps/
│   ├── tasks/              # Task logic & models
│   └── notifications/      # Notification system
├── templates/              # HTML templates
├── core/                   # Shared models (BaseModels)
├── static/                 # Tailwind / DaisyUI styles
├── app/
│   ├── tasks.py            # Huey tasks
│   └── methods.py          # Notification logic
├── manage.py
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the project**
   ```bash
   git clone https://github.com/ihsnmuh/task-reminder.git
   cd task-reminder
   ```

2. **Create virtual environment & install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Huey consumer**
   ```bash
   python manage.py run_huey
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Account Login**
   ```bash
   username: admin
   password: admin
   ```

---

## 📌 Notes

- All tasks have a scheduled notification 5 minutes before the deadline
- Notifications only appear inside the app — no email or SMS integration
- Timezone issues handled using Django's timezone utilities

---

## ✅ To Do for Improvement

- [ ] Add edit/delete task feature
- [ ] Option to set notification lead time
- [ ] Dark mode toggle (via DaisyUI)
- [ ] Integration with email/Telegram

---

## 🧑‍💻 Author

Developed by Ihsan Muhammad
