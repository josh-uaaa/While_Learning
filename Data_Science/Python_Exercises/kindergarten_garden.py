class Garden:
    diagram_encoding = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = sorted(students)
        self.assigned_plants = self.assign_plants(diagram)

    def plants(self, student):
        encoded_plants = self.assigned_plants[student]
        student_plants = []
        for plant in encoded_plants:
            student_plants.append(Garden.diagram_encoding[plant])
        return student_plants

    def assign_plants(self, diagram):
        assigned_plants = {}
        plants_diagram = [list(row) for row in diagram.split("\n")]

        student_i, curr_i, prev_i = 0, 2, 0
        while curr_i <= len(plants_diagram[0]):
            assigned_plants[self.students[student_i]] = plants_diagram[0][prev_i:curr_i] + plants_diagram[1][prev_i:curr_i]
            prev_i = curr_i
            curr_i += 2
            student_i += 1
        return assigned_plants