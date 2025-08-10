import re


def collapse_empty_lines(block: str) -> str:
    """
    Markdownテキスト中の連続する空行を1行にまとめる。
    段落区切りは保持する。
    """
    # stripで先頭末尾の空白行を除去 → 連続空行を1行に
    return re.sub(r"\n\s*\n+", "\n\n", block.strip()) + "\n"
