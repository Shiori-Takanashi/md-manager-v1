import shutil
from pathlib import Path


class BlockExtracter:
    def __init__(self, mdpath: Path) -> None:
        self.mdpath: Path = mdpath
        with self.mdpath.open("r", encoding="utf-8") as f:
            self.text = f.read()

    def get_blocks(self):
        """
        Markdownテキストから、--- に囲まれた中身だけを順に yield する。
        """
        lines = self.text.splitlines(keepends=True)
        in_block = False
        block = ""

        for line in lines:
            if line.strip() == "---":
                if in_block:
                    # 終了 --- に到達、ブロック確定
                    yield block
                    block = ""
                else:
                    # 開始 --- に到達、次から記録開始
                    in_block = True
            elif in_block:
                block += line

    def _initialize_dir(self, out_dir: Path) -> None:
        if out_dir.is_dir():
            shutil.rmtree(out_dir)
            out_dir.mkdir()

    def _is_like_yml(self, block: str) -> bool:
        lines = block.splitlines(keepends=True)
        judgements = []
        for line in lines:
            if ":" in line:
                judgements.append(True)
            else:
                judgements.append(False)
        if all(judgements):
            return True
        else:
            return False

    def write_each_blocks(self, out_dir: Path) -> None:
        """
        yeildされたブロックをファイルに書き込む。
        judge関数で形式を見極める。
        それぞれの関数でフォーマットする。
        """
        self._initialize_dir(out_dir)
        for index, block in enumerate(self.get_blocks()):
            block = collapse_empty_lines(block)
            out_file = out_dir / f"out_{(index + 1):02d}.md"
            with open(out_file, "w", encoding="utf-8") as f:
                if self._is_like_yml(block):
                    f.write("---\n")
                    f.write(block)
                    f.write("---")
                else:
                    f.write("<hr>\n\n")
                    f.write(block)
                    f.write("\n<hr>")
                    print(True)
