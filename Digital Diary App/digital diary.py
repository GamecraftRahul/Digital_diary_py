import tkinter as tk
from tkinter import messagebox, simpledialog
import customtkinter as ctk
import mysql.connector
from tkcalendar import Calendar
from datetime import datetime

# ------------------ DATABASE CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # change if needed
    password="RAHUL123",  # your MySQL password
    database="digital_diary"
)
cur = conn.cursor(buffered=True)


# ------------------ APP CLASS ------------------
class DigitalDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Diary App")
        self.root.geometry("1000x700")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.current_user_id = None

        # Login Frame
        self.login_frame = ctk.CTkFrame(self.root)
        self.login_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.login_frame, text="Digital Diary Login", font=("Roboto", 24)).pack(pady=20)
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)
        ctk.CTkButton(self.login_frame, text="Login", command=self.do_login).pack(pady=20)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ------------------ LOGIN ------------------
    def do_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        cur.execute("SELECT user_id FROM users WHERE username=%s AND password=%s", (username, password))
        result = cur.fetchone()
        if result:
            self.current_user_id = result[0]
            self.show_diary()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    # ------------------ SHOW DIARY ------------------
    def show_diary(self):
        self.login_frame.pack_forget()
        self.diary_frame = ctk.CTkFrame(self.root)
        self.diary_frame.pack(expand=True, fill="both")

        # Header
        header_frame = ctk.CTkFrame(self.diary_frame)
        header_frame.pack(fill="x", pady=10)
        ctk.CTkLabel(header_frame, text="Your Digital Diary", font=("Roboto", 24)).pack(side="left", padx=20)
        ctk.CTkButton(header_frame, text="Add Note", command=self.add_note).pack(side="left", padx=10)
        ctk.CTkButton(header_frame, text="Search Notes", command=self.search_notes).pack(side="left", padx=10)
        ctk.CTkButton(header_frame, text="Filter by Date", command=self.filter_by_date).pack(side="left", padx=10)
        ctk.CTkButton(header_frame, text="Toggle Theme", command=self.toggle_theme).pack(side="right", padx=20)

        # Notes Display Area
        self.notes_container = ctk.CTkScrollableFrame(self.diary_frame, width=950, height=600)
        self.notes_container.pack(pady=10)
        self.load_notes()

    # ------------------ TOGGLE THEME ------------------
    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        if current == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    # ------------------ LOAD NOTES ------------------
    def load_notes(self, notes=None):
        for widget in self.notes_container.winfo_children():
            widget.destroy()

        if notes is None:
            cur.execute(
                "SELECT note_id, title, content, created_at FROM diary_notes WHERE user_id=%s ORDER BY created_at DESC",
                (self.current_user_id,))
            notes = cur.fetchall()

        if not notes:
            ctk.CTkLabel(self.notes_container, text="No notes found.", font=("Roboto", 16)).pack(pady=20)
            return

        for note in notes:
            note_id, title, content, created_at = note
            card = ctk.CTkFrame(self.notes_container, corner_radius=10, border_width=1)
            card.pack(pady=10, padx=20, fill="x")

            title_label = ctk.CTkLabel(card, text=f"{title} ({created_at.strftime('%Y-%m-%d %H:%M')})",
                                       font=("Roboto", 16, "bold"))
            title_label.pack(anchor="w", padx=10, pady=5)
            content_label = ctk.CTkLabel(card, text=content, font=("Roboto", 14), wraplength=900, justify="left")
            content_label.pack(anchor="w", padx=10, pady=5)

            # Action Buttons
            btn_frame = ctk.CTkFrame(card)
            btn_frame.pack(anchor="e", pady=5, padx=10)
            ctk.CTkButton(btn_frame, text="Edit", width=60, command=lambda nid=note_id: self.edit_note_card(nid)).pack(
                side="left", padx=5)
            ctk.CTkButton(btn_frame, text="Delete", width=60,
                          command=lambda nid=note_id: self.delete_note_card(nid)).pack(side="left", padx=5)

    # ------------------ ADD NOTE ------------------
    def add_note(self):
        title = simpledialog.askstring("Title", "Enter note title:")
        if not title:
            return
        content = simpledialog.askstring("Content", "Enter note content:")
        if not content:
            return
        cur.execute("INSERT INTO diary_notes (user_id, title, content) VALUES (%s, %s, %s)",
                    (self.current_user_id, title, content))
        conn.commit()
        self.load_notes()

    # ------------------ EDIT NOTE ------------------
    def edit_note_card(self, note_id):
        cur.execute("SELECT title, content FROM diary_notes WHERE note_id=%s", (note_id,))
        note = cur.fetchone()
        if note:
            new_title = simpledialog.askstring("Edit Title", "Enter new title:", initialvalue=note[0])
            new_content = simpledialog.askstring("Edit Content", "Enter new content:", initialvalue=note[1])
            if new_title and new_content:
                cur.execute("UPDATE diary_notes SET title=%s, content=%s WHERE note_id=%s",
                            (new_title, new_content, note_id))
                conn.commit()
                self.load_notes()

    # ------------------ DELETE NOTE ------------------
    def delete_note_card(self, note_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this note?"):
            cur.execute("DELETE FROM diary_notes WHERE note_id=%s", (note_id,))
            conn.commit()
            self.load_notes()

    # ------------------ SEARCH NOTES ------------------
    def search_notes(self):
        keyword = simpledialog.askstring("Search Notes", "Enter keyword:")
        if not keyword:
            return
        cur.execute(
            "SELECT note_id, title, content, created_at FROM diary_notes WHERE user_id=%s AND (title LIKE %s OR content LIKE %s) ORDER BY created_at DESC",
            (self.current_user_id, f"%{keyword}%", f"%{keyword}%"))
        results = cur.fetchall()
        self.load_notes(results)

    # ------------------ FILTER BY DATE ------------------
    def filter_by_date(self):
        top = tk.Toplevel(self.root)
        top.title("Select Date")
        cal = Calendar(top, selectmode="day")
        cal.pack(pady=20)

        def select_date():
            selected = cal.selection_get()
            cur.execute(
                "SELECT note_id, title, content, created_at FROM diary_notes WHERE user_id=%s AND DATE(created_at)=%s ORDER BY created_at DESC",
                (self.current_user_id, selected))
            results = cur.fetchall()
            self.load_notes(results)
            top.destroy()

        ctk.CTkButton(top, text="Filter", command=select_date).pack(pady=10)

    # ------------------ ON CLOSE ------------------
    def on_close(self):
        cur.close()
        conn.close()
        self.root.destroy()


# ------------------ RUN APP ------------------
if __name__ == "__main__":
    root = ctk.CTk()
    app = DigitalDiaryApp(root)
    root.mainloop()
