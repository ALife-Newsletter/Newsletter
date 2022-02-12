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
            with open(os.path.join(directory, filename), "r") as f:
                text.append(f.read())
    bodytext = "\n".join(text)

    md = markdown.Markdown(extensions=['toc'])
    htmlbody = md.convert(bodytext)
    htmltoc = md.toc

    html = [
    "<html>",
    "<head><title>Alife Newsletter</title></head>",
    "<body>",
    htmltoc,
    htmlbody,
    "</body>",
    "</html>"
    ]

    with open(os.path.join(directory, "newsletter.html"), "w") as o:
        o.write("\n".join(html))

    print("done.")


# with open("edition_004_202202/AlifeJapanReport.md") as f:
#     print(markdown.markdown(f.read()))
