class BlockTransformer:
    def __init__(self, block: str):
        self.block = block
        self.lines = block.splitlines(keepends=True)
