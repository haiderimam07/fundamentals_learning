-- in the previous we have setup and tested the wuery now that all is set we can proceed with various cscenario based questions in this file.

select * from employees;
select * from customers;
select * from order_items;

select employee_id, email from employees where employee_id < 4;

-- inserting rows in a table

-- DML ---> Data manipulation language

insert into categories
(category_name, description)
values 
('embedded', 'embedded softeare related');

select * from categories;

select * from products;

update products
set stock_quantity =50
where product_id =1;

delete from department
where departement_id=4;





-- DQL ----> Data Query language
select * from products;


select product_id, product_name as name, stock_quantity
from products;

select country from customers;
select distinct country from customers;

-- retireve sleected data from columns
select * from products
where price>100;

-- give me products having 0 stock quantity or price <150

select * from products
where stock_quantity =0 or price <150;


-- give me products which is not active
select * from products
where not is_active;

-- give me products where price having between 120 and 200

select * from products
where price >120 and price <200;


-- in this range is inclusive 
select * from products
where price between 120 and 200;

-- give me products from electronics as well as books
select * from categories;

select * from products
where category_id=1 or category_id=3 or category_id=4;

select * from products
where category_id in (1,3, 4);

-- give me products name starting with wireless

select * from products;

select * from products
where product_name like '%wireless%';

select * from products
where product_name ilike '%wireless%';

select * from products
where product_name ilike '%less%';

-- give me customers whose ohone is null

select * from customers;

select * from customers
where  phone is null;

select * from customers
where  phone is not null;

-- need tor eturn phone number not available where phone is null
select first_name ,
    last_name,
    coalesce( phone, 'N/A')
from customers;

-- sorting in sql 
-- give me products from cheapest ot expensive
select * from products
order by price asc;

-- give me products from cheap to expensive price for each category

select * from products
order by category_id desc , price asc;


select * from products
order by price desc
limit 5;

-- pagination
select * from products
order by product_id
limit 10
offset 5;

-- offset =(page-1) * limit; method for paginaiton that we used 


-- joins in sql
-- by using the foreign key and retrievug the sata from other table and joining into th eprimary table

-- give me all orders including employee details  of the emploee table that order only include  orders punched by the employee measn not null 
select * from orders;

-- this is inner join which means only where both are present following the statement completely
select * 
from orders as o 
join employees as e on e.employee_id = o.employee_id;

select * 
from orders as o 
join employees as e on o.employee_id = e.employee_id;

select o.status, o.order_id, e.email, e.first_name 
from orders as o 
inner join employees as e on o.employee_id = e.employee_id;


-- left join will also include the valkues which are not present in the forregin table and present in the foreign table basically whole orginal tbale that is why it is called left join 
-- qu- give me all orders  and include employee details of employee who processed that order and if it directly coming from customers keep the employee  empty 

select *
from orders as o 
left join employees as e on o.employee_id = e.employee_id;

-- all the rows of the right table regardless the condintion match or not
select *
from orders as o 
right join employees as e on o.employee_id = e.employee_id;

-- order amd emoloyee table all will be there
select *
from orders as o 
full outer join employees as e on o.employee_id = e.employee_id;

-- it will be nxn table from each row will be connected with each row of the right table 
select *
from orders as o 
cross join employees as e;


-- give me all customers who did not place any order
select * from customers;
select * from orders;

select c.first_name, c.email, o.status, o.order_id 
from customers as c
left join orders as o on o.customer_id = c.customer_id
where o.order_id is null;


-- give me orders which have not been paid
select o.order_id, o.customer_id, o.status, p.payment_id
from orders as o 
left join payments as p on o.order_id=p.order_id
where p.payment_id is null;


-- give me the informartion about all orders that are there in the db inlcude info about order_items, product, customer and categroy the product beling to 

select o.order_id, o.status , oi.product_id, oi.unit_price, p.product_name, p.price, c.category_name, cu.first_name, cu.last_name
from orders as o 
left join order_items as oi on oi.order_id =o.order_id
left join products as p on p.product_id=oi.product_id
left join categories as c on c.category_id=p.category_id
left join customers as cu on cu.customer_id=o.customer_id;

-- give me info about employees including their maanger;s info
-- it is self joining
select e.employee_id, e.first_name, e.last_name, e.manager_id, ei.first_name, ei.last_name 
from employees as e 
left join employees as ei on ei.employee_id = e.manager_id;


-- aggregation in sql
-- it is reducing rows into some meaningful data either average minimum maximam sum total numbers all those things


select * from customers;

select 
count(*) as "total entry" ,
count(phone) as "total phone nnumber"
from customers;

-- give me total revenue across all orders till now
select 
    order_item_id,
    quantity,
    unit_price,
    quantity * unit_price as "selling value"
    
from order_items;
select sum(quantity * unit_price) from order_items;

select avg(price) as avg_price from products;
select round(avg(price),2) as avg_price from products;

-- give me min price and max price across al products

select min(price) as minimum_price, max(price) as max_price from products;


-- group by and having use

select count(*) from products;

-- give me total number of products in each category
select distinct(category_id) as categories from products ORDER BY categories asc;


-- it is aggregating the rows but instead of all the rows it aggregating by category_id so we will use group by clause
select category_id, count(*)
from products
group by category_id;

