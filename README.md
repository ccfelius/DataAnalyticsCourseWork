# Fundamentals of Data Analytics
SEN163A Fundamentals of Data Analytics practical - TU Delft

### Assignments

These are the assignments of Fundamentals of Data Analytics. This course is given by Delft University of Technology.
Note: Improved version of Assignment 2 is not available. Datasets are missing, available upon request.

# Instructions

## Set up Github

* Install git bash

If you have installed git bash open it and subsequently navigate to folder where you want to 'clone' the existing repository in using:

```
cd path_to_folder
```

Then clone the repository "DataAnalyticsFundamentals" into your selected folder using

```
git clone https://github.com/ccfelius/DataAnalyticsFundamentals.git
```

The repository is now cloned which means that you have a local copy of the repository on your computer.
Subsequently, establish a remote by using the command stated below.

```
git add remote upstream https://github.com/ccfelius/DataAnalyticsFundamentals.git
```

Note that 'upstream' is just a name which you could change. 
If you want to update your local repository, i.e. incorporate changes made by others, you need to 'fetch' your remote repo. 
In other words, you collect the changes made by using the following command:

```
git fetch upstream
```

Then it is usefull to check your local repository, if you made any changes that could cause merging conflicts.
You do this by

```
git checkout master
```

If there are no changes made, you can easily merge the collected changes with your local repository by:

```
git merge upstream/master
```

Now your local repository is up to date!

### How to Push to original repository on github

Check which files you modified with the comment:

```
git status
```

Then add the desired files that you want to commit, i.e. you want to add to the original repository online, with

```
git add name_of_file name_of_other_file
```

Or add all files that you changed

```
git add .
```

Then, if all changes that you wanted to add are added, you can commit your changes with

```
git commit -m "Message what you did"
```

Note that -m denotes that you are adding a message. The last step you need to take is push your commits with

```
git push
```
