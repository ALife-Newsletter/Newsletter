def collect_content_directory_names():
    import os
    content_directory_prefix = "edition_"
    return [name for name in os.listdir(".") if os.path.isdir(name) and name.startswith(content_directory_prefix)]

if __name__ == "__main__":
    raise ValueError("test")
    from makeNewsletter import make_newsletter
    edition_names = collect_content_directory_names()
    for edition_name in edition_names:
        make_newsletter(edition_name)
