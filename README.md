# Pre-requisites:
* Python 3
* Selenium `pip install -U selenium`
* Web driver (chromedriver.exe): Included in `Resources` folder

# Run Tests:

### Run all tests
Using any terminal, from the root of the project execute the following command to run all the tests:
```pwsh
python -m unittest discover Tests -v
```
### Run individual test file
Using any terminal, from the root of the project execute the following command to run a specific test file:
Note: Update <test_class_name.py> with an actual test class name you want to run.
```pwsh
python -m unittest discover Tests -p <test_class_name.py> -v
```

# Notes
Developed using Python 3.9.4 and selenium 3.141.0.