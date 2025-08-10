def decotate_to_heading(block: str) -> str:
    lines = block.splitlines(block, keepends=True)
    re_block = ""
    for line in lines:
        if line.startswith("#"):
            re_line = f"<hr>\n\n{line}\n"
