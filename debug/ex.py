from config.paths import OUT_DIR, SAMPLE_FILE
from src.blocksearcher import BlockSearch

bs = BlockSearch(SAMPLE_FILE)
bs.write_each_blocks(OUT_DIR)
