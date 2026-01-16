def getAssessmentTable(html):
    startIndex = -1
    endIndex = -1

    for i in range(len(html)):
        if startIndex < 0:
            if "<!-- Assessments -->" in html[i]:
                startIndex = i
        else:
            if "</div>" in html[i]:
                endIndex = i
                break
    
    assessmentTable = html[startIndex:endIndex + 1]

    return assessmentTable

if __name__ == "__main__":
    from webScraping import getHTML
    
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    getAssessmentTable(html)

