class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[len(self.scores) - 1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        sorted_scores = sorted(self.scores, reverse=True)
        if len(sorted_scores) < 3:
            return sorted_scores
        else:
            return sorted_scores[:3]