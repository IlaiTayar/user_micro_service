DROP TABLE IF EXISTS `user`


CREATE TABLE `user` (
    user_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    joining_date DATE NOT NULL,
    is_registered BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY(user_id)
);







INSERT INTO `user` (first_name, last_name, email, age, address, joining_date, is_registered)
VALUES ('Alice', 'Smith', 'alice.smith@example.com', 28, '123 Maple Street, New York', '2026-01-15', TRUE);

INSERT INTO `user` (first_name, last_name, email, age, address, joining_date, is_registered)
VALUES ('Bob', 'Johnson', 'bob.johnson@example.com', 34, '456 Oak Avenue, Chicago', '2026-02-10', FALSE);

INSERT INTO `user` (first_name, last_name, email, age, address, joining_date, is_registered)
VALUES ('Charlie', 'Brown', 'charlie.brown@example.com', 22, '789 Pine Road, Austin', '2026-03-01', TRUE);

INSERT INTO `user` (first_name, last_name, email, age, address, joining_date, is_registered)
VALUES ('Diana', 'Prince', 'diana.prince@example.com', 30, '321 Elm Street, Seattle', '2026-03-20', FALSE);