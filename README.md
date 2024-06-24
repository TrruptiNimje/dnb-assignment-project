# DNB-Assignment-Project
Test automation project for dnb-developer website.

## Project Summary Report
The project to automate UI tests for a web application is built using Selenium and Python. The directory structure is designed to be modular, ensuring scalability and enhancing the readability of test results. By leveraging the Page Object Model, the tests are structured in a way that enhances readability and reusability.

### Tools and Frameworks Used
Selenium: Used for browser automation to interact with the web application.
Python: The programming language used to write the test scripts.
Pytest: A testing framework that makes writing simple and scalable test cases easy.

### Directory and File Descriptions
1. tests/
This directory contains the test scripts. Each script is responsible for executing specific test cases.
test_create_app_pom.py: This script includes test cases for creating an app, attaching an API, verifying app details, and deleting the app.
test_api_navigation_pom.py: This script contains test cases for verifying navigation to the API explorer from different parts of the application and validating the list of displayed APIs under various categories.
2. pages/
This directory follows the Page Object Model (POM) design pattern. Each file represents a page of the web application, encapsulating its elements and functionalities.
login_page.py: Contains locators and methods for the login page, enabling the automation script to perform login actions.
app_page.py: Encapsulates the elements and actions related to app creation, verification, and deletion.
api_explorer_page.py: Includes locators and methods for interacting with the API explorer page, validating the displayed APIs and their categories.
base_page.py: Includes events and methods that are used throughout the project.
3.conftest.py
This file is used for configuration setups in pytest. It includes fixtures used to set up preconditions for the tests, such as initializing the WebDriver, logging into the application, and other setup tasks that need to be performed before running the tests.
4. pytest.ini
This file is used to configure customized settings for tests. I have used this to create custom markers for categorizing and running tests.
5. requirements.txt
This file is used in the projects to specify the dependencies that are needed to run the project.
**Note: Sleep time is added intentionally to see through the step-by-step execution process.**
