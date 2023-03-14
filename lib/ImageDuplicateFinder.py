from difPy import dif
import shutil
import os
import sys

class ImageDuplicateFinder:
    def __init__(self, path: str):
        super().__init__()
        search = dif(path)
        destination = path + "/duplicate"


        results = search.result
        x = len(results)
        if x > 0:
            if not os.path.exists(destination):
                os.mkdir(destination)
            for result in results:
                items = results[result]
                for item in items:
                    og = items['location']
                    matchs = items['matches']
                    for matches in matchs:
                        check_file = os.path.isfile(matchs[matches]['location'])
                        if check_file:
                            dest = shutil.move(matchs[matches]['location'], destination)
                            print("Destination path:", dest)