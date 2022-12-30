import os
from datetime import date, datetime
from utilities import collect_content_directory_names

rss_header = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
 <title>Artificial Life Newsletter</title>
 <link>https://alife-newsletter.github.io/Newsletter/</link>
 <description>The Artificial Life Newsletter Brings you the latest alife news!</description>
"""

rss_footer = """
</channel>
</rss>
"""


def getDate(edition):
    dateFile = os.path.join(edition,"release_date.dat")
    rdate = ""
    if os.path.exists(dateFile):
        with open(dateFile,"r") as f:
            dateText = f.readline()
            rdate = date(*[int(s) for s in dateText.split("-")])    
    return rdate

def getContents(edition):
    htmlFile = os.path.join("docs",edition+".html")
    appender = False
    contents = []
    with open(htmlFile,"r") as f:
        for l in f.readlines():
            if "<h1 " in l:
                appender = True
            if "</div>" in l:
                appender = False
            if appender:
                contents.append(l)
    return "\n".join(contents)

def makeTitle(edition):
    nmb = str(int(edition[8:]))
    if nmb[-1]=="1":
        nmb += "st"
    elif nmb[-1]=="2":
        nmb += "nd"
    elif nmb[-1]=="3":
        nmb += "rd"
    else:
        nmb += "th"    
    return f"The {nmb} edition of the Alife Newsletter"

def makeItem(edition):
    nDate = getDate(edition)
    if (nDate==""):
        return ""
    titleDate = nDate.strftime("%B %Y")
    pubDate = nDate.strftime("%d %b %Y 00:00:00 GMT")
    link = "https://alife-newsletter.github.io/Newsletter/"+edition+".html"

    item = []
    item.append(" <item>")
    item.append("  <title>"+makeTitle(edition)+", "+titleDate+"</title>")
    item.append("  <link>"+link+"</link>")
    item.append("  <guid>"+edition+"</guid>")
    item.append("  <pubDate>"+pubDate+"</pubDate>")
    item.append("<description><![CDATA[")
    item.append(getContents(edition))
    item.append("]]></description>")
    item.append(" </item>")
    return "\n".join(item)

def makeRSS():
    edition_names = collect_content_directory_names()
    edition_names.sort(reverse=True)

    with open(os.path.join("docs","RSS.xml"),"w") as f:
        f.write(rss_header)
        f.write(" <lastBuildDate>")
        f.write(datetime.now().strftime("%d %b %Y %X GMT"))
        f.write("</lastBuildDate>\n")
        for e in edition_names:
            f.write(makeItem(e))
        f.write(rss_footer)

if __name__ == "__main__":
    makeRSS()

