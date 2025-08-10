from pathlib import Path
import logging
import shutil


class WriteManager:

    def __init__(self, out_dir: Path) -> None:
        self.out_dir = out_dir
        self.temp_file = self.out_dir / "temp.txt"

    def try_make_temp_file(self) -> None:
        """
        一時ファイルを作成する。
        """
        try:
            self.temp_file.touch(exist_ok=True)
            logging.info(f"一時ファイル {self.temp_file.name} を作成しました。")
        except Exception as e:
            logging.exception(f"一時ファイルの作成に失敗しました: {e}")

    def try_write_temp_file(self) -> None:
        """
        一時ファイルに内容を書き込む。
        """
        try:
            with self.temp_file.open("w", encoding="utf-8") as f:
                f.write("This is check.")
            logging.info(f"一時ファイル {self.temp_file.name} に内容を書き込みました。")
        except Exception as e:
            logging.exception(f"一時ファイルへの書き込みに失敗しました: {e}")

    def try_remove_temp_file(self) -> None:
        """
        一時ファイルを削除する。
        """
        if self.temp_file.exists():
            try:
                self.temp_file.unlink()
                logging.info(f"一時ファイル {self.temp_file.name} を削除しました。")
            except Exception as e:
                logging.exception(f"一時ファイルの削除に失敗しました: {e}")

    def try_all(self) -> None:
        """
        一時ファイルの作成、書き込み、削除を一連で試す。
        """
        self.try_make_temp_file()
        self.try_write_temp_file()
        self.try_remove_temp_file()

    # def _initialize_dir(self, out_dir: Path) -> None:
    #     if out_dir.is_dir():
    #         shutil.rmtree(out_dir)
    #         out_dir.mkdir()

    # def _is_like_yml(self, block: str) -> bool:
    #     lines = block.splitlines(keepends=True)
    #     judgements = []
    #     for line in lines:
    #         if ":" in line:
    #             judgements.append(True)
    #         else:
    #             judgements.append(False)
    #     if all(judgements):
    #         return True
    #     else:
    #         return False

    # def write_each_blocks(self, out_dir: Path) -> None:
    #     """
    #     yeildされたブロックをファイルに書き込む。
    #     judge関数で形式を見極める。
    #     それぞれの関数でフォーマットする。
    #     """
    #     self._initialize_dir(out_dir)
    #     for index, block in enumerate(self.get_blocks()):
    #         block = collapse_empty_lines(block)
    #         out_file = out_dir / f"out_{(index + 1):02d}.md"
    #         with open(out_file, "w", encoding="utf-8") as f:
    #             if self._is_like_yml(block):
    #                 f.write("---\n")
    #                 f.write(block)
    #                 f.write("---")
    #             else:
    #                 f.write("<hr>\n\n")
    #                 f.write(block)
    #                 f.write("\n<hr>")
    #                 print(True)
