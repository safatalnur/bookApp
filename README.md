# Children's Book App
![](./screenshots/Landing_Page.png)

## Technologies Used

* [PostgresQL](https://www.postgresql.org/)
* [Python3](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Materialize](https://materializecss.com/)
* [CSS3](https://www.w3schools.com/css/)

## Installation
1. Create a "bookApp" PostgresQL database, ```$ createdb bookApp```
2. clone the project from GitHub (https://github.com/safatalnur/bookApp)
3. Create database migration files ```$ python3 manage.py makemigrations```
4. Synchronize database ```$ python3 manage.py migrate```
5. Run the server ```$ python3 manage.py runserver```
6. Browse to ```localhost:8000```


## Planning Stage
* [Trello Board](https://trello.com/b/JGXywzXC)
* [Entity Relationship Diagram (ERD)]![](./screenshots/BookApp.png)
* [Wire Frame Design]

## Features
* Sign-up as a new user in the Landing Page
* View all the books in "All Books"
* Go to "Details" and click "READ THE BOOK" to open the pdf file
* Ability to edit or delete as a user
* Like/ Dislike the book
* Click on "Add New Book" to create your own book. (book has to be in pdf file)
