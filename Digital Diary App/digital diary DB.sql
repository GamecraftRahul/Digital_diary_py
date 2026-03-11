
-- Create a new database
CREATE DATABASE digital_diary;

-- Use the new database
USE digital_diary;

-- Create users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(200),
    email VARCHAR(200)
);

-- Insert sample users
INSERT INTO users (username, password, full_name, email) VALUES
('john', '1234', 'John Carter', 'john@gmail.com'),
('anna', '1234', 'Anna Smith', 'anna@gmail.com'),
('mike', '1234', 'Mike Johnson', 'mike@gmail.com');

-- Create diary_notes table
CREATE TABLE diary_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Insert sample diary notes
INSERT INTO diary_notes (user_id, title, content) VALUES
(1, 'Morning Thoughts', 'Today was a productive morning.'),
(1, 'Work Ideas', 'Brainstormed new project ideas.'),
(2, 'Shopping List', 'Buy milk, eggs, and bread.'),
(3, 'Workout', 'Did 30 mins cardio and weight training.');
