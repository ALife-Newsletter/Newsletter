# How is the Artificial Life Newsletter Made?
By [Claus Aranha](https://scholar.social/@caranha) and [Mitsuyoshi Yamazaki](https://mitsuyoshi-yamazaki.github.io/)

Every two months, we put our heads together to bring this little slice
of Alife news to you. This is the process that we use.

Our teams meets once every month (two meetings per news letter). 

In the first meeting, we choose the contents of the next newsletter,
and assign these to each member - usually two or three items per
member. To choose the contents, we check [the
form](https://forms.gle/QpQ68xhvSMt4wiv89) with your contributions,
and also a big pile of interesting things that we find on the
internet. 

In this stage, we make heavy use of a [Trello](https://trello.com)
board, with a column for the big pile, one for the different items
that we choose for the newsletter, and another for done or rejected
items.

Over the next month, we work on the assigned items, writing them as
[Markdown](https://daringfireball.net/projects/markdown/) files. These
files are kept on the [Newsletter's Github
repository](https://github.com/ALife-Newsletter/Newsletter). Every
time a change is pushed to the repository, it is converted to the HTML
format that you know and love using python's [Markdown
Package](https://pypi.org/project/Markdown/). The script concatenates
the HTML from all markdown files together, and adds a static footer
and header, including the newsletter CSS style.

The second meeting happens about one week before the planned date of
the newsletter. We check which of the contributions were completed,
which have to be scrapped, and which need just a little bit more work
before release. We also fix the final release date of the Newsletter.

The day before the newsletter we give it a final check online, and
after everyone gives the OK, we prepare it for release. The final HTML
file is sent to everyone using MailJet, and a magic text file is added
to the github repository that tells the script to update the
newsletter RSS.

Looks complicated? A lot of this routine grew organically, as we
learned what worked and what didn't work for each edition of the
newsletter. We still have a lot of pain points to solve (the
Newsletter Mail service being probably the biggest one). If you have
any ideas or suggestions to improve our workflow, [send us a
message](https://forms.gle/QpQ68xhvSMt4wiv89)!
