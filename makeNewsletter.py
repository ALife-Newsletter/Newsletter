import markdown
from markdown.extensions.toc import TocExtension
import os, shutil
import re
import argparse

import sys
# in case the system default encoding is not utf-8: it may cause UnicodeEncodeError on Markdown.convert() or file.write()
if sys.getdefaultencoding() is not "utf-8":
    try:
        print("change encoding from {} to utf-8".format(sys.getdefaultencoding()))
        sys.setdefaultencoding("utf-8")
    except AttributeError:
        reload(sys) # I don't know why but this fixes "AttributeError: 'module' object has no attribute 'setdefaultencoding'"
        sys.setdefaultencoding("utf-8")
    except Exception as e:
        print("changing encoding failed: {}".format(e))


def make_newsletter(target_edition_name):
    if not os.path.isdir(target_edition_name):
        raise ValueError("Can't find directory {}".format(target_edition_name))


    # Part II -- generate the newsletter from the md files
    text = []

    files = os.listdir(target_edition_name)
    files.sort()

    for filename in files:
        if filename.endswith(".md"):
            if filename.startswith("00"):
                with open(os.path.join(target_edition_name, filename), "r") as f:
                    opening = f.read()
            else:
                with open(os.path.join(target_edition_name, filename), "r") as f:
                    text.append(f.read())
    bodytext = "\n".join(text)

    md = markdown.Markdown(extensions=[TocExtension(toc_depth=1)])
    htmlopen = md.convert(opening)
    md.reset()
    htmlbody = md.convert(bodytext)
    htmltoc = md.toc

    # Part 3 save the result in the publish directory
    with open(os.path.join("static", "header.html")) as f:
        htmlhead = f.read()

    with open(os.path.join("static", "footer.html")) as f:
        htmlfooter = f.read()

    html = [
    htmlhead,
    htmlopen,
    htmltoc,
    htmlbody,
    htmlfooter
    ]


    htmltext = "\n".join(html).replace('"images/',
                                       '"https://alife-newsletter.github.io/Newsletter/images_{}/'.format(target_edition_name))
    with open(os.path.join("docs", target_edition_name+".html"), "w") as o:
        o.write(htmltext)

    # copying images
    source_image_dir = os.path.join(target_edition_name, "images")
    dest_image_dir = os.path.join("docs", "images_"+target_edition_name)

    if not os.path.isdir(dest_image_dir):
        os.mkdir(dest_image_dir)
    for file in os.listdir(source_image_dir):
        shutil.copyfile(os.path.join(source_image_dir, file),
                        os.path.join(dest_image_dir, file))

    print("generating {} done.".format(target_edition_name))

if __name__ == "__main__":
    # Part I -- configure and validate the script from parameters
    parser = argparse.ArgumentParser(description="Create a newsletter html")
    parser.add_argument("directory", metavar="directory", type=str,
                        help="directory with the newsletter contents")
    target = (parser.parse_args()).directory

    make_newsletter(target)


# with open("edition_004_202202/AlifeJapanReport.md") as f:
#     print(markdown.markdown(f.read()))
