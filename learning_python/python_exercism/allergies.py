class Allergies:
    allergy_items = {'cats': 128, 'pollen': 64, 'chocolate': 32, 'tomatoes': 16, 'strawberries': 8, 'shellfish': 4, 'peanuts': 2, 'eggs': 1}

    def __init__(self, score):
        self.score = score
        self.allergy_list = self.determine_allergies(score)

    def allergic_to(self, item):
        if item in self.allergy_list:
            return True
        return False

    @property
    def lst(self):
        return list(reversed(self.allergy_list))

    def determine_allergies(self, score):
        allergy_list = []
        while self.score > 256:
            self.score -= 256
        for item, value in self.allergy_items.items():
            if self.score >= value:
                allergy_list.append(item)
                self.score -= value
        return allergy_list