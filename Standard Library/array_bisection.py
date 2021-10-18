import bisect

break_points = [60, 70, 80, 90]
letter_grades = "FDCBA"
scores = [81, 68, 53, 91, 90, 82, 76, 71, 84]


def calcGrade(score):
    i = bisect.bisect(break_points, score)
    return letter_grades[i]


results = [calcGrade(score) for score in scores]
print(results)
