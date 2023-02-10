# Selenium Web Navigation Project
## Introduction
This project uses the selenium package for Python to open a website and navigate to 4 different pages of the site. Unit tests have also been written for the code to ensure its functionality. The project has been uploaded to a repository for you to review.

## Prerequisites: You will need to have the following installed:

### Virtual environment

#### To create a virtual environment on Windows:

- Open the Command Prompt.
- Type the following command to install virtual environment: ```pip install virtualenv```
- Create a new virtual environment using the following command: ```virtualenv venv_name``` Replace "venv_name" with the desired name of your choice.
- Activate the virtual environment using the following command: ```venv_name\Scripts\activate```
- Now that the virtual environment is active, install Python by typing the following command: ```brew install python``` or ```python -m ensurepip --upgrade```

#### To create a virtual environment on Linux and MacOS:

- Open the terminal.
- Type the following command to install virtual environment: ```pip install virtualenv```
- Create a new virtual environment using the following command: ```virtualenv venv_name``` Replace "venv_name" with the desired name of your virtual environment.
- Activate the virtual environment using the following command: ```source venv_name/bin/activate```
- Now that the virtual environment is active, install Python by typing the following command: ```brew install python``` or ```python -m ensurepip --upgrade```

* You can now install packages and use them in the virtual environment without affecting the packages installed in your global Python environment.

### Selenium
#### To install Selenium:
```pip install selenium```

### A web browser of your choice (e.g. Chrome, Firefox, etc.)
### When you are finished using the virtual environment, you can deactivate it using the following command:
```deactivate```

## Steps
- After creating and activating a virtual environment
- Install all required packages
- Or you can easily fork my repository then:
    * ```cd .../Selenium_test``` change directory to the forked folder location
    * ```source seleniumEnv/bin/activate``` activate the virtual environment
    * ```python -m unittest main.py``` to run the test
## Code
This code uses the selenium package to open a website of [Gojo Afalagi](https://gojo.herokuapp.com) choice and navigate to 4 different pages.

## Unit Tests
The code includes unit tests to ensure that the website is opened and the navigation to different pages is successful. You can run the unit tests using the following command:

```python -m unittest main.py```

## Repository
The project has been uploaded to a repository for you to fork. You can find the repository at the following link:
https://github.com/ezekielmisgae/Selenium_test
