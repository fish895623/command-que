from server import __version__
from server.utils import CommandUtilities


def test_version():
    assert __version__ == "0.1.0"


def test_utils_CommandUtilities_run():
    assert CommandUtilities(cmd="echo a").run() == "a\n"
