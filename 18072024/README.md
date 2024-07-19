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

You have cloned the repository and you are in G7 branch - Senior Data Engineer. 
Familiarise yourself with the code briefly. 

To make sure it all works, try running it:

```
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

Now that the list is alphabetical, the analysts notice that `Russia` is not on the list. 
The country is covered by sanctions, so they don't expect any exports, but they still would like to see it on the list to ensure no whiskey is exported. 

You speak to your team. They have considered this scenario and it is covered by the test data you are working with already. 

Ensure countries with no exports show up on the list

## Task 3

Another user complaints that when they try to get top exports per country the `derec` tool is very slow to return its results. 

```
python3 derec show top
```

Remember, they have much more data in production than we have in development,
so you will have to analyse the code to understand the problem to improve its performance. 

## Task 4

A new feature has been requested. Our users would like to be able to specify the number of top types of whiskey they want to see, 
something like this would much the default behaviour at the moment.

```
python3 derec show top 3
```

But they would also like to do things like this:
 
```
python3 derec show top 1
```

## Task 5

A new feature has been requested.
Our users would like to add a new command `save` which will save the output of the programme (countries or top) to a JSON file.
They haven't specified the format, so you will have to design it. 
