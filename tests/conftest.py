import pytest
import sys
from mhs5200 import MHS5200
from time import sleep
from uuid import uuid4

def pytest_addoption(parser):
    parser.addoption(
            "--port",
            action="store",
            default="",
            help="Serial port of MHS-5200 device.",
            )

@pytest.fixture(scope='session')
def port(request):
	cfg_port = request.config.getoption("--port")
	if len(cfg_port) == 0:
		if sys.platform == "win32":
			cfg_port = "COM12"
		else:
			cfg_port = "/dev/ttyUSB0"
	return cfg_port

@pytest.fixture(scope='session')
def uuid():
    return uuid4()

@pytest.fixture(scope='function')
def scope(port):
    sg = MHS5200(port)
    yield sg
    # Close the serial port.
    sg.serial.close()
    # Let Windows catch up.
    sleep(2)
