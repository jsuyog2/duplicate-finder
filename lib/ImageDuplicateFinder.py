# /lib/ImageDuplicateFinder.py

from difPy import dif
import shutil
import os
import sys

class ImageDuplicateFinder:
    """
    A class to find and handle duplicate images in a specified directory.

    Attributes:
        path (str): The path to the directory to scan for duplicate images.
        destination (str): The path where duplicate images will be moved.
        results (list): The list of duplicate images found.
        progress_bar (PySimpleGUI.ProgressBar): The progress bar to update during processing.
    """

    def __init__(self, path: str, progress_bar):
        """
        Initialize the ImageDuplicateFinder class with the specified path and progress bar.

        Args:
            path (str): The path to the directory to scan for duplicate images.
            progress_bar (PySimpleGUI.ProgressBar): The progress bar to update during processing.
        """
        super().__init__()
        self.path = path
        self.destination = os.path.join(path, "duplicate_images")
        self.results = []
        self.progress_bar = progress_bar
        self.search_duplicates()

    def search_duplicates(self):
        """
        Scan the specified directory for duplicate images and store the results.
        """
        search = dif(self.path)
        self.results = search.result
        self.move_duplicates()

    def move_duplicates(self):
        """
        Move the duplicate images to the destination directory and update the progress bar.
        """
        if self.results:
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)
            
            total_items = len(self.results)
            for idx, (original, matches) in enumerate(self.results.items(), start=1):
                original_location = matches.get('location')
                matched_files = matches.get('matches', {})
                
                # Check if matches are not empty
                if matched_files:
                    for match in matched_files.values():
                        match_location = match.get('location')
                        if match_location and os.path.isfile(match_location):
                            dest_path = self.get_destination_path(match_location)
                            shutil.move(match_location, dest_path)
                
                # Update progress bar
                self.update_progress_bar(idx, total_items)

    def get_destination_path(self, file_path):
        """
        Generate the destination path for a file based on its relative path to the root directory.

        Args:
            file_path (str): The path of the file to move.

        Returns:
            str: The destination path where the file will be moved.
        """
        relative_path = os.path.relpath(os.path.dirname(file_path), self.path)
        dest_folder = os.path.join(self.destination, relative_path)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        return os.path.join(dest_folder, os.path.basename(file_path))

    def update_progress_bar(self, current, total):
        """
        Update the progress bar with the current progress percentage.

        Args:
            current (int): The current item index.
            total (int): The total number of items to process.
        """
        progress = int(current / total * 100)
        self.progress_bar.update(current_count=progress)
    
    def get_results(self):
        """
        Format and return the results of the duplicate image search.

        Returns:
            str: A formatted string of duplicate images found.
        """
        if self.results:
            formatted_results = "Duplicate images found:\n"
            for original, matches in self.results.items():
                formatted_results += f"Original: {matches['location']}\n"
                formatted_results += f"Duplicates: {', '.join([match['location'] for match in matches['matches'].values()])}\n\n"
            return formatted_results
        else:
            return "No duplicate images found."
