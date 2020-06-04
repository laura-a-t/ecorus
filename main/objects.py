from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        self._id = int(uuid4())

    def __hash__(self):
        return self._id

    def happyBirthday(self):
        self.age += 1

    def changeName(self, name: str):
        self.name = name


@dataclass
class Office:
    name: str
    peopleWorking: set = field(default_factory=set)

    def startWorkingFor(self, person: Person):
        self.peopleWorking.add(person)

    def finishedWorkingFor(self, person: Person):
        if person in self.peopleWorking:
            self.peopleWorking.remove(person)
        else:
            raise UnidentifiedEmployeeError('Employee with name %s does not work in this office' % person.name)


class UnidentifiedEmployeeError(Exception):
    pass


if __name__ == '__main__':
    print("3. Create an object of the class 'Office', named Ecorus")
    office = Office('Ecorus')
    print(office)
    print("4. Create 2 objects of that class (Eduardo and Laura)")
    laura = Person('Laura', 1143)
    eduardo = Person('Eduardo', 756)
    print(laura)
    print(eduardo)
    print("5. Make Eduardo and Laura start working for Ecorus")
    office.startWorkingFor(laura)
    office.startWorkingFor(eduardo)
    print(office)
    print("6. Make Eduardo finish working from Ecorus")
    office.finishedWorkingFor(eduardo)
    print(office)

