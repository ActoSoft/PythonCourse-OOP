class Person:
    # Constructor
    def __init__(self, first_name, last_name, curp, email, age, height, nacionality='Mexicano'):
        self.first_name = first_name
        self.last_name = last_name
        self.curp = curp
        self.email = email
        self.age = age
        self.height = height
        self.nacionality = nacionality

    # Getters
    def get_first_name(self):
        return self.first_name

    # Setters
    def set_first_name(self, first_name):
        self.first_name = first_name

    def present_me(self):
        print(f'¡Hola! Mi nombre es: {self.first_name} {self.last_name}')
        print(f'Mi CURP es: {self.curp}')
        print(f'Actualmente tengo {self.age} años y soy {self.nacionality} de <3')
        print(f'Mido {self.height} mts. y mi correo para las nenas es {self.email}')
        print('Mucho gusto, para servirle a uste!')

class Student(Person):

    def __init__(self, id, career, semester, group, *args):
        super(Student, self).__init__(*args)
        self.id = id
        self.career = career
        self.semester = semester
        self.group = group

    def student_info(self):
        print(f'Mi matrícula es: {self.id}')
        print(f'Actualmente estudio {self.career}')
        print(f'Voy en {self.semester} semestre, en el grupo {self.group}')


def main():
    # person = Person('Martín', 'Melo Godínez', 'MEGM970321HHGLDR09', 'martin.melo.dev.97@gmail.com', 23, 1.64)
    # person.present_me()
    # print("##################")
    # person.set_first_name(input('Dame el nuevo nombre de la persona: '))
    # print(person.first_name) -> NOT
    # print('Nuevo nombre actualizado:', person.get_first_name())
    # print("#####################")
    # person.present_me()
    student = Student('ABCD1234', 'Ing', 3, 'A', 'Martín', 'Melo Godínez', 'MEGM970321HHGLDR09', 'martin.melo.dev.97@gmail.com', 23, 1.64)
    student.present_me()
    student.student_info()
    # student = Student(person, )
    # student.present_me()
main()