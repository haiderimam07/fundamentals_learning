-- creating of table 
create table departments(
    department_id serial primary key,
    deparment_name varchar(50) not null
);

-- inserting into table 
insert into departments (deparment_name)
values
('sales'),
('support'),
('warehouse');

-- quering the table
select * from departments;

-- renaming column name 
alter table departments 
rename column deparment_name to department_name;

select * from departments;
INSERT INTO departments (department_name) VALUES ('logistics'), ('work'); -- assuming ID 5

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, manager_id, hire_date) 
VALUES ('Priya', 'Nair', 'priya.nair@techbazaar.com', 1, 'Sales Representative', 62000.00, NULL, '2020-01-01');

-- Step 2: Insert the rest of the team who report to manager_id 1
INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, manager_id, hire_date) 
VALUES 
('Fake', 'Robert', 'robert.chen@techbazaar.com', 1, 'Rep', 50000.00, 1, '2024-01-01'),
('Marcus', 'Webb', 'marcus.webb@techbazaar.com', 1, 'Sales Representative', 58000.00, 1, '2021-01-01'),
('Elena', 'Garcia', 'elena.garcia@techbazaar.com', 1, 'Senior Sales Rep', 68000.00, 1, '2019-01-01'),
('James', 'Okafor', 'james.okafor@techbazaar.com', 2, 'Support Lead', 72000.00, 1, '2018-01-01'),
('Lily', 'Zhang', 'lily.zhang@techbazaar.com', 2, 'Support Agent', 48000.00, 2, '2022-01-01'),
('Diego', 'Fernandez', 'diego.fernandez@techbazaar.com', 2, 'Support Agent', 46000.00, 2, '2023-01-01'),
('Sara', 'Osei', 'sara.osei@techbazaar.com', 3, 'Warehouse Lead', 55000.00, 1, '2020-01-01');

TRUNCATE TABLE employees RESTART IDENTITY CASCADE;

select * from employees;


-- these are some queries that are not adhering to the consrtraints that wre set while creating the table so they will throw some erros

 INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES (NULL, 'NoFirstName', 'nofirstname.demo@example.com', 1, 'Rep', 50000.00, '2024-01-01');

 INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES ('Fake', 'Robert', 'robert.chen@techbazaar.com', 1, 'Rep', 50000.00, '2024-01-01');

 INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES ('Unpaid', 'Intern', 'unpaid.demo@example.com', 1, 'Intern', 0, '2024-01-01');

 INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date, employee_status)
VALUES ('Bad', 'Status', 'badstatus.demo@example.com', 1, 'Rep', 50000.00, '2024-01-01', 'retired');



-- these commands are basic command for printing the entire table
select * from departments;
select * from payments;
SELECT * from order_items;
select * from employees;
select * from products;
select * from orders;
select * from customers;
select * from categories;