# IP2 Chinese Postman Problem

## DEV BRANCH  
This branch is the branch which is used for development. Here, everyone can
edit and work on tasks.  
  
## WORKFLOW  
This is a brief explanation of the workflow which is used in IP2.
  
1. Files are placed into "./tasks". Those files are not under development yet and you are free to choose which file you'll be working on.  
2. If you've decided to work on a task, take the file and move it into the inDev folder. Please change the header of the file and put in your name. From this point on, you have one week time to generate the source code for this task. You are allowed to use any python packages, however, please speak to Robin or Joël first.
3. As soon as the file is finished, the code can be tested with files available in the testing folder. If there is no test function written yet, chances are that the test function is not written yet or that there is none. In this case, contact Robin or Joël and put the file into the awaitingTesting folder inside the testing folder.
4. If the file is tested and working, put it into the validation folder. After this point, Robin or Joël will review it and merge it into the source code in the main branch. <span style="color:red">DO NOT DO THIS BY YOURSELF! </span>.

## Basic commands
Before you start working, be sure to be on the same commit with origin/dev. To do this, write following command:

`git pull`

This will then sync you up with github. When you're finished with working, commit your files and push them to the repository with following command:

`git push`

For more help, visit:
 https://education.github.com/git-cheat-sheet-education.pdf