#!/usr/bin/python3
import menu
import exercises
import subprocess

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

        # write the worksheet
        # [TODO]
        # - allow the user to specify the name and possibly the location of the file
        self.generatePDF()

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
        # [TODO]
        # - Check for exercise type and add heading indicating the type
        # - While we are still on that exercise type, add questions
        # - On new type, change the heading
        # - May want to allow the user to restart/keep the numbering on new exrecise type?
        #   - currently, it will restart

        currentExerciseType = None
        for exercise in self.exercises:
            # Let's store the old exercise type and
            # get the type of exercise we are currently working with

            if currentExerciseType is not None:
                previousExerciseType = currentExerciseType
            else:
                previousExerciseType = None
            currentExerciseType = type(exercise).__name__

            # Now we had better check and see if they are the same.
            if previousExerciseType is None:
                # We are at the start.  No need to close an enuerate clause
                # Let's just start a new section, and an enumerate clause
                self.worksheet += r"\section*{"+exercise.displayName+r" Questions}\$"\
                    r"\begin{enumerate}\$"
            elif previousExerciseType != currentExerciseType:
                # If they are different, we need to
                #   - close the enumerate
                #   - write a new section
                #   - open another enumerate (defaulting to new numbering)
                self.worksheet += r"\end{enumerate}\$\$"\
                    r"\section*{"+exercise.displayName+r" Questions}\$"\
                    r"\begin{enumerate}\$"

            # Now that we have got the sectioning/ question type changes out of the way,
            # let's add the question itself.
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
                        r"\T\T\T" +exercise.latexOperatorSymbol +r"&{}\\\$".format(operand)

            self.worksheet += \
                    r"\T\T\T\hline\$"\
                r"\T\T\end{tabular}\$"

        self.worksheet += r"\end{enumerate}\$"

    def generateFoot(self):
        self.worksheet += r"\end{document}"

    def generatePDF(self):
        # We need to replace our formatting tags.
        self.worksheet = self.worksheet.replace(r'\$','\n').replace(r'\T','\t')

        # will take a file name in the future,
        # currently, it's just a hard coded test file.
        with open("autoTemplate.tex","w") as f:
            f.write(self.worksheet)

        # with the worksheet written, let's run pdflatex
        subprocess.call(["pdflatex","autoTemplate.tex"])

if __name__ == "__main__":
    worksheet = Worksheet()
    #print(type(worksheet).__name__)
    #print("Welcome to the worksheet module!")

    for i in range(3):
        worksheet.exercises.append(exercises.Addition(3, 0, 10))
    for i in range(3):
        worksheet.exercises.append(exercises.Subtraction(3, 0, 10))
    for i in range(3):
        worksheet.exercises.append(exercises.Multiplication(3, 0, 10))
    for i in range(3):
        worksheet.exercises.append(exercises.Addition(3, 0, 10))

    #print("Generated Worksheet:")
    worksheet.generateWorksheet()

    #print(worksheet.worksheet.replace(r'\$','\n').replace(r'\T','\t'))

    string = r"\documentclass"
    #print(string.replace(r'\$','\n'))
