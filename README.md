About the project - The scope of this suite is to test, on Android, some of the functionalities of various tabs from the app: [Skill2Lead Android Demo App](https://github.com/Skill2Lead/AndroidDemoApp)

Prerequisites

  1. PyCharm 2024.3.2

The Python code for these tests was written using PyCharm 2024.3.2. The version of Python can be checked in cmd.exe using the command: "python --version". In my case, it is Python 3.12.

  2. Appium Module 2.15.0

Used to automate the app interaction from Python

  3. Behave Module 1.2.7.dev6 & Cucumber 17.10.0 & Gherkin 243.22562.13 

Tools used for creating the BDD Framework (Behaviour driven development) in Python

  4. Behave-html-formatter 0.9.10 & Ini 243.23654.177

Made in order to create HTML reports of the tests conducted

  5. Appium Inspector 2024.12.1

This app is needed to find the locators used for the tests in a native app. For a hybrid app the process is different

  7. Android Studio Ladybug 2024.2.2

Used to communicate with the phone in order to run the tests. We can use a physical phone (linked by USB or through Wi-Fi) or we can create an emulator of a phone.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Installation and setup

1. A folder needs to be created in the computer, where the code to run the app will be stored
2. A new project needs to be opened in PyCharm and a virtual environment needs to be created
3. The structure of a project using the BDD framework is the following:
    - The folder "features" contains the feature files for each tab where we conduct tests. These files contain the steps of each text written in a simple language that everyone can understand
    - The folder "pages" contains the Python files, with the written code for each test, for each page where we will conduct tests
    - The folder "steps" contains the files where we make the binding between the coded test and the text used to describe, in a simple language that everyone can understand, the steps of the tests
    - The file "Browser" contains the needed steps to open Appium, to open the app and to close the app
    - The file "Environment" defines the setup (the steps prior to the actual test) and teardown (all the steps needed after running the test) functions

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests description

- The EnterValue Feature contains one Scenario: While on the homepage clicking on the EnterSomeValue button, filling the textbox with "Mircea", clicking on the submit button and checking if the text submitted is shown on the page 
  
- The Login Feature contains one Scenario: Signing In with the correct credentials, checking that the tab changed, filling the textbox with "Mircea", clicking on the submit button and checking if the text submitted is shown on the page
      
- The ScrollView Feature contains one Scenario: While on the homepage clicking on the ScrollView button, checking that the tab changed, scrolling to button 16, clicking on the button and clicking "Yes" on the pop-up message
   
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running the tests

In the PyCharm terminal we use the following command line:

    behave -f=html "-o=raport.html"

And all the tests will go live and after that the results will be shown in the newly generated HTML report (raport.html in our example).
In case we add decorators (filters) on tests and we want to run only the filtered tests we have to explicit this in the command line from above.
