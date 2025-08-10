import shutil
from pathlib import Path
import logging


class BlockExtractor:
    def __init__(self, mdpath: Path) -> None:
        self.mdpath: Path = mdpath
        with self.mdpath.open("r", encoding="utf-8") as f:
            self.text = f.read()
        self.lines = self.text.splitlines(keepends=True)

    def get_blocks(self):
        """
        Markdownテキストから、--- に囲まれた中身だけを順に yield する。
        """
        in_block = False
        block = ""

        for line in self.lines:
            if line.strip() == "---":
                if in_block:
                    # 終了 --- に到達、ブロック確定
                    yield block
                    logging.info(f"ブロックを抽出しました")
                    block = ""
                else:
                    # 開始 --- に到達、次から記録開始
                    in_block = True
            elif in_block:
                block += line
        if block:
            # 最後のブロックが終了 --- で終わっていない場合も考慮
            logging.info(f"最後の不完全なブロックを抽出しました")
            yield block
