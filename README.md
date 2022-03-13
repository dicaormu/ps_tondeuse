_Author: Lamine DIOP_
# Mower algorithm implementation

This projects contains an implementation of mowing algorithm problem.

### Project structure
    ├── README.md -- high level documentation of the project
    ├── data -- folder that should contain mower config files
    │   └── test.txt -- example file
    ├── main.py -- main program wrapping up source code
    ├── requirements.txt -- package requirements (here empty)
    ├── src -- folder that contains main source code
    │   ├── tondeuse.py -- mower class definition
    │   └── utils.py -- utility functions
    └── venv -- virtual environment

### How to install
This project has been implemented using python3.8.

Find below main commands to set up the project **locally**:

    git clone https://github.com/moladiop29/ps_tondeuse
    pip install virtualenv #if not already installed
    cd Path_to_project
    python -m venv ./venv
    source venv/bin/activate 

For now there isn't any requirement (additional specialized package) to run this project.

_To be update in further releases._

### How to use the code

Once you complete installation of the project, you can start exploring and testing few functions.

See below some notes about test files and main function.

##### Test file

The project is set up with a data folder where all tests file one would like to use **has to be dropped.**
Also the structure of the test file should always follow requirements below for the program to work properly

    Line 1 - Maximum size of the field - Ex 5 10 (with 1 space to separate)
    Line 2 - Position of the first mower
    Line 3 - Moves of the first mower
    Line 4 - Position of the second mower
    Line 5 - Moves of the second mower
    etc.

###### Notes

* This structure is key to understanding the file preprocessing function that has been implemented in the utils.py file
* Special characters requirements have to be strictly respected
* You can add as many mowers as you want as long as you follow file specifications

#### Main function

The program is designed to work with command lines. To run the algorithm given a file (here > test.txt), one should
simply run the following command at the root of the project.

    python main.py --file test.txt    

Even if it has been designed to work this way, feel free to modify the main function to accommodate any use you would
like.

### Further notes

Find below some ideas that could be part of the next releases (not implemented due to time constraints):

* Controls of file parsing
* Unit testing. Actually, we could have approached the project using test driven methods.
* Implementation of API basically to enable file upload through a simple form or web app (flask for example)

If we were to go full scale with such application, we could add

* Dockerization if we were to deploy this app as a service
* CI/CD pipelines to enable automated testing as well as deployment into end architecture
