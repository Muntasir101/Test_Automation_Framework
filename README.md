# Selenium Python Automation Framework

This is a basic Selenium automation framework developed in Python using the Page Object Model (POM) design pattern. The framework is designed to be modular, scalable, and maintainable. It includes features such as configuration management, logging, basic and advanced reporting, data-driven testing, and more.

## Features

- **Page Object Model (POM):** Locators and functionality are separated using the Page Object Model for better maintainability.

- **Separate Locators:** Locators are kept separate for easy modification and maintenance.

- **Separate Test Data:** Test data is stored separately for easy management and updates.

- **Configuration Management:** Configuration settings are handled separately for flexibility and ease of configuration changes.

- **Logging:** Logging is implemented to capture detailed information during test execution.

- **Conftest:** Configuration for Pytest is set up in a separate conftest file.

- **Assertions:** Custom assertion methods are provided for better error reporting.

- **Basic Reporting:** Pytest basic reporting is integrated for easy test result analysis.

- **Advanced Reporting:** Pytest HTML reporter is integrated for detailed and visually appealing test reports.

- **Data-Driven Testing:** The framework supports data-driven testing with external data sources.

- **DocString:** DocStrings are used for clear documentation of test cases and functions.

- **Separate Config:** Configuration settings are separated for better organization.

- **Parallel Execution:** Parallel execution of tests is not supported in this version.

- **Parametrization:** Parametrization of tests is not implemented in this version.

- **Error Handling:** Basic error handling is included.

- **Listeners:** Event listeners are not implemented in this version.

## Usage

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
# Install Dependencies:
pip install -r requirements.txt
# Run Tests:
pytest test_directory/

# Configuration
Modify the configuration file (config.ini) with your specific settings.
[General]
base_url = https://example.com
timeout = 10

[Credentials]
username = your_username
password = your_password

# Report Generation
After running the tests, HTML reports can be found in the reports directory. Open the HTML report in a browser for detailed test results.

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your enhancements.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
