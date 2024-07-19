# Data Engineering CoP pg_locks task and space invaders as an extra if we have time
Repository for the pg_lock pair programming session on 6th June

Heavily inspired by [Michal Charemza's block or not script](https://gist.github.com/michalc/d5da003fdbc673cb6b0dfd82cd4d4c2a)

## Getting Started

In order to begin, please follow these steps:

1. Open one terminal and install the required dependencies/launch docker env by running:
```
pip install psycopg2
pip install pygame

make docker_start
```

2. In another terminal, proceed with the tasks outlined below.

## Task 1 - Resolving Deadlock
To begin task 1, execute the following in terminal:
```
python task_1.py
```

This demonstrates a deadlock scenario. Your objective is to identify and implement a solution to resolve this deadlock. If you require assistance, refere to the [documentation](https://www.postgresql.org/docs/9.4/sql-rollback.html).

## Task 2 - Resolving Block
For task 2, execute the following:
```
python task_2.py
```

This task is showing a block scenario. Your goal is to implement a solution to resolve this blockage. For guidance, this is the [documentation](https://www.postgresql.org/docs/current/sql-commit.html)

## Task 3 - Space invaders
In this scenario we have a script that is littered with bugs, but should be running a space invaders type game. The task at hand is to run this initially and debug these problems to get the simple game up and running. For this, there's no documentation, just your python knowledge.

```
python task_3.py
```