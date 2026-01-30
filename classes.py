class Paper:
    def __init__(self, name, assessmentTable):
        self.name = name
        
        self.categories = []
        tempList = []
        tempName = ""
        tempPercentage = ""
        firstFound = False

        for i in assessmentTable:
            if i[0] == 0:
                firstFound = True
                if len(tempList) > 0:
                    self.categories.append(Category(tempName, tempPercentage, tempList))
                
                tempName = i[1]
                tempPercentage = i[3]
                tempList = []

            elif firstFound:
                tempList.append(i)

class Category:
    def __init__(self, name, percentage, assessments):
        self.name = name
        self.percentage = percentage
        self.comment = ""

        if len(assessments[0]) == 1:
            self.comment = assessments.pop(0)

        self.assessments = []
        for i in range(0, len(assessments)):
            self.assessments.append(Assessment(assessments[i][0], assessments[i][1], assessments[i][2]))

class Assessment:
    def __init__(self, name, date, percentage):
        self.name = name
        self.date = date
        self.percentage = percentage

if __name__ == "__main__":
    from htmlParsing import *
    from webScraping import getHTML
    
    # Pass default value of ENGEN101-24A for testing purposes
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN111-24B%20%28HAM%29")
    # html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    html = getAssessmentTablehtml(html)
    tableList = getAssessmentTableList(html)

    newPaper = Paper("ENGEN101-24A", tableList)

    print(newPaper.categories[0].comment)
    print(newPaper.categories[1].name)