import pytest
from selenium import  webdriver
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("launching firefox Browser")
    else:
        driver=webdriver.Ie()
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
########pytest html Report########  hook for adding environment info to html repor
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'pythonProject5'
#     config._metadata['module Name'] = 'customer'
#     config._metadata['tester'] = 'shaielsh'
# ##hook for delete/modify environment info to html report
# @pytest.mark.optioalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("plugins",None)


