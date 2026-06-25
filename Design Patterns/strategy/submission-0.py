class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    def __init__(self):
        self.age_filter = 18

    def apply(self, person:Person) -> bool:
        age = person.getAge()
        if age >= self.age_filter: 
            return True
        return False

class SeniorFilter(PersonFilter):
    def __init__(self):
        self.age_filter = 65

    def apply(self, person:Person) -> bool:
        age = person.getAge()
        if age >= self.age_filter: 
            return True
        return False

class MarriedFilter(PersonFilter):
    def apply(self, person:Person) -> bool:
        return person.isMarried()

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        cnt = 0
        for person in people:
            if self.filter.apply(person):
                cnt += 1
        return cnt
    
