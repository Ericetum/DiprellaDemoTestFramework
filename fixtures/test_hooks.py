def pytest_addoption(parser):
    parser.addoption("--conf",
                     action='store',
                     help="Path to the environment configuration")
