# takes html of a course outline webpage and returns section with table of assessments
def getAssessmentTablehtml(html):
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

# Takes html of assessment table from course outline and puts it in a tkinter window
def getAssessmentTableList(html):

    # turn html into a single string with indentation removed
    for i in range(len(html)):
        html[i] = html[i].strip()
    html = "".join(html)

    output = []
    subOutput = []
    foundEntry = False
    entryStarted = False
    entryString = ""
    subtags = 0
    
    # iterate through every character in html
    for i in range(len(html)):

        # if <td> or <th> tag has been opened but not closed
        if foundEntry and not entryStarted:

            # check for closing of tag
            if html[i] == ">":
                entryStarted = True
                continue

        # if in text portion of entry
        if entryStarted:

            # check for closing tag
            if html[i:i+4] == "</td" or html[i:i+4] == "</th":

                # populate table with entry
                subOutput.append(entryString)

                # reset variables
                entryString = ""
                foundEntry = False
                entryStarted = False

                continue
            
            # if tag opened inside of text section (for example, <em>) TODO: sense and bold/italicise appropriately
            if html[i] == "<":
                subtags += 1

            # if tag inside of text section closed
            if html[i] == ">":
                subtags -= 1
                continue

            # add character to text string unless inside of extra tag
            if subtags == 0:
                entryString = entryString + html[i]

        # if new table row is created
        if html[i:i+3] == "<tr":
            if len(subOutput) > 0:
                output.append(subOutput)
            subOutput = []
            
            if html[i:i+33] == r'<tr class=\"assessmentCategory\">':
                    subOutput.append(0)

        # if new data intry is found
        if html[i:i+3] == "<td" or html[i:i+3] == "<th":
            foundEntry = True
    
    return output

if __name__ == "__main__":
    from webScraping import getHTML
    
    # Pass default value of ENGEN101-24A for testing purposes
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    html = getAssessmentTablehtml(html)
    tableList = getAssessmentTableList(html)

    for i in tableList:
        print(i)

