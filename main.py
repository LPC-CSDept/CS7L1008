
class Person:
    def __init__(self, name, addr, tel):
        self.name = name
        self.addr = addr
        self.tel = tel

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, addr):
        self._addr = addr

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, tel):
        self._tel = tel


class Student(Person):
    numofStudent = 0
    ########################################
    # Code your program here
    ########################################

    def __str__(self):
        strval = f'Name: {self._name:>10} \t Address: {self.addr} \t Tel: {self.tel}'
        strval += f'\t Scores: '
        for i in range(len(self._scores)):
            strval += str(self._scores[i]) + '\t'
        return strval


def main():

    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = Student('James', '123 Ave', '555-555-1234', 1001, sc1)
    s2 = Student('Mary', '456 Ave', '555-555-9999', 1002, sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {Student.numofStudent}')
    print(f'Difference between s1 and s2 scores: {s1-s2}')

    print(s1 > s2)
    print(s1 < s2)


if __name__ == '__main__':
    main()
