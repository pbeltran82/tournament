-- Table definitions for the tournament project.
-- 
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- author: Pedro Beltran

-- drop database in case there's any duplicate database.
DROP DATABASE IF EXISTS tournament;

--create database
CREATE DATABASE tournament;

--connect to database
\c tournament;

--create player table
CREATE TABLE player (
    name TEXT NOT NULL,
    id SERIAL PRIMARY KEY
);

--create matches table
CREATE TABLE matches (
    id serial PRIMARY KEY,
    wins INTEGER,
    matches INTEGER
);




