# 314-Project
Group work assignment for CSIT314

## Requirements
note these are as I understand them, feel free to discuss 

- Design a tool to test a specific type of software or website
  - No GUI, just results of testing a specific piece of software
  - Test many features of the software
- Tool must Auto generate tests
- Tool must Auto run tests
- Tool must generate a report from automatic running of test
- Tool must itself by developed using TDD i.e. unit tested
  - This is done through fuzzy testing?
  - After further work this can be also done through Metamorphic relations e.g. for testing the assert_array_equals() function
- Write report to outline how the tool works
- The Professor has said as a direct quote "As this is a 3rd year assignment the requirements are somewhat vague to give you freedom" which means we have freedom with these requirements. So long as we follow these guidelines and develop a good project we should be fine.

## The Planned Product
A tool that tests the mathematical functions implemented by the popular python library NumPy. It tests a variety of domains such as linear algebra, trigonometry, statistics and others.

## Git Guide
Git is a popular version control tool used to keep a record of the changes made to software throughout it's development. 
You can read the detail on it here: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F, I'm just going to describe how to do basic things in this guide not the theory of it.

First we need to install git, download it here https://git-scm.com/downloads and during the installation process make sure to install gitbash as well (a command line interface for git).

To "clone" this repository (get it copied to your computer) open git bash, navigate to a directory you want to clone using the standard linux cd command then run the following commmand `git clone https://github.com/Wattsy2020/314-Project.git`

Now you can make changes to the repository on your local machine, to have those changes be seen by everyone else perform the following (in git bash opened at the folder the repository is contained in)
0. before anything else make sure you are on your own branch (otherwise the changes from 5 other people will overlap). A branch is a different version of the repository that can be later merged back into the master branch. read this https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging for more info about branches and how to create them
1. `git add file_that_you_changed.py`   - this adds the changes to git
2. `git commit -m "commit message"`     - this creates a "commit", basically new version of the repository with your new changes (make sure to leave a useful message so other can understand what the commit changed)
3. `git push`                           - this uploads the changes so others can see

For people to actually see these changes they will have to be on your branch and type `git pull` which downloads all new changes.
Branches can be merged into master using a pull request on the Github website.

## Tools used
- Python 3.x 
  - install from here https://www.python.org/downloads/
- Numpy
  - Introduction and documentation here https://numpy.org/doc/stable/user/whatisnumpy.html
  - Install by entering the following command in command prompt (python is required) `pip install numpy`
