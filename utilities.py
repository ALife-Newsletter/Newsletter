def enforce_default_encoding():
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

def get_source_image_directory_path(target_edition_name):
    import os
    path = os.path.join(target_edition_name, "images")
    if not os.path.isdir(path):
        # ★ the reason we need mkdir here is, when the directory is empty git avoids committing it and on the CI environment the lack of the directory may cause an error
        os.mkdir(path)
    return path

def get_destination_image_directory_path(target_edition_name):
    import os
    path = os.path.join("docs", "images_"+target_edition_name)
    if not os.path.isdir(path):
        # see: ★
        os.mkdir(path)
    return path

def collect_content_directory_names():
    import os
    content_directory_prefix = "edition_"
    return [name for name in os.listdir(".") if os.path.isdir(name) and name.startswith(content_directory_prefix)]
