#!/usr/bin/python3
import menu
import exercises

class Worksheet:
    def __init__(self):
        self.exercises = []

    def generateWorksheet(self):
        # initialize the worksheet
        self.worksheet = ''

        # build the worksheet
        self.generateHead()

        # add exercises.
        # will want to add more functionality in here based on options passed
        # currently only does addition questions
        self.generateExercises()

        # end document
        self.generateFoot()

    def generateHead(self):
        self.worksheet += r"\documentclass{article}\$"\
            r"\setlength{\tabcolsep}{1px}\$"\
            r"\begin{document}\$"\
            r"\section*{Hello, and welcome to the worksheet!}\$"\
            r"Please record your name, class, and date below.\$\$"\
            r"\vspace{1em}\$"\
            r"\noindent\$"\
            r"Name: \underline{\hspace{7em}}\hfill\$"\
            r"Class: \underline{\hspace{7em}}\hfill\$"\
            r"Date: \underline{\hspace{7em}}\$"

        return {"status":"success"}

    def generateExercises(self):
        self.worksheet += r"\section*{Addition Questions}\$"\
            r"\begin{enumerate}\$"
        for exercise in self.exercises:
            self.worksheet += \
                r"\T\item\$"\
                    r"\T\T\begin{tabular}[t]{cr}\$"
            for index, operand in enumerate(exercise.operands):
                # [IDEA]
                # could be nice to refactor the operator presence
                # logic out to a function that takes the
                #   index, number of operands, and a decision structure
                # and/or possibly provides a lambda encompasing such logic
                if index < (len(exercise.operands)-1):
                    self.worksheet += \
                        r"\T\T\T&{}\\\$".format(operand)
                else:
                    self.worksheet += \
                        r"\T\T\T+&{}\\\$".format(operand)

            self.worksheet += \
                    r"\T\T\T\hline\$"\
                r"\T\T\end{tabular}\$"

        self.worksheet += r"\end{enumerate}\$"

    def generateFoot(self):
        self.worksheet += r"\end{document}"

if __name__ == "__main__":
    worksheet = Worksheet()
    #print("Welcome to the worksheet module!")

    for i in range(10):
        worksheet.exercises.append(exercises.Addition(3, 0, 10))

    #print("Generated Worksheet:")
    worksheet.generateWorksheet()

    print(worksheet.worksheet.replace(r'\$','\n').replace(r'\T','\t'))

    string = r"\documentclass"
    #print(string.replace(r'\$','\n'))
