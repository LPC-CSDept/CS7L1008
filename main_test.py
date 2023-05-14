import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = main.Student('James', '123 Ave', '555-555-1234', 1001, sc1)
    s2 = main.Student('Mary', '456 Ave', '555-555-9999', 1002, sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {main.Student.numofStudent}')
    print(f'Difference between s1 and s2 scores: {s1-s2}')

    print(s1 > s2)
    print(s1 < s2)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert (s1 > s2) == True
    assert (s1 < s2) == False
    assert (s1-s2) == 10.0

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())
