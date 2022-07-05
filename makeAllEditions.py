from utilities import collect_content_directory_names

if __name__ == "__main__":
    from makeNewsletter import make_newsletter
    edition_names = collect_content_directory_names()
    for edition_name in edition_names:
        make_newsletter(edition_name)
