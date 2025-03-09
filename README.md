### Python API Automation Framework

Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, Pytest HTML 
- Test Data - CSV, Excel, JSON, Faker
- Advanced API Testcase - jsonschema
- Parallel Execution - x Distribute(xDist)

How to install Packages
```commandline
pip install requests pytest pytest-html allure-pytest faker jsonschema pytest-xdist python-dotenv pandas
```
How to run your Testcase Parallel
```commandline
pip install pytest-xdist
```

How to run a Basic Test with Allure report
```
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```

