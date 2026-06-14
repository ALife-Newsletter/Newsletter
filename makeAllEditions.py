import os
from shutil import copyfile

from utilities import collect_content_directory_names
from makeNewsletter import make_newsletter
from makeIndexPage import makeIndexPage
from makeRSS import makeRSS, getDate


# This is the main script that generates the ALIFE Newsletter

def copyStaticFiles():
    copyfile("static/newsletter.css", "docs/newsletter.css")



if __name__ == "__main__":

    copyStaticFiles()    

    edition_names = collect_content_directory_names()


    for edition_name in edition_names:
        make_newsletter(edition_name)

    edition_names.reverse()    
    makeIndexPage(edition_names)

    
    makeRSS()
