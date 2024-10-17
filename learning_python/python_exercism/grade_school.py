class School:
    def __init__(self):
        self.school = {}
        self.is_added = []

    def add_student(self, name, grade):
        if any(name in names_by_grade for names_by_grade in self.school.values()):
            self.is_added.append(False)
        else:
            if grade not in self.school:
                self.school[grade] = []
            self.school[grade].append(name)
            self.is_added.append(True)

    def roster(self):
        return sum([sorted(self.school[grade]) for grade in sorted(self.school.keys(), key=int)], [])

    def grade(self, grade_number):
        return sorted(self.school.get(grade_number)) if grade_number in self.school.keys() else []

    def added(self):
        return self.is_added