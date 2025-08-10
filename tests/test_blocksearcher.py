# test_search.py

import re
from pathlib import Path

import pytest

from src.search import BlockSearcher

from config.paths import SAMPLE_FILE


def test_blocksearcher_output_created(tmp_path: Path) -> None:
    """BlockSearchの出力がファイルに書き込まれることを確認"""
    result_file = tmp_path / "result.md"

    bs = BlockSearch(SAMPLE_FILE)
    text = bs.export_text()

    result_file.write_text(text, encoding="utf-8")

    assert result_file.exists()
    assert result_file.read_text(encoding="utf-8") == text


def test_blocksearcher_output_differs(tmp_path: Path) -> None:
    """BlockSearchの出力が元のテキストと異なることを確認（仕様確認）"""
    result_file = tmp_path / "result.md"

    bs = BlockSearch(SAMPLE_FILE)
    text = bs.export_text()
    result_file.write_text(text, encoding="utf-8")

    sample_text = SAMPLE_FILE.read_text(encoding="utf-8")

    assert text == sample_text


def test_blocksearcher_each_output(tmp_path: Path) -> None:
    bs = BlockSearch(SAMPLE_FILE)
    for index, block in enumerate(bs.get_blocks()):
        result_file = tmp_path / f"result{(index + 1):02d}.md"
        result_file.write_text(block)
        assert result_file.exists()
        assert result_file.read_text(encoding="utf-8") == block
