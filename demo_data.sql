create database financial_reporting;
use financial_reporting;

create table transactions(
id int auto_increment primary key,
transaction_date date,
category varchar(50),
type enum('income','expense'),
amount decimal(10,2)
);

create table taxes(
id int auto_increment primary key,
tax_date date,
amount decimal(10,2)
);

INSERT INTO transactions (transaction_date, category, type, amount) VALUES
('2024-01-05', 'Product Sales', 'income', 25000.00),
('2024-01-08', 'Office Rent', 'expense', 5000.00),
('2024-01-15', 'Salaries', 'expense', 10000.00),
('2024-02-02', 'Product Sales', 'income', 30000.00),
('2024-02-05', 'Utilities', 'expense', 2000.00),
('2024-02-15', 'Salaries', 'expense', 10000.00);

INSERT INTO taxes (tax_date, amount) VALUES
('2024-01-30', 2000.00),
('2024-02-28', 2500.00);

insert into transactions(transaction_date, category, type, amount) values
('2024-02-04', 'Product Sales', 'income', 23000),
('2024-01-20', 'Salaries', 'expense', 12000)
;

select* from transactions;
truncate table transactions;
select* from taxes;


