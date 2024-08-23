import os
import shutil
from DuplicateFinder import DuplicateFinder

class VideoDuplicateFinder:
    """
    A class to find and handle duplicate videos in a specified directory.

    Attributes:
        path (str): The path to the directory to scan for duplicate videos.
        destination (str): The path where duplicate videos will be moved.
        results (list): The list of duplicate videos found.
        progress_bar (PySimpleGUI.ProgressBar): The progress bar to update during processing.
    """

    def __init__(self, path: str, progress_bar):
        """
        Initialize the VideoDuplicateFinder class with the specified path and progress bar.

        Args:
            path (str): The path to the directory to scan for duplicate videos.
            progress_bar (PySimpleGUI.ProgressBar): The progress bar to update during processing.
        """
        super().__init__()
        self.path = path
        self.destination = os.path.join(path, "duplicate_videos")
        self.results = []
        self.progress_bar = progress_bar
        self.find_duplicates()

    def find_duplicates(self):
        """
        Scan the specified directory for duplicate videos and move them to the destination directory.
        """
        duplicate_finder = DuplicateFinder(self.path)
        duplicate_finder.find_dups()
        self.results = duplicate_finder.get_results()

        total_items = len(self.results)
        if total_items > 0:
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)

            for idx, result in enumerate(self.results, start=1):
                for item in result[1:]:  # Skip the first item (original)
                    if os.path.isfile(item):
                        dest_path = self.get_destination_path(item)
                        shutil.move(item, dest_path)
                # Update progress bar after processing each duplicate set
                self.update_progress_bar(idx, total_items)
        else:
            self.update_progress_bar(0, 1)  # Set progress to 100% if no duplicates are found

    def get_destination_path(self, file_path):
        """
        Generate the destination path for a video file based on its relative path to the root directory.

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
        Format and return the results of the duplicate video search.

        Returns:
            str: A formatted string of duplicate videos found.
        """
        if self.results:
            formatted_results = "Duplicate videos found:\n"
            for result in self.results:
                original = result[0]
                duplicates = result[1:]
                formatted_results += f"Original: {original}\nDuplicates: {', '.join(duplicates)}\n\n"
            return formatted_results
        else:
            return "No duplicate videos found."
