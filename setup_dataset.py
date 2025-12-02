import os
import logging
from pathlib import Path

# Configure logging (can be adjusted based on environment)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def setup_kaggle_credentials():
    """Check if Kaggle API credentials exist."""
    kaggle_json = Path.home() / '.kaggle' / 'kaggle.json'
    return kaggle_json.exists()


def download_dataset():
    """Download the Suicide Watch dataset from Kaggle."""
    if not setup_kaggle_credentials():
        logger.error("Kaggle API credentials not found")
        return False

    try:
        import kaggle
        kaggle.api.dataset_download_files(
            'nikhileswarkomati/suicide-watch',
            path='data/raw',
            unzip=True
        )
        return True
    except Exception as e:
        logger.error(f"Failed to download dataset: {e}")
        return False


def check_dataset():
    """Check if the dataset file exists."""
    dataset_path = Path('data/raw/Suicide_Detection.csv')
    return dataset_path.exists()


def main():
    """Set up the dataset directory structure and download if needed."""
    # Create directory structure
    data_dirs = ['data/raw', 'data/processed', 'data/splits']
    for dir_path in data_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    # Check and download dataset if needed
    if not check_dataset():
        if not download_dataset():
            logger.error("Dataset setup failed")
            return False

    return True


if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)