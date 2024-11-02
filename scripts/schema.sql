--- create the name of the database as fashion - user: fashion, password : fashion

drop database fashion;
create database fashion;
use fashion;

drop table user;
drop table user_details;
drop table preference;
drop table recommendation;

create table user(
    id int not null primary key AUTO_INCREMENT,
    email varchar(255) not null unique,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    gender varchar(255) not null,
    phone_number varchar(255) not null unique,
    password varchar(255) not null,
    age int,
    city varchar(255) not null
);
create table preference (
    userid int  not null,
    preferences longtext not null,
    primary key (userid),
    foreign key (userid) references user(id));

create table recommendation (
    userid int not null,
    links json not null,
    primary key (userid),
    foreign key (userid) references user(id));

create table favourite (
    id int not null primary key AUTO_INCREMENT,
    userid int not null,
    favourite_url varchar(255) not null,
    search_occasion varchar(255) not null,
    search_weather varchar(255) not null,
    foreign key (userid) references user(id));



drop database fashion_test;
create database fashion_test;
use fashion_test;

drop table user;
drop table user_details;
drop table preference;
drop table recommendation;

create table favourite (
    id int not null primary key AUTO_INCREMENT,
    userid int not null,
    favourite_url varchar(255) not null,
    search_occasion varchar(255) not null,
    search_weather varchar(255) not null,
    foreign key (userid) references user(id));

create table user(
    id int not null primary key AUTO_INCREMENT,
    email varchar(255) not null unique,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    gender varchar(255) not null,
    phone_number varchar(255) not null unique,
    password varchar(255) not null,
    age int,
    city varchar(255) not null
);
create table preference (
    userid int  not null,
    preferences longtext not null,
    primary key (userid),
    foreign key (userid) references user(id));

create table recommendation (
    userid int not null,
    links json not null,
    primary key (userid),
    foreign key (userid) references user(id));
    
    
select * from favourite;
truncate table favourite;