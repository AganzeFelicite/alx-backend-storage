-- creating a user table
-- with a unique email address
CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCRMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
