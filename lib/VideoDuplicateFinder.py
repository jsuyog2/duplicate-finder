import os
import shutil
from DuplicateFinder import DuplicateFinder
import sys


class VideoDuplicateFinder:
    def __init__(self, path: str):
        destination = path + "/duplicate"

        duplicate_finder = DuplicateFinder(path)
        duplicate_finder.find_dups()
        res = duplicate_finder.get_results()
        x = len(res)
        if x > 0:
            if not os.path.exists(destination):
                os.mkdir(destination)
            for result in res:
                result.pop(1)
                for item in result:
                    check_file = os.path.isfile(item)
                    if check_file:
                        dest = shutil.move(item, destination)
                        print("Destination path:", dest)