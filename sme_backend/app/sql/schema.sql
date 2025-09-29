-- Table: Users

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, password_hash) VALUES
('user1', 'user1@example.com', 'hashed_password_1'),
('user2', 'user2@example.com', 'hashed_password_2');

-- Table: Categories

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

INSERT INTO categories (name, description) VALUES
('Food', 'Expenses for food and dining'),
('Transport', 'Travel and transportation costs'),
('Entertainment', 'Movies, games, and leisure'),
('Utilities', 'Electricity, water, internet bills');

-- Table: Expenses

CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description TEXT,
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE SET NULL
);

INSERT INTO expenses (user_id, category_id, amount, description, expense_date) VALUES
(1, 1, 12.50, 'Lunch at cafe', '2025-09-01'),
(1, 2, 25.00, 'Taxi ride', '2025-09-02'),
(2, 3, 15.75, 'Movie ticket', '2025-09-03'),
(2, 4, 60.00, 'Electricity bill', '2025-09-04');
