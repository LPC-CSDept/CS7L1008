import main


def test_main_1():

    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = main.Student('James', '123 Ave', '555-555-1234', 1001, sc1)
    s2 = main.Student('Mary', '456 Ave', '555-555-9999', 1002, sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {main.Student.numofStudent}')

    assert s1.name == 'James'
    assert s2.name == 'Mary'
    assert s1.scores == [100, 100, 100]
    assert s2.scores == [90, 90, 90]


def test_main_2():
    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = main.Student('James', '123 Ave', '555-555-1234', 1001, sc1)
    s2 = main.Student('Mary', '456 Ave', '555-555-9999', 1002, sc2)

    assert callable(s1.__str__) == True
    assert callable(s1.__sub__) == True
    assert callable(s1.__gt__) == True
    assert callable(s1.__lt__) == True
    assert (s1 > s2) == True
    assert (s1 < s2) == False
    print(f'Difference between s1 and s2 scores: {s1-s2}')
    assert (s1 - s2) == 10.0
