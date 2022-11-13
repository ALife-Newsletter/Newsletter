import os
import shutil
import argparse
from utilities import get_source_image_directory_path, collect_content_directory_names

template_directory_name = "template"

def copy_common_section_files(target_edition_name):
    results = []
    paths = [[os.path.join(template_directory_name, x), os.path.join(target_edition_name, x)] for x in os.listdir(template_directory_name)]
    for path in paths:
        shutil.copy(path[0], path[1])
        results.append("copied: {0}, {1}".format(path[0], path[1]))
    return results

def make_new_edition_directories(target_edition):
    if not isinstance(target_edition, int):
        raise ValueError("edition number should be an integer number")
    if target_edition < 1 or target_edition > 999:
        raise ValueError("edition number should be 0 < n < 1000")

    target_edition_name = "edition_{:03}".format(target_edition)
    if os.path.isdir(target_edition_name):
        raise ValueError("edition {:003} already has directories".format(target_edition))

    results = []

    os.mkdir(target_edition_name)
    results.append("created: {}".format(target_edition_name))

    image_source_directory_path = get_source_image_directory_path(target_edition_name)
    results.append("created: {}".format(image_source_directory_path))

    results.extend(copy_common_section_files(target_edition_name))

    print("\n".join(results))

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Create the new edition directories")
    parser.add_argument("edition number", metavar="edition number", type=int,
                        help="the next edition number")
    target_edition = vars(parser.parse_args())["edition number"]

    make_new_edition_directories(target_edition)
