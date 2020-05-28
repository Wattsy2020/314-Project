# 314-Project
Group work assignment for CSIT314

## Requirements
note these are as I understand them, feel free to discuss 

- Design a tool to test a specific type of software or website
  - No GUI, just results of testing multiple software of the same type e.g. multiple search engines
  - Test many features of the software
  - Use post and get commands to interact with websites?
- Tool must Auto generate tests
- Tool must Auto run tests
- Tool must generate a report from automatic running of test
- Tool must itself by developed using TDD i.e. unit tested
  - This is done through fuzzy testing?
- Write report to outline how the tool works
- The Professor has said as a direct quote "As this is a 3rd year assignment the requirements are somewhat vague to give you freedom" which means we have freedom with these requirements. So long as we follow these guidelines and develop a good project we should be fine.

## The Planned Product
A tool that tests search functions of websites, specifically Ebay (though the specific website may change depending on the feasibility of web scraping). It is developed in python and uses metamorphic relations such as subsets (e.g. the results of a search with a price filter applied should be a subset of a search with no filter).

## Tools used
- Python 3.x 
  - install from here https://www.python.org/downloads/
- Beautiful soup 
  - a python library for webscraping
  - Introduction on how to use here https://www.dataquest.io/blog/web-scraping-tutorial-python/
  - Install by entering the following command in command prompt (python is required) `pip install bs4`
- Requests 
  - a python library for creating http requests, also needed for webscraping
  - install by entering the following command in command prompt `pip install requests`  
