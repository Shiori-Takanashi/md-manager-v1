import re


class BlockJudgement:
    def __init__(self, block: str) -> None:
        self.block = block
        self.lines = block.splitlines(keepends=True)

    def is_like_yml(self, lines: str) -> str:
        return "a"

    # def search_first_heading(self) -> bool:
    #     pattern = re.compile(r"^#\s(.+)", re.MULTILINE)
    #     lines = self.block.splitlines()
    #     for line in lines:
    #         if pattern.search(line):
    #             return True
    #     return False
