CREATE SCHEMA IF NOT EXISTS lab;

CREATE TABLE IF NOT EXISTS lab.customers (
    customer_id BIGINT PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT,
    city TEXT,
    signup_date DATE,
    CONSTRAINT ck_customer_id_positive CHECK (customer_id > 0)
);
