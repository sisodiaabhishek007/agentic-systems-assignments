class StudentPerformance:
    
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            # Check if the list is empty
            if len(self.scores) == 0:
                raise ValueError
            
            # Using indexing to get first and last score
            difference = self.scores[-1] - self.scores[0]
            print(f"Difference between last and first score is: {difference}")

        except:
            print("No scores available to calculate difference")


# Example Input
scores = [55, 65, 75, 85]
student = StudentPerformance(scores)
student.score_difference()
