import re
import logging


class BlockTransformer:
    def __init__(self, block: str):
        self.block = block
        self.lines = block.splitlines(keepends=True)

    def make_yml(self) -> str:
        """
        yamlスタイルのstringを---と---で囲む。
        """
        pass

    def collapse_empty_lines(self) -> str:
        """
        Markdownテキスト中の連続する空行を1行にまとめる。
        段落区切りは保持する。
        """
        # stripで先頭末尾の空白行を除去 → 連続空行を1行に
        text = re.sub(r"\n\s*\n+", "\n\n", self.block.strip()) + "\n"
        logging.info(f"ブロック変換成功（MDとして適切な改行）")
        return text
