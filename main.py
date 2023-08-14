# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам
# для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы.")
        setattr(instance, self._name, value)


class Student:
    first_name = NameDescriptor()
    middle_name = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self._grades = {}
        self._test_results = {}
        self._subjects = []
        self.read_csv()

    def read_csv(self):
        with open('file.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';').__next__()
            for i in reader:
                self._subjects.append(i)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def add_grade(self, subject, grade):
        if subject not in self._subjects:
            raise ValueError('Такого предмета нет!')
        if not 1 < grade < 6:
            raise ValueError('Такой оценки не существует!')
        if subject not in self._grades:
            self._grades[subject] = [grade]
        else:
            val = self._grades[subject]
            val.append(grade)
            self._grades[subject] = val

    def add_test_result(self, subject, test_res):
        if subject not in self._subjects:
            raise ValueError('Такого предмета нет!')
        if not -1 < test_res < 101:
            raise ValueError('Такого балла не существует!')
        if subject not in self._test_results:
            self._test_results[subject] = [test_res]
        else:
            val = self._test_results[subject]
            val.append(test_res)
            self._test_results[subject] = val
            print(self._test_results)

    def average_of_grade(self, subject=None):
        result = 0
        count = 0
        if subject:
            if subject not in self._subjects:
                raise ValueError('Такого предмета нет!')
            result = sum(self._grades[subject])
            count = len(self._grades[subject])
        else:
            for i in self._grades.values():
                result += sum(i)
                count += len(i)
        return (round(result/count, 2))

    def average_of_test(self, subject=None):
        result = 0
        count = 0
        if subject:
            if subject not in self._subjects:
                raise ValueError('Такого предмета нет!')
            result = sum(self._test_results[subject])
            count = len(self._test_results[subject])
        else:
            for i in self._test_results.values():
                result += sum(i)
                count += len(i)
        return (round(result / count, 2))



st1 = Student('Иванов', 'Иван', 'Иванович')
st1.add_grade('Математика', 3)
st1.add_grade('Математика', 4)
st1.add_grade('Математика', 2)
st1.add_grade('История', 4)
st1.add_grade('История', 2)
st1.add_grade('История', 4)
# st1.add_grade('Русский', 4)
print(st1.average_of_grade())
print(st1.average_of_grade('Математика'))