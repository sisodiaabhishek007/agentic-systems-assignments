class StudentMarks:
    
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Check if marks are less than 3
            if len(self.marks) < 3:
                raise ValueError
            
            # Using negative indexing to get last three marks
            avg = sum(self.marks[-3:]) / 3
            print(f"Average of last 3 marks is: {avg}")

        except:
            print("Not enough marks to calculate average")


# Example Input
marks = [50, 60, 70, 80, 90]
student = StudentMarks(marks)
student.last_three_avg()
