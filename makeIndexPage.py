import os
from shutil import copyfile
from makeRSS import getDate

indexHeader = """
<h1>What is this?</h1>

    <p>The Artificial Life Newsletter collects news about research,
    projects, events and media that are of interest to the Alife
      community.</p>

    <p>We publish a new edition roughly every two months, and
      distribute it in this website, as well as by e-mail to
      subscribers.</p>

    <p>In July, 2022, the newsletter received the <b>Exceptional
    Service Award</b> by the <a href="https://alife.org">International
    Society of Artificial Life (ISAL)</a>. Thank you!</p>

    <h1>I want to read the Newsletter!</h1>

    <p>You can use <a href="https://forms.gle/QpQ68xhvSMt4wiv89">this
    form to subscribe to the newsletter</a>, and receive a new e-mail
    every time we release a new edition. Please check your spam folder
      (specially if you use Gmail!).</p>

    <p>Alternatively, you can register our <a href="RSS.xml">RSS
    feed</a> to read the newsletter from the confort of your favorite
    RSS reader! (Claus
    recommends <a href="https://lzone.de/liferea/">Liferea</a>)</p>
    
    <p>You can also read past editions in the links below:</p>
    
    <ul>
"""

indexFooter = """
    </ul>

    <h1>I want to share my work in the Newsletter!</h1>
    
    <p>If you have an idea for something that should be in the next
    newsletter, please let us know
    through <a href="https://forms.gle/jv7FdtdbWVTaTFGd9">this
    form</a>! Contributions from students and young researchers are
    particularly welcome.</p>

    <p>You can also contact us on:</p>

<ul>
    <li><a href="https://github.com/ALife-Newsletter/Newsletter/issues">github</a></li>
    <li><a rel="me" href="https://fediscience.org/@alifenewsletter">Mastodon</a></li>
    <li><a rel="me" href="https://bsky.app/profile/alifenewsletter.bsky.social">Blue Sky</a></li>
    </ul>

    <p>The Alife Newsletter welcomes anything that might be
    interesting to Alifers: Programs, Papers, Experiments, Videos,
    Art, Events, Opinions, Book Reviews, etc. Surprise us!</p>

    <p>If you want to send a fully formed contribution, it would be
    great if it was formatted in Markdown, and under 500 words. Lots
    of images and links are welcome! Think bulletin board, not
    magazine. Check the github link above for examples.</p>
    
    <h1>Who makes this newsletter anyway?</h1>
    
    <p>This Newsletter is organized by volunteer editors. The current
    editorial body is <a rel="me" href="https://lanasina.github.io/">Lana</a>, 
    <a rel="me" href="http://imytk.co.uk/">Imy</a>,
    <a rel="me" href="https://mitsuyoshi-yamazaki.github.io">Mitsuyoshi</a>, <a rel="me" href="https://scholar.social/@caranha">Claus</a>, Gabriel,
    and Martha.</p>
  </div>
"""




def makeEditionLink(edition):
    rdate = getDate(edition)
    if rdate == "":
        return None

    numbersuffix = ["st","nd","rd","th"]
    number = int(edition.split("_")[1])

    text = [
        "<li>",
        "<a href=\""+edition+".html\"\>",
        str(number) + numbersuffix[min((number-1)%10, 3)],
        "Edition,",
        rdate.strftime("%B %Y"),
        "</a></li>",
    ]
    
    return " ".join(text)
    
def makeIndexPage(editions):
    # Adding static data (header, footer, index text
    with open(os.path.join("static", "header.html")) as f:
        htmlhead = f.read()

    with open(os.path.join("static", "footer.html")) as f:
        htmlfooter = f.read()

    editionlist_raw = [makeEditionLink(edition) for edition in editions]
    editionlist = [ _ed for _ed in editionlist_raw if _ed != None ]

    html = [
        htmlhead,
        indexHeader,
        "\n".join(editionlist),
        indexFooter,
        htmlfooter,
    ]
    
    htmltext = "\n".join(html)
    
    # Finally: writing HTML file
    with open(os.path.join("docs", "index.html"), "w") as o:
        o.write(htmltext)
