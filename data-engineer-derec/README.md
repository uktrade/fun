# Data Engineering Interview Tasks

This set of tasks is used to assess your ability to work with SQL, Python, and typical data problems. 

Imagine you are working at the Department for Business and Trade supporting export analysts. 
Data engineering team build a tool for them (for simplicity in this scenario) as a python module, 
a command line application called `derec` (Data Engineering RECruitment tool).

The `derec` command line tool is used by analysts to quickly check information about whiskey exporters. 
In production system it has information about over 100 countries and hundreds of thousands of individual whiskey exports from the UK. 
But this data is not available in the development environment. 
We have only a few records (you can see them in the data folder). 

## Task 0

You have cloned the repository and are in the `seo` branch - Data Engineer. 
Familiarise yourself with the code briefly. 
See the unit tests and modules `__main__.py` as a starting point. 
The development data can be seen in CVS files in the `derec/data` folder. 

To make sure it all works, we recommend trying the following commands:

```
poetry shell
poetry install
pytest
python3 derec
python3 derec test
```

If you have any questions, ask. If you have any comments, tell. 
It is an interview, and we would like to hear you thinking through your code exploration and problem solving. 

## Task 1

You got a support request. One of the whiskey analysts complains that the country list is not ordered alphabetically. Try:

```
python3 derec show countries
```

Can you fix the problem? 

## Task 2 

Now that the list is alphabetical, the analysts notice that `Russia` is not on the list. The country is covered by sanctions, so they don't expect any exports, but they still would like to see it on the list to ensure no whiskey is exported. 

You speak to your team. They have considered this scenario and it is covered by the test data you are working with already.

Ensure countries with no exports show up on the list.

## Task 3

The tool allows to check top exports per country. At the moment it is always top 3 export. 
The users would like to be able to specify the number of top records to show. 

The current behaviour can be seen by executing 

```
python3 derec show top
```

We need to be able to do something like 

```
python3 derec show top 2
```
