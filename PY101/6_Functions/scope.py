def elective_sub_grade(mark):
    threshold = 40

    mark = mark * 5
    return mark > threshold


def core_sub_grade(mark):
    return mark > threshold


mark = int(input("Enter your mark:"))

print(elective_sub_grade(mark))

print(core_sub_grade(mark))
# This will raise an error because 'threshold' is not defined in core_sub_grade's scope.
