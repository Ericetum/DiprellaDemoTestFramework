# **Installation**
From the _project's root dir_ execute:

`python setup.py install`

# **Test Markins**
To make the test execution easy, _pytest_ makes it possible to mark them like this:
`````@pytest.mark.regression
    @pytest.mark.test_search_existing
    def test_search_existing(self, main_page, username, password):
        pass
`````
To execute specified by marking test, use `-m mark` command line key.

# **Reporting**
Here we use _Allure_ reporter. We use key `--alluredir=/path/to/report_dir` for command line

# **Executing tests**
To execute full regression we type in projects console:
`pytest --alluredir /path/to/report_dir -n 5 -m regression --conf=/path/to/conf/my_conf.yml`
Where:
`-n 5` - amount of _threads_ to run tests
`--conf=/path/to/conf/my_conf.yml` - path to env config. The example can be found in _test/conf/example_env.yml_