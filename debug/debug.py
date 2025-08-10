from config.paths import OUT_DIR, SAMPLE_FILE
from pathlib import Path
from collections import Counter

# 置換順序に注意：バックスラッシュ最初、改行は最後
REPLACEMENTS: list[tuple[str, str]] = [
    ("\\", "\\\\"),
    ("\r\n", "\\r\\n\n"),
    ("\r", "\\r"),
    ("\t", "\\t"),
    ("\b", "\\b"),
    ("\f", "\\f"),
    ("\v", "\\v"),
    # Unicode 不可視の代表例（見える記号に）
    ("\u00a0", r"\u00A0"),  # NBSP
    ("\u3000", r"\u3000"),  # 全角空白
    ("\u200b", r"\u200B"),  # ゼロ幅スペース
    ("\u200c", r"\u200C"),  # Zero Width Non-Joiner
    ("\u200d", r"\u200D"),  # Zero Width Joiner
    ("\u2060", r"\u2060"),  # Word Joiner
    ("\ufeff", r"\uFEFF"),  # BOM
    ("\n", "\\n\n"),
]


def define_out_path(base_dir: Path = OUT_DIR) -> list[Path]:
    base_dir.mkdir(parents=True, exist_ok=True)
    out_path01 = base_dir / "debug01.md"
    out_path02 = base_dir / "debug02.md"
    return [out_path01, out_path02]


def define_text(file_path: Path = SAMPLE_FILE) -> list[str]:
    simple_text = "aaaaa\nbbbbb\nccccc"
    loaded_text = file_path.read_text(encoding="utf-8")
    return [simple_text, loaded_text]


def visualize_and_report(text: str) -> tuple[str, Counter]:
    counts = Counter()
    for src, dst in REPLACEMENTS:
        n = text.count(src)
        if n:
            counts[src] += n
            text = text.replace(src, dst)
    return text, counts


def make_code_block(text: str) -> str:
    return f"```\n{text}\n```"


def output_simple_text() -> None:
    out_path, _ = define_out_path()
    text, _ = define_text()
    text, counts = visualize_and_report(text)
    text = make_code_block(text)  # コードブロック不要なら外す
    out_path.write_text(f"{counts}\n\n{text}", encoding="utf-8")


def output_loaded_text() -> None:
    _, out_path = define_out_path()
    _, text = define_text()
    text, counts = visualize_and_report(text)
    text = make_code_block(text)  # コードブロック不要なら外す
    out_path.write_text(f"{counts}\n\n{text}", encoding="utf-8")


output_simple_text()
output_loaded_text()
