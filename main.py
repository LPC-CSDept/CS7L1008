
class Person:
    """
    ########################################
    Code Your Program here
    ########################################
    """


class Student(Person):
    numofStudent = 0

    def __str__(self):
        strval = f'Name: {self._name:>10} \t Address: {self.addr} \t Tel: {self.tel}'
        strval += f'\t Scores: '
        for i in range(len(self._scores)):
            strval += str(self._scores[i]) + '\t'
        return strval
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():

    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = Student('James', '123 Ave', '555-555-1234', 1001, sc1)
    s2 = Student('Mary', '456 Ave', '555-555-9999', 1002, sc2)
    print(s1)   # call the function __str__()
    print(s2)
    print(f'Total number of students: {Student.numofStudent}')  # it should be 2
    print(f'Difference between s1 and s2 scores: {s1-s2}')      # Expected value 10.0

    print(s1 > s2)  # True
    print(s1 < s2)  # False


if __name__ == '__main__':
    main()
