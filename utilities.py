def get_source_image_directory_path(target_edition_name):
    import os
    path = os.path.join(target_edition_name, "images")
    if not os.path.isdir(path):
        # * the reason we need mkdir here is, when the directory is empty git avoids committing it and on the CI environment the lack of the directory may cause an error
        os.mkdir(path)
    return path

def get_destination_image_directory_path(target_edition_name):
    import os
    path = os.path.join("docs", "images_"+target_edition_name)
    if not os.path.isdir(path):
        # see: *
        os.mkdir(path)
    return path

def collect_content_directory_names():
    import os
    content_directory_prefix = "edition_"
    return [name for name in os.listdir(".") if os.path.isdir(name) and name.startswith(content_directory_prefix)]
