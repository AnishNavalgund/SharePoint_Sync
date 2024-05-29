import shutil
import logging

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_from_sharepoint(source, destination):
    if source and destination:
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            logging.info("Successfully copied from Sharepoint")
        except Exception as e:
            logging.error(f"Error during copying from Sharepoint: {e}")
    else:
        logging.error("Source or destination path not provided")

def export_to_sharepoint(source, destination):
    if source and destination:
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            logging.info("Successfully copied to Sharepoint")
        except Exception as e:
            logging.error(f"Error during copying to Sharepoint: {e}")
    else:
        logging.error("Source or destination path not provided")
