import re
with open('README.md', 'r') as readFile:
  with open('urls.txt', 'w') as writeFile:
    strUrls = '\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(strUrls, readFile.read())
    for url in urls:
      link = url.replace("(","").replace(")","")
      regex = re.compile('http[s]?:\/\/(?:github|gitlab).com')
      if regex.search(link):
        writeFile.write(f'{link}\n')
      # go to each url
      # if the web page contains the message: "No results matched your search"
      # annoted the current url with "outdated" || checkbox or create an automated issue/notification to main contributor