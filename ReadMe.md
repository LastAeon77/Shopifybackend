# About the site:

- The Site is run upon the web framework dJango. Written in Python.
- Database used is sqlite3 for it's small size for this small scale project

# Prerequisites

- git
- python 3.8+
- pip
- virtualenv

# Install

1. Clone repository

```
git clone https://github.com/LastAeon77/Shopifybackend.git
```

2. Install dependencies (If you would like to make virtual env you could also do that)

```
pip3 install -r requirements.txt
```

# Running the program:

1. CD into correct directory

```
cd into shopify backend
```

the folder structure should include manage.py and 2 folder(inventory and shopifybackend).

# Migrate data

## (You won't need to do this since the repository also includes the database in sqlite)

```
python manage.py makemigrations
python manage.py migrate

```

# Finally Run:

```
run: python manage.py runserver

```

The site should be up and running at port 8000 (Or whatever it will tell you in the terminal in special cases)

Link: http://localhost:8000/

# Site itself

Although it is pretty self explanatory, just in case:

Download CSV Here: click "here" to download data

Create new Inventory Here: click "Here" to create new inventory

"Edit" Lets you edit data

"Delete" will permanently delete data

"Take a closer look" just moves from list view to single view
