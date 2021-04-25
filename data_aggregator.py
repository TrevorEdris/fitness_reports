import math
import random
from constants import Columns, Labels


def aggregate(data):
    """

    :param data: list of lists, the rows and columns of the CSV file
    Example:
    [
        [
            'Back Squat', '3', '6', '7', '3', '185', '185', '185', '9', 'Sit back and down, 15 degree toe flare, derive your knees out laterally'
        ],
        [
            'Romanian Deadlift', '3', '10', '7', '2', '115', '165', '165', '8', "Maintain a neutral lower back, set your hips back, don't allow your spine to round"
        ]
    ]

    :returns: dict, the final aggregation
    Example:
    {
        "Back Squat": {
            "LSRPE": [9, 8, 8],
            "sets": [[185.0, 190.0, 195.0], [190.0, 190.0, 195.0], [195.0, 195.0, 200.0]],
            "averages": [190.0, 192.5, 197.5]
        },
        "Bench Press": {
            "LSRPE": [7, 9, 9]
            "sets": [[145.0, 145.0, 155.0], [155.0, 160.0, 160.0], [160.0, 165.0, 165.0]],
            "averages": [147.5, 157.5, 162.5]
        }
    }
    """
    aggregation = {}
    for row in data:
        # Ensure the exercise name is in the aggregation
        if row[Columns.EXERCISE_NAME.value] not in aggregation:
            aggregation[row[Columns.EXERCISE_NAME.value]] = {
                Labels.LSRPE: [],
                Labels.SETS: [],
                Labels.AVERAGES: []
            }

        if row[Columns.LSRPE.value] == '': # TODO: REMOVE THIS
            row[Columns.LSRPE.value] = random.randint(6, 10)

        if row[Columns.SET_1.value] == '': # TODO: REMOVE THIS
            row[Columns.SET_1.value] = random.randint(50, 200)
            row[Columns.SET_2.value] = random.randint(50, 200)
            row[Columns.SET_3.value] = random.randint(50, 200)

        if row[Columns.LSRPE.value] != '':
            aggregation[row[Columns.EXERCISE_NAME.value]][Labels.LSRPE].append(row[Columns.LSRPE.value])

        if row[Columns.SET_1.value] != '':
            set1 = float(row[Columns.SET_1.value])
            set2 = float(row[Columns.SET_2.value])
            set3 = float(row[Columns.SET_3.value])
            lifting_set = [set1, set2, set3]
            avg = round(sum(lifting_set) / len(lifting_set), 1)

            aggregation[row[Columns.EXERCISE_NAME.value]][Labels.SETS].append(lifting_set)
            aggregation[row[Columns.EXERCISE_NAME.value]][Labels.AVERAGES].append(avg)
    return aggregation
