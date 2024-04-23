from pathlib import Path
import os


PARENT_DIR = Path(__file__).parent.resolve().parent.parent
DATA_DIR = PARENT_DIR / 'data'
RAW_DATA_DIR = PARENT_DIR / 'data' / '00_raw'
INTERIM_DATA_DIR = PARENT_DIR / 'data' / '01_interim'
TRANSFORMED_DATA_DIR = PARENT_DIR / 'data' / '02_transformed'


if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(RAW_DATA_DIR).exists():
    os.mkdir(RAW_DATA_DIR)

if not Path(INTERIM_DATA_DIR).exists():
    os.mkdir(INTERIM_DATA_DIR)

if not Path(TRANSFORMED_DATA_DIR).exists():
    os.mkdir(TRANSFORMED_DATA_DIR)