# SE-Python-uitestingplayground.com
This is a repository made to practice Selenium with python by doing the exercises from the UI Test Automation Playground website.

The test suit is structured using the Page Object Model (POM) model. In Pages\basepage.py are the functions that the other pages will inherit to interact with the web pages and in Test\conftest.py is handle the session of the web driver. 

Some of the cases were straightforward to implement, like those for the 'dynamicid', 'click', 'loaddelay', 'clientdelay', and 'ajax'.

Others required more work like that for the 'dynamictable' in which I had to make a copy of the table in python by getting a list of the cells in the table and then selecting the necessary data to test the page.

Code used to get the necessary data from the table:
```
def get_table_cpu(self):
    headers = self.get_list_elements_xpath(Locators.dynamic_table_headers)
    cells = self.get_list_elements_xpath(Locators.dynamic_table_cells)
    return cells[headers.index('CPU') + cells.index('Chrome')]
```

Code of the get_list_elements_xpath() function:
```
def get_list_elements_xpath(self, locator):
    return [element.text for element in self.find_elements_xpath(locator)]
```

Or like 'sampleapp' page in which I used parametrization with pytest to do multiple test cases using different data using the same code.

Code of the test case that uses parametrization:
```
@pytest.mark.parametrize('username, password, expected_result',
                         TestData.sample_app_login_data)
def test_sample_app(self, init_driver, username, password,expected_result):
    self.sampleapp = SampleApp(init_driver)
    text = self.sampleapp.go_and_do_login(username, password)
    assert text == expected_result
```

Data stored in sample_app_login_data variable:
```
sample_app_login_data = [
    ('Roberto', 'pwd', 'Welcome, Roberto!'),
    ('', 'pwd', 'Invalid username/password'),
    ('Roberto', 'asd', 'Invalid username/password'),
    ('', '', 'Invalid username/password'),
    ('', 'asd', 'Invalid username/password'),
    ('Roberto', '', 'Invalid username/password'),
]
```

Finally, for 'shadowdom' I had to use the HTTP protocol and make Selenium ignore ssl and certificate errors to test the page because using the protocol HTTPS disabled the copy button.

Code of the function that instantiates and drops the browser session for the 'shadowdom' test:
```
def init_driver_ignore():
    if TestData.browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    yield driver
    driver.quit()
```

### Requiriments:

chromedriver.exe added to the system PATH

pytest==7.2.0

selenium==4.6.1

webdriver-manager==3.8.5
