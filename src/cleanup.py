from pathlib import Path
import shutil
import logging


class Cleanupper:
    """出力ディレクトリを初期化（削除→作成）する。"""

    def __init__(self, out_dir: Path) -> None:
        self.out_dir = out_dir

    def remove_out_dir(self) -> None:
        """
        出力ディレクトリを削除
        """
        if self.out_dir.exists():
            try:
                shutil.rmtree(self.out_dir)
                logging.info(f" {self.out_dir.name} を削除しました。")
            except Exception as e:
                logging.exception(f" {self.out_dir.name} の削除に失敗しました: {e}")

    def create_out_dir(self) -> None:
        """
        出力ディレクトリをサイド作成
        """
        try:
            self.out_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f" {self.out_dir.name} を作成しました。")
        except Exception as e:
            logging.exception(f" {self.out_dir.name} の作成に失敗しました: {e}")

    def cleanup(self) -> None:
        """
        出力ディレクトリを初期化する。
        """
        logging.info(f" {self.out_dir.name} を初期化します。")
        self.remove_out_dir()
        self.create_out_dir()
        logging.info(f" {self.out_dir.name} の初期化が完了しました。")
