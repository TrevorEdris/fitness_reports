from enum import Enum


class Labels:
    LSRPE = "LSRPE"
    SETS = "sets"
    AVERAGES = "averages"


class Columns(Enum):
    EXERCISE_NAME = 0
    SET_COUNT = 1
    REPS = 2
    RPE = 3
    REST = 4
    SET_1 = 5
    SET_2 = 6
    SET_3 = 7
    LSRPE = 8
    NOTES = 9
