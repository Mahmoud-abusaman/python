CREATE DATABASE practice_db;
USE practice_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
insert into users (name,email,age) values ("mahmoud","mod2saman@gmail.com",22);
select * from users;

