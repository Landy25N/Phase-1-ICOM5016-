-- This file contains the definitions of the tables used in the application.
--
-- Resources table
create table resources(rid serial primary key, rname varchar(20), rprice float);

-- Users table
create table users(uid serial primary key, type varchar(20), fname varchar(20), lname varchar(20), phone integer);

-- Address table
create table address(uid integer references Users(uid), city varchar(20), street varchar(50), zcode int);

-- Requests table
create table requests(uid integer references Users(uid), rid integer references Resources(rid)), qty integer, primary key(rid, uid));

-- Supplies table
create table supplies(uid integer references Users(uid), rid integer references Resources(rid)), qty integer, primary key(rid, uid));

-- Purchases table
create table purchases(pid serial primary key, sellerid integer, uid integer references Users(uid), cid integer references CreditCards(cid), ptotal float, pdate Date);

-- CreditCards table
create table creditcards (cid serial primary key, uid integer references Users(uid), cnumber char(16), cexpdate char(6), credit_limit float);

-- ResourceSales table
create table resourcesales(pid integer references Purchases(pid), rid integer references Resources(rid), qty integer, pprice float, primary key(rid, pid));

-- Water table
create table water(rid integer references Resources(rid), rtype integer);

-- Medication table
create table medication(rid integer references Resources(rid), rtype integer);

-- BabyFood table
create table babyfood(rid integer references Resources(rid), rage integer, rflavor varchar(20));

-- CannedFood table
create table cannedfood(rid integer references Resources(rid), rtype integer);

-- DriedFood table
create table driedfood(rid integer references Resources(rid), rtype integer);

-- Ice table
create table water(rid integer references Resources(rid), rsize integer);

-- Fuel table
create table fuel(rid integer references Resources(rid), rtype integer, amount float);

-- MedicalDevice table
create table medicaldevice(rid integer references Resources(rid), rtype integer);

-- HeavyDevice table
create table heavydevice(rid integer references Resources(rid), rtype integer);

-- Clothing table
create table clothing(rid integer references Resources(rid), rtype integer, rsize integer);

-- Tools table
create table tools(rid integer references Resources(rid), rtype integer);

-- PowerGenerator table
create table powergenerator(rid integer references Resources(rid), rpower float, rsize integer);

-- Batteries table
create table batteries(rid integer references Resources(rid), rtype integer);