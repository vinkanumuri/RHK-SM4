It would be helpful if all participants import stmpy in a jupyter notebook at some point, as our read_sm4 function is already integrated to stmpy, and it would be good to access a lot of useful features that developed in our lab over the past few years .
To install the package, you will need to follow these steps. 

How to install stmpy:
Download anaconda
Download GitHub desktop
In GitHub desktop, sign in to your GitHub account (or create a new account if you don’t have one)
Select "Clone a repository" , then select the "URL" tab, and paste the url: https://github.com/harrispirie/stmpy. Choose your local install folder (somewhere accessible, we will navigate there next) and click "Clone".
Launch Anaconda, then launch the command terminal (called something like CMD.exe prompt), and navigate to the folder containing stmpy. By default this folder should be something like C:\Users\Name\Documents\GitHub\stmpy\
Type dir on windows or ls on mac to reveal the folder contents. You should see a file called setup.py
Within the command prompt run: python setup.py develop
In the Anaconda main window, launch a jupyter notebook. In the first cell type %pylab inline and execute the cell. In the second cell type import stmpy and execute.
To call your data you just need to type in stmpy.load('xxx.sm4').
Please email me if you have any difficulties with a screenshot of your error message.