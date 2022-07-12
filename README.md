### Introduction

The spending tracker is a simple full stack Python web app deisgned as part of the solo project for my Professional Software Development PDA course with CodeClan. The project is to build an app that allows a user to track their spending.

#### Brief

The app allows the user to:

- create and edit merchants, e.g. Tesco, Amazon, ScotRail
- create and edit tags for their spending, e.g. groceries, entertainment, transport
- assign tags and merchants to a transaction, as well as an amount spent on each transaction.
- display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

#### Inspired by:

Monzo, MoneyDashboard, lots of mobile/online banking apps

#### Running the app

You will require SQLite3 to set up the database and Flask to run the app. Once repository is cloned, the following should be entered in the terminal from the startcode

1.

```bash
sqlite3 db/spending_tracker.db < db/spending_tracker.sql
```

2.

```bash
python3 console.py
```

3.

```bash
flask run
```

#### Tech Stack

Python, Flask, SQLite3, HTML, CSS

#### Future and Continuous Improvements

- User can apply a budget, and app will alert user if nearing or gone over budget
- User can add a timestamp to their transactions
- User can filter their transactions by different options ie category, month etc
