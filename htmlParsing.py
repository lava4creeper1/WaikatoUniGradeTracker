# takes html of a course outline webpage and returns section with table of assessments
def getAssessmentTable(html):
    startIndex = -1
    endIndex = -1

    # Iterate through html looking for comment that says "Assessments" and the first end of a div after that
    for i in range(len(html)):
        if startIndex < 0:
            if "<!-- Assessments -->" in html[i]:
                startIndex = i
        else:
            if "</div>" in html[i]:
                endIndex = i
                break
    
    # Take slice of html including only table of assessments
    assessmentTable = html[startIndex:endIndex + 1]

    return assessmentTable


if __name__ == "__main__":
    from webScraping import getHTML
    
    # Pass default value of ENGEN101-24A for testing purposes
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    getAssessmentTable(html)

