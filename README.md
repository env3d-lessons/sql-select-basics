# Learning Objectives

  - Define database, table, row, and column
  - Understand the difference between database and DBMS
  - Basic SQL language: SELECT and WHERE
  - Launching `sqlite3` on the command line
    - Using database file command line argument
    - Issuing SQL commands from the commandline and from text files
  - Working on assignments with Github Codespaces

# Introduction

Make sure you read chapter 1.1 of the textbook https://runestone.academy/ns/books/published/practical_db/PART1_SQL/01-sql-basics/sql-basics.html, as well as the SELECT BASIC tutorial from https://sqlzoo.net/wiki/SELECT_basics 

The database for all the textbook examples are stored in the database file `textbook.db`.

Complete the following exercises.  You will need to create a separate text file for each question in the form
of 1.sql, 2.sql etc. Each text file will contain a single sql command.

You can access the sql prompt using the command:

```
$ sqlite3 textbook.db
```

# Questions

In 1.sql, retrieve all fields from the table simple_books with the title 'The Hobbit'.

In 2.sql, retrieve all fields from the table simple_authors with the names 'Margaret Atwood' and 'J.R.R. Tolkien'.

In 3.sql, retrieve all fields from the table fruit_stand with prices between 1 and 2 dollars.

In 4.sql, retrieve all fields from the table simple_books with the author 'Margaret Atwood'.

In 5.sql, retrieve all fields from the table fruit_stand for the fruits 'apple' and 'orange'.

In 6.sql, retrieve all fields from the table simple_authors with author's born between 1920 and 1940.# Hand-in

Test your solution by executing the following command on the bash terminal:

```shell
$ pytest
```

When you are satisified, execute the following commands to submit:

```shell
$ git add -A
$ git commit -m 'submit'
$ git push
```
