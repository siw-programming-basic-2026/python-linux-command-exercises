import shutil
import sys

import pytest

from ex1_run_command import run_command


def test_returns_stdout_as_str():
    out = run_command([sys.executable, "-c", "print('hi')"])
    assert isinstance(out, str)
    assert out.strip() == "hi"


def test_keeps_all_lines():
    out = run_command([sys.executable, "-c", "print('a'); print('b')"])
    assert out.splitlines() == ["a", "b"]


@pytest.mark.skipif(shutil.which("who") is None, reason="who コマンドがない環境")
def test_who_runs():
    assert isinstance(run_command(["who"]), str)
