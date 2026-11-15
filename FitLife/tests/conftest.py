import subprocess
import sys
from pathlib import Path


import pytest


BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPT_PATH = BASE_DIR / "fit_life.py"


@pytest.fixture(scope="session")
def file_path():
    """Возвращает путь к файлу fit_life.py."""
    return SCRIPT_PATH


@pytest.fixture(scope="session")
def source_code(file_path):
    """Читает и возвращает исходный код fit_life.py."""
    assert file_path.exists(), (
        "Не найден файл `fit_life.py`.\n"
        "Проверьте, что основной файл проекта называется `fit_life.py` "
        "и находится в корне проекта."
    )
    return file_path.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def ast_tree(source_code):
    """Парсит исходный код и возвращает AST-дерево."""
    import ast
    return ast.parse(source_code)


@pytest.fixture
def run_program(file_path):
    """Возвращает функцию запуска fit_life.py с заданным вводом."""

    def _run(user_input):
        """Запускает программу и возвращает её stdout."""
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=user_input,
            text=True,
            capture_output=True,
            encoding="utf-8",
            timeout=2,
        )

        assert result.returncode == 0, (
            "Программа завершилась с ошибкой.\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
        return result.stdout

    return _run
