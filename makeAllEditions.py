from utilities import collect_content_directory_names
from makeNewsletter import make_newsletter
from makeRSS import makeRSS

# This is the main script that generates the ALIFE Newsletter


if __name__ == "__main__":
    edition_names = collect_content_directory_names()
    for edition_name in edition_names:
        make_newsletter(edition_name)
    makeRSS()
