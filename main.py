from gui import *
from webScraping import *
from htmlParsing import *

coloursFile = "colours.txt"
urlFormat = "https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/{}%20%28HAM%29"

classNames = drawMainGUI(coloursFile)

for className in classNames:
    url = urlFormat.format(className)

    print(f"url: {url}")

    html = getHTML(url)

    tableHTML = getAssessmentTable(html)

    for i in tableHTML:
        print(i)
