from gui import *
from webScraping import *
from htmlParsing import *

coloursFile = "colours.txt"
urlFormat = "https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/{}%20%28HAM%29"

# Get classname list in format ENGEN101-26A
classNames = drawMainGUI(coloursFile)

# Iterate through classnames 
for className in classNames:
    # Put classname into url format to find url for specific classes course outline
    url = urlFormat.format(className)

    # Get html of course outline in format of one list entry for one line
    html = getHTML(url)

    # Get only portion of html with assessment table
    tableHTML = getAssessmentTable(html)

    # Create GUI displaying assessments table  
    drawAssessmentTable(coloursFile, tableHTML)

