import shutil
import logging
from pathlib import Path

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_path_valid(path: Path, check_write_access=False) -> bool:
    """
    Check if the given path is valid and accessible.

    Args:
        path: The directory path to check as a Path object.
        check_write_access: If True, also check if the path is writable.
    
    Returns:
        bool: True if path is valid and accessible, False otherwise.
    """
    if check_write_access:
        return path.exists() and path.is_dir() and os.access(path, os.W_OK)
    return path.exists()

def copy_directory(source: Path, destination: Path, create_dest=False):
    """
    Attempts to copy directories from the source to the destination and logs the number of folders and files copied.

    Args:
        source: The source directory path as a Path object.
        destination: The destination directory path as a Path object.
        create_dest: If True, create the destination directory if it does not exist.
    """
    if not source.exists():
        logging.error(f"Source path {source} does not exist.")
        return
    
    if not destination.exists():
        if create_dest:
            destination.mkdir(parents=True, exist_ok=True)
        else:
            logging.error(f"Destination path {destination} does not exist and is not permitted to be created.")
            return
    
    num_folders = 0
    num_files = 0
    
    for item in source.rglob('*'):
        dest_path = destination.joinpath(item.relative_to(source))
        if item.is_dir():
            if not dest_path.exists():
                dest_path.mkdir(exist_ok=True)
                num_folders += 1
        else:
            shutil.copy2(item, dest_path)
            num_files += 1
    
    logging.info(f"Successfully copied {num_folders} folders and {num_files} files from {source} to {destination}")

def import_from_sharepoint(source: str, destination: str) -> None:
    """
    Copies files from SharePoint to the local directory and creates the destination folder if it does not exist.

    Args:
        source: The source directory path in SharePoint.
        destination: The destination directory path on the local machine.
    """
    source_path = Path(source)
    destination_path = Path(destination)
    if source_path and destination_path:
        if is_path_valid(source_path):
            copy_directory(source_path, destination_path, create_dest=True)
        else:
            logging.error("Invalid source path. Ensure the source path is valid and accessible.")
    else:
        logging.error("Source or destination path not provided")

def export_to_sharepoint(source: str, destination: str) -> None:
    """
    Copies files from the local directory to SharePoint but does not create a new folder in SharePoint.

    Args:
        source: The source directory path on the local machine.
        destination: The destination directory path in SharePoint.
    """
    source_path = Path(source)
    destination_path = Path(destination)
    if source_path and destination_path:
        if is_path_valid(source_path) and is_path_valid(destination_path):
            copy_directory(source_path, destination_path, create_dest=False)
        else:
            logging.error("Invalid path(s). Ensure both source and destination paths are valid and accessible.")
    else:
        logging.error("Source or destination path not provided")


