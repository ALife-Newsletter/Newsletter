import markdown
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a newsletter html")
    parser.add_argument("directory", metavar="directory", type=str,
                        help="directory with the newsletter contents")
    directory = (parser.parse_args()).directory

    if not os.path.isdir(directory):
        raise ValueError("{} is not a directory".format(directory))

    text = []

    files = os.listdir(directory)
    files.sort()

    for filename in files:
        if filename.endswith(".md"):
            if filename.startswith("00"):
                with open(os.path.join(directory, filename), "r") as f:
                    opening = f.read()
            else:
                with open(os.path.join(directory, filename), "r") as f:
                    text.append(f.read())

    bodytext = "\n".join(text)

    md = markdown.Markdown(extensions=['toc'])
    htmlopen = md.convert(opening)
    md.reset()
    htmlbody = md.convert(bodytext)
    htmltoc = md.toc

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

    with open(os.path.join(directory, "newsletter.html"), "w") as o:
        o.write("\n".join(html))

    print("done.")


# with open("edition_004_202202/AlifeJapanReport.md") as f:
#     print(markdown.markdown(f.read()))
