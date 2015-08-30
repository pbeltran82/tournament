-- Table definitions for the tournament project.
-- 
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- author: Pedro Beltran
drop table player;

drop table matches;

create table player (
    name text,
    id serial
);

create table matches (
    id serial,
    wins integer,
    matches integer
);




