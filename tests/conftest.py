"""テスト対象のディレクトリを環境変数 TARGET で切り替える(既定: exercises)。

    pytest                  学生の課題を確認
    TARGET=solutions pytest 教員用の解答例を確認
"""
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TARGET = os.environ.get("TARGET", "exercises")
sys.path.insert(0, str(ROOT / TARGET))


@pytest.fixture
def who_sample():
    from compare import SAMPLE_WHO

    return SAMPLE_WHO
