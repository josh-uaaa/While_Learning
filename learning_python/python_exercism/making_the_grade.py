def round_scores(student_scores):
    rounded_scores = []
    while student_scores:
        rounded_scores.append(round(student_scores.pop(0)))

    return rounded_scores

def count_failed_students(student_scores):
    failed_count = 0
    while student_scores:
        curr_student_score = student_scores.pop()
        if curr_student_score <= 40:
            failed_count += 1

    return failed_count

def above_threshold(student_scores, threshold):
    above_threshold_scores = []
    while student_scores:
        curr_student_score = student_scores.pop(0)
        if curr_student_score >= threshold:
            above_threshold_scores.append(curr_student_score)

    return above_threshold_scores

def letter_grades(highest):
    lower_threshold_scores = []
    score_increment = (highest - 40) // 4
    for score in range(41, highest, score_increment):
        lower_threshold_scores.append(score)

    return lower_threshold_scores

def student_ranking(student_scores, student_names):
    student_rank_list = []
    for index, student in enumerate(student_names):
        curr_student_score = student_scores[index]
        student_string = f"{index + 1}. {student}: {curr_student_score}"
        student_rank_list.append(student_string)

    return student_rank_list

def perfect_score(student_info):
    perfect_score_list = []
    while student_info:
        curr_student_info = student_info.pop(0)
        if 100 in curr_student_info:
            perfect_score_list.extend(curr_student_info)
            break

    return perfect_score_list