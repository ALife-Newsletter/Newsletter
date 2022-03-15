import markdown
import os, shutil
import re
import argparse

if __name__ == "__main__":
    # Part I -- configure and validate the script from parameters
    parser = argparse.ArgumentParser(description="Create a newsletter html")
    parser.add_argument("directory", metavar="directory", type=str,
                        help="directory with the newsletter contents")
    target = (parser.parse_args()).directory

    if not os.path.isdir(target):
        raise ValueError("Can't find directory {}".format(target))


    # Part II -- generate the newsletter from the md files
    text = []

    files = os.listdir(target)
    files.sort()

    for filename in files:
        if filename.endswith(".md"):
            if filename.startswith("00"):
                with open(os.path.join(target, filename), "r") as f:
                    opening = f.read()
            else:
                with open(os.path.join(target, filename), "r") as f:
                    text.append(f.read())
    bodytext = "\n".join(text)

    md = markdown.Markdown(extensions=['toc'])
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
                                       '"https://alife-newsletter.github.io/Newsletter/images_{}/'.format(target))
    with open(os.path.join("docs", target+".html"), "w") as o:
        o.write(htmltext)

    # copying images
    source_image_dir = os.path.join(target, "images")
    dest_image_dir = os.path.join("docs", "images_"+target)

    if not os.path.isdir(dest_image_dir):
        os.mkdir(dest_image_dir)
    for file in os.listdir(source_image_dir):
        shutil.copyfile(os.path.join(source_image_dir, file),
                        os.path.join(dest_image_dir, file))

    print("done.")


# with open("edition_004_202202/AlifeJapanReport.md") as f:
#     print(markdown.markdown(f.read()))
