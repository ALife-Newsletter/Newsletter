import markdown
from markdown.extensions.toc import TocExtension
import os, shutil
from datetime import datetime
from utilities import get_source_image_directory_path, get_destination_image_directory_path

def make_12days(day: int):
    """
    the content files should be formatted .md (markdown) and stored under 12_days_alife_2023/ directory.
    each content files are concated and converted into html file
    the main contents (1-12days contents) should be stored under 12_days_alife_2023/80_contents/ directory and named day_<day>.md like day_1.md, day_2.md, ...

    the directory structure should look like:
    - 12_days_alife_2023/
      - 00_foreword.md
      - 01_something.md
      - ...
      - 80_contents/ # the 80_ is sorting prefix
        - day_1.md
        - day_2.md
        - ...
        - day_12.md
      - 90_something.md
      - ...

    for testing:
    read comment in `if __name__ == "__main__":` scope
    """

    root_directory_name = "12_days_alife_2023"
    contents_directory_name = "80_contents"

    if not os.path.isdir(root_directory_name):
        raise ValueError(f"Can't find directory {root_directory_name}")


    text = []
    def read_markdownfile(filepath: str):
        with open(filepath, "r") as f:
            text.append(f.read())

    contents = os.listdir(root_directory_name)
    contents.sort()

    for content_name in contents:
        if content_name.endswith(".md"):
            filename = content_name
            if filename.startswith("00"):
                with open(os.path.join(root_directory_name, filename), "r") as f:
                    opening = f.read()
            else:
                read_markdownfile(os.path.join(root_directory_name, filename))

        elif content_name == contents_directory_name:
            for content_filepath in [os.path.join(contents_directory_name, f"day_{i + 1}.md") for i in range(day)]:
                read_markdownfile(os.path.join(root_directory_name, content_filepath))
            
    bodytext = "\n".join(text)

    md = markdown.Markdown(extensions=[TocExtension(toc_depth=1)])
    htmlopen = md.convert(opening)
    md.reset()
    htmlbody = md.convert(bodytext)
    htmltoc = md.toc

    # Part save the result in the publish directory
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


    htmltext = "\n".join(html).replace('"images/', '"https://alife-newsletter.github.io/Newsletter/images_{}/'.format(root_directory_name))

    # copying images
    source_image_dir = get_source_image_directory_path(root_directory_name)
    dest_image_dir = get_destination_image_directory_path(root_directory_name)

    for file in os.listdir(source_image_dir):
        if "newsletter_header" in file:
            print("Newsletter {} has a header file {}".format(root_directory_name, file))
            htmltext = htmltext.replace('images/alifenewshead.png',"images_{}/".format(root_directory_name)+file)
        shutil.copyfile(os.path.join(source_image_dir, file),
                        os.path.join(dest_image_dir, file))

        
    # writing HTML file
    with open(os.path.join("docs", root_directory_name+".html"), "w") as o:
        o.write(htmltext)
        
    print("generating {} done.".format(root_directory_name))


def get_day() -> int:
    now = datetime.now()
    if now.year != 2023:
        raise RuntimeError("out of range")
    if now.month != 12:
        raise RuntimeError("out of range")

    day = now.day - 13 # Dec 14th is the 1st day
    if day <= 0:
        raise RuntimeError("out of range")
    
    return day

if __name__ == "__main__":
    try:
        """
        if you want to test locally, put an arbitary integer value to `day` (example: `day = 3`)
        and call this script by `$ python3 12DaysAlife.py`
        """
        day = get_day()
        print(f"today is {day}th day!")
        make_12days(day)
    except:
        print(f"not in the 12days")