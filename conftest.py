from datetime import datetime
import logging
import pytest


def pytest_configure(config):
	if not config.option.resultlog:
		timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
		config.option.resultlog = 'log/pytest/result_log ' + timestamp + '.log'
	if not config.option.log_file:
		timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
		config.option.log_file = 'log/pytest/pytest_log ' + timestamp + '.log'

def pytest_collection_modifyitems(items):
    for item in items:
        if "csp" in item.nodeid:
            item.add_marker(pytest.mark.csplus)
        elif "pos" in item.nodeid:
            item.add_marker(pytest.mark.pos)

# def pytest_sessionstart(session):
#     session.failednames = set()

# def pytest_runtest_makereport(item, call):
#     if call.excinfo is not None:
#         item.session.failednames.add(item.originalname)

# def pytest_runtest_setup(item):
#     if item.originalname in item.session.failednames:
#         pytest.skip("previous test failed (%s)" % item.name)

def pytest_addoption(parser):
    parser.addoption("--ini", action="store", default="config.ini")
    # parser.addoption("--result-log", action="store", default="log/pytest/result_log "  + '.log')
