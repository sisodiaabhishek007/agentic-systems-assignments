class StudentScores:
    
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            # Check if scores are less than 2
            if len(self.scores) < 2:
                raise ValueError
            
            # Using negative indexing to get last two scores
            highest = max(self.scores[-2:])
            print(f"Highest score among last two is: {highest}")

        except:
            print("Not enough scores to find highest value")


# Example Input
scores = [45, 67, 89, 72]
student = StudentScores(scores)
student.highest_last_two()
