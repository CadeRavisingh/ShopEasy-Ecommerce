create database shopeasy;
use shopeasy:
-- user table
create table users(
    id int auto_increment primary key,
    full_name varchar(150) not null,
    email varchar(200) unique not null,
    mobile varchar(100) not null,
    created_at timestamp defult current_timestamp
);

-- Products table
create table products(
    id int auto_increment primary key,
    product_name varchar(100) not null,
    description text,
    price decimal(10,2) not null,
    image varchar(300),
    stock int defult 0
);
-- cart table
create table cart(
    id int auto_incrment primary key,
    user_id int,
    product_id int,
    quantity int defult 1,
    foreign key (user_id) references user(id),
    foreign key (product_id) references products(id)
);
-- Order table
create table orders(
    id auto_increment primary key,
    user_id int,
    total_amount decimal(10,2),
    payment_method varchar(50) ,
    order_status varchar(50) default 'pending',
    order_date timestamp default current_timestamp,
    foreign key (user_id) references users(id)
);
-- order item
create table order_item(
    id auto_increment primary key,
    order_id int,
    product_id int,
    quantity int,
    price decimal(10,2),
    foreign key (order_id) references order(id),
    foreign key (product_id) references products(id)
);