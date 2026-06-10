# 📔 Digital Diary Application

A modern and secure **Digital Diary Application** built using **Python, CustomTkinter, MySQL, and TkCalendar**. This application allows users to securely store, manage, search, edit, and organize personal diary notes through an attractive graphical user interface.

---

## 🚀 Features

### 🔐 User Authentication
- Secure Login System
- User-Based Access Control
- Personalized Diary Space
- Database Authentication

### 📝 Notes Management
- Create New Notes
- Edit Existing Notes
- Delete Notes
- View All Notes
- Automatic Timestamp Storage

### 🔍 Smart Search
- Search Notes by Title
- Search Notes by Content
- Instant Keyword Filtering
- Fast Database Queries

### 📅 Date-Based Filtering
- Calendar-Based Date Selection
- Filter Notes by Creation Date
- Easy Historical Note Retrieval

### 🎨 Modern User Interface
- Built with CustomTkinter
- Light Theme Support
- Dark Theme Support
- Responsive Design
- Scrollable Notes Layout

### 🗄️ Database Integration
- MySQL Database Storage
- User Management
- Secure Data Persistence
- Structured Note Organization

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| CustomTkinter | Modern GUI Framework |
| Tkinter | GUI Components |
| MySQL | Database Management |
| mysql-connector-python | Database Connectivity |
| TkCalendar | Calendar Date Selection |
| Datetime Module | Timestamp Management |

---

# 📂 Project Structure

```text
Digital-Diary-App/
│
├── digital diary.py
├── digital diary DB.sql
├── README.md
│
└── Database
    ├── users
    └── diary_notes
```

---

# ⚙️ Database Setup

## Step 1: Create Database

```sql
CREATE DATABASE digital_diary;
```

## Step 2: Select Database

```sql
USE digital_diary;
```

## Step 3: Import SQL File

Import the provided SQL script:

```text
digital diary DB.sql
```

using MySQL Workbench or any MySQL client.

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/digital-diary-app.git
cd digital-diary-app
```

## Install Required Libraries

```bash
pip install customtkinter mysql-connector-python tkcalendar
```

---

# 🗄️ Configure Database Connection

Open:

```python
digital diary.py
```

Update database credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="digital_diary"
)
```

---

# ▶️ Run Application

```bash
python "digital diary.py"
```

---

# 🔐 Login System

The application starts with a secure login page.

### Features

- Username Authentication
- Password Verification
- User-Specific Notes
- Protected Access

---

# 📝 Notes Management

Users can create and manage diary entries with:

### Note Information

```text
Title
Content
Creation Date & Time
```

### Available Actions

- Add Notes
- Edit Notes
- Delete Notes
- View Notes

All notes are automatically stored in the MySQL database.

---

# 🔍 Search Functionality

Search notes using keywords from:

- Note Title
- Note Content

The application instantly retrieves matching notes from the database.

---

# 📅 Date Filtering

Using the integrated calendar, users can:

- Select Any Date
- View Notes Created on That Date
- Browse Historical Entries Easily

---

# 🎨 Theme Support

The application includes:

```text
Light Mode
Dark Mode
```

Users can switch themes dynamically using the Theme Toggle button.

---

# 🗃️ Database Structure

### Users Table

```text
users
├── user_id
├── username
└── password
```

### Diary Notes Table

```text
diary_notes
├── note_id
├── user_id
├── title
├── content
└── created_at
```

---

# 🔒 Security Features

- User Authentication
- User-Specific Note Access
- Protected Database Storage
- Session-Based Access Control

---

# 📱 User Interface Components

### Dashboard

- Notes Display Area
- Search Button
- Add Note Button
- Date Filter Button
- Theme Toggle Button

### Notes Cards

Each note displays:

- Title
- Content
- Creation Date
- Edit Button
- Delete Button

---

# 🎯 Future Enhancements

- User Registration System
- Password Encryption
- Rich Text Editor
- Note Categories
- Mood Tracking
- Image Attachments
- Voice Notes
- Cloud Synchronization
- Backup & Restore
- Export Notes to PDF

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the Repository
2. Create a Feature Branch
3. Commit Your Changes
4. Push to GitHub
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed using Python, CustomTkinter, MySQL, and TkCalendar to provide a secure and modern digital journaling experience.

⭐ If you found this project useful, consider giving it a star on GitHub.
