if __name__ == "__main__":
  # TODO: correct each editions' directory names and call makeNewsletter.py with them
  import os
  with open(os.path.join("docs", "test.html"), "w") as o:
    o.write("<html><head><title>Test</title></head><body>It worked!!!</body></html>")
