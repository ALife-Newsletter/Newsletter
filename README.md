# Newsletter
Task management &amp; content backup for ALife Newsletter

## Issues
- [August 2020](https://alife.org/newsletter-august-2020/)
- [October 2021](https://alife.org/newsletter-october-2021/)
- [December 2021](https://alife.org/december-2021-alife-newsletter/)
- [April 2022](https://alife.org/april-2022-alife-newsletter/)
- [June 2022]()
  - coming soon!

---

Issues published on GitHub Pages: https://alife-newsletter.github.io/Newsletter/

# for Repository Contributors
## TODO
- Improve the CSS of the automated generated newsletter
- Add the old newsletters here
- Automatically generate index.html
  - Or maybe not? Need a way to hide "in progress" editions
- Add permalink to each contribution
- Twitter bot to remind people to contribute / talk about past contributions?

## Branches
- main
  - The main branch we commit to.
- gh-pages
  - A branch for GitHub Pages. Only CI modify it. Do not manually commit to it.

## How to Use Scripts
Basically those scripts are self-explanatory, so `$ <script> -h` shows what arguments it accepts.

```sh
# makeNewsletter.py
# generates a static html for the specified edition newsletter
$ python makeNewsletter.py <edition_directory_name>

# makeNewEditionDirectories.py
# creates files and directories for a new newsletter issue
$ python makeNewEditionDirectories.py <new_edition_number>

# makeAllEditions.py
# CI uses this script
# generates static html files for all editions
$ python makeAllEditions.py
```

## How CI Works
### Generates static html files and publishes them to GitHub Pages
It works on GitHub Action and the workflow file is [.github/workflows/gh_pages_deploy.yml](.github/workflows/gh_pages_deploy.yml)

The action is triggered by pushing the main branch, and it generates all editions' static html files and publish them on GitHub Pages.