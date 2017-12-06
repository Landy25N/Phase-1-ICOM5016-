-- This file contains the definitions of the tables used in the application.
--
-- Resources table
create table resources(rid serial primary key, rname varchar(20), qty integer);

-- Users table
create table users(uid serial primary key, type varchar(20), fname varchar(20), lname varchar(20), address varchar(50));

-- Requests List
create table requests(uid integer references Users(uid), rid integer references Resources(rid)), qty integer, primary key(rid, uid));

-- Supply List
create table supplies(uid integer references Users(uid), rid integer references Resources(rid)), qty integer, primary key(rid, uid));

-- Daily Stats Data (16 quantities)
create table daily(did serial primary key, small int, gallon int, med int, baby int, can int, dry int, ice int,
diesel int, pro int, gas int, md int, hd int, tools int, cloth int, pg int, bat int);

-- Weekly day table
create table weekly(did integer references Daily(did), 1st table, 2nd table, 3rd table, 4th table, 5th table,
6th table, 7th table);