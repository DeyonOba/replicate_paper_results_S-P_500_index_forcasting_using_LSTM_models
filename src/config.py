from pathlib import Path

FILENAME = "HistoricalPrices.csv"
DATA_DIR = Path(__file__).resolve().parents[1].joinpath("data")
DATA_PATH = DATA_DIR.joinpath(FILENAME)
