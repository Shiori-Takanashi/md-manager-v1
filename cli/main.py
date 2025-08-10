# cli/main.py
from src.extract import BlockExtractor

from src.transform import BlockTransformer

# from src.judge import BlockJudgement
from src.cleanup import Cleanupper

from src.write import WriteManager

from config.paths import SAMPLE_FILE, OUT_DIR

import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def main():
    out_dir = OUT_DIR  # 共通の Path 変数を作る

    # 出力ディレクトリの初期化
    Cleanupper(out_dir).cleanup()

    # 一時ファイルの作成・削除テスト
    wm = WriteManager(out_dir)
    wm.try_all()

    ex = BlockExtractor(SAMPLE_FILE)
    for index, block in enumerate(ex.get_blocks()):
        file_name = f"block_{(index + 1):03d}.md"
        file_path = out_dir / file_name

        # ブロックの変換処理
        tf = BlockTransformer(block)
        # マークダウンとして適切な改行に変更
        block = tf.collapse_empty_lines()
        try:
            with file_path.open("w", encoding="utf-8") as f:
                f.write(block)
            logging.info(f"ブロックの書き込み成功: {file_name}")
        except Exception as e:
            logging.error(f"ブロックの書き込みに失敗しました: {e}")


if __name__ == "__main__":
    main()