-- give me total number of active and inactive products  in each category
select category_id, is_active, count(*)
from products
group by category_id ,is_active;

-- give me total number of products in each category include category name in the results

select 
    p.category_id, 
    c.category_name,
    count(*)
from products as p 
left join categories as c on p.category_id=c.category_id
group by p.category_id, c.category_name;


-- give me total number of products  ineach category which has total product more than 4
select category_id, count(*) as total_product
from products
group by category_id
having count(*)> 5;

-- find departments having more than one emplpyee where their combined salary of each deaprtments exceeds more than 20000 rupees

select * from employees;
select * from departments;

select 
    department_id,
    count(*),
    sum(salary) as total_sum
from employees
where manager_id is not null
group by department_id
having count(*) > 1  and sum(salary) > 200000;


-- subqueries in sql 

-- give me all custoemrs having one cancelled orders

select  c.customer_id, o.status, count(*) 
from customers as c
left join orders as o on o.customer_id=c.customer_id
where o.status ='cancelled'
group by o.status, c.customer_id;

-- we can do this using subqueries

select customer_id from orders where status='cancelled';

select *  from customers 
where customer_id in (7,9,18);

-- we can combine both queries as you can see selecting customer_id from orders give the same results as the above but it does not have the links to the customers so we can just take this query and feed inside the customers query in which we provide the row directly

select *  from customers 
where customer_id in (
    select customer_id from orders where status='cancelled'
);


-- give me all the products which are having price > avg price across all products

select * from products
where price >(select avg(price) from products);


-- give me revenue sales on category level
select 
    p.category_id, 
    sum(unit_price*quantity) as category_sales
from order_items as oi
left join products as p on p.product_id= oi.product_id
group by p.category_id;

-- give me categories having sales greater than 500
-- this is derived table in which we can simply use our normal query methods 
select cs.category_id, cs.category_sales, c.category_name
from (
        select 
        p.category_id, 
        sum(unit_price*quantity) as category_sales
    from order_items as oi
    left join products as p on p.product_id= oi.product_id
    group by p.category_id
)as cs
left join categories as c on c.category_id= cs.category_id
where category_sales>500;


-- CTE common table expression - it is just a cleaner way to write queries in which understanding and writing queries become very easy 
-- it is a way to reduce redundancy

select cs.category_id, cs.category_sales, c.category_name
from (
        select 
        p.category_id, 
        sum(unit_price*quantity) as category_sales
    from order_items as oi
    left join products as p on p.product_id= oi.product_id
    group by p.category_id
)as cs
left join categories as c on c.category_id= cs.category_id
where category_sales>500;


-- let's convert htis into cte 
-- structure of cte
with var_name as (
    ...query
)

-- this is much cleaner and easily readable we can use multiple cte just by using , 
with cs as (
    select 
        p.category_id, 
        sum(unit_price*quantity) as category_sales
    from order_items as oi
    left join products as p on p.product_id= oi.product_id
    group by p.category_id
)
select cs.category_id, cs.category_sales, c.category_name from cs
left join categories as c on c.category_id= cs.category_id;


-- reusability
-- give me total spend of  customer, also giveme average spend of all customers , also give me flag tru or false basis if the custoemrs have above average spends

select * from customers;

select 
    o.customer_id,
    sum(oi.quantity*oi.unit_price) as customer_spends
from orders as o
left join order_items as oi on oi.order_id=o.order_id
where o.status='completed'
group by o.customer_id;



with cs as (
    select 
        o.customer_id,
        sum(oi.quantity*oi.unit_price) as customer_spends
    from orders as o
    left join order_items as oi on oi.order_id=o.order_id
    where o.status='completed'
    group by o.customer_id
)
select 
    cs.customer_id,
    cs.customer_spends,
    avg(cs.customer_spends)
from cs
group by cs.customer_id,cs.customer_spends;


with cs as (
    select 
        o.customer_id,
        sum(oi.quantity*oi.unit_price) as customer_spends
    from orders as o
    left join order_items as oi on oi.order_id=o.order_id
    where o.status='completed'
    group by o.customer_id
)
select 
    cs.customer_id,
    cs.customer_spends,
    round((select avg(customer_spends) from cs),2) as avg_spends,
    cs.customer_spends> (select avg(customer_spends) from cs) as is_above
from cs;


--   sql funciton

select 
    category_id,
    sum(price) as product_sum
from products
GROUP BY category_id;
-- by using this i am restricting myself to render only category_id column  


select 
    category_id,
    product_name,
    price,
    sum(price) over (partition by category_id )as product_sum
from products;

-- add avg price column

select 
    *,
    avg(price) over() as avg_price
from products;

-- provide the ranking by the order of price
select
    product_name,
    price,
    row_number() over (order by price desc) as pro_rank_on_price
from products;


-- cancatenate union and union all

-- add unique entries
select first_name, last_name from employees
UNION
select first_name , last_name from customers;

-- add duplicate entries
select first_name, last_name from employees
UNION all
select first_name , last_name from customers;


with cn as(
    select first_name, last_name from employees
    UNION
    select first_name , last_name from customers
) select count(*) from cn;


with cn as(
    select first_name, last_name from employees
    UNION all
    select first_name , last_name from customers
) select count(*) from cn;



-- indexing

create index idx_customer_email on customers(email);

select * from customers;