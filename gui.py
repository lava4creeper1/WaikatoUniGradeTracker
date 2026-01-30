import tkinter as tk

returnValues = []
numFields = 2

# Draws main GUI for class submission page
# returns string
def drawMainGUI(colourFile):

    # Callback function to extract text from entry boxes and close tk window
    def submit():
        global returnValues
        for i in range(numFields):
            returnValues.append(linkVars[i].get())

        root.destroy()
    
    colours = extractColours(colourFile)

    # Create tkinter window
    root = tk.Tk()
    root.configure(background=colours[0])

    # Create label to be title for window
    title = tk.Label(root, text="Enter a classname in the format 'ENGEN101-24A'", padx=20, pady=20, background=colours[0], foreground=colours[4])
    title.grid(row=0, column=0)

    linkVars = []
    linkEntries = []

    # Create variable number of text entry boxes
    for i in range(numFields):

        linkVars.append(tk.StringVar(master=root, value=""))

        linkEntries.append(tk.Entry(root, width=50, background=colours[1], textvariable=linkVars[i]))
        linkEntries[i].grid(row=i + 1)

    # Create button to submit classnames and close window
    submitButton = tk.Button(root, text="Submit", width=42, bg=colours[2], command=submit)
    submitButton.grid(row=1 + numFields)

    tk.mainloop()

    return returnValues

# Takes file of colour codes and extracts into a list
def extractColours(colourFile):

    # Extract list of colours from passed file for drawing gui
    with open(colourFile) as file:
        colours = file.readlines()
        for colour in range(len(colours)):
            colours[colour] = colours[colour].strip("\n")

    return colours

# Takes html of assessment table from course outline and puts it in a tkinter window
def drawAssessmentTable(colourFile, papers):

    colours = extractColours(colourFile)

    for paper in papers:

        # create tkinter window
        root = tk.Tk()
        root.configure(background=colours[0])
        root.title(paper.name)

        row = 0


        for category in paper.categories:
            heading = tk.Label(root, text=category.name, bg=colours[0])
            heading.grid(row=row, column=0)

            percentage = tk.Label(root, text=category.percentage, bg=colours[0])
            percentage.grid(row = row, column=2)
            row += 1

            if category.comment != "":
                commentName = tk.Label(root, text=category.comment, bg=colours[0])
                commentName.grid(row=row, column=0, columnspan=3)
                row += 1

            for assessment in category.assessments:
                assessmentName = tk.Label(root, text=assessment.name, bg=colours[0])
                assessmentName.grid(row=row, column=0)

                assessmentDate = tk.Label(root, text=assessment.date, bg=colours[0])
                assessmentDate.grid(row=row, column=1)

                assessmentPercentage = tk.Label(root, text=assessment.percentage, bg=colours[0])
                assessmentPercentage.grid(row=row, column=2)
                row += 1


        tk.mainloop()

if __name__ == "__main__":
    from webScraping import getHTML
    from htmlParsing import *
    from classes import *
    
    # Pass default value of ENGEN101-24A for testing purposes
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    tablehtml = getAssessmentTablehtml(html)
    tableList = getAssessmentTableList(tablehtml)
    newPaper = Paper("ENGEN101-24A", tableList)

    drawAssessmentTable("colours.txt", [newPaper])