class Member:
    """a member of a school"""

    def __init__(self, name, email):
        print("Initializing member")
        self.name = name
        self.email = email

    def __str__(self):
        member_string = "{}\n{}".format(self.name,
                                        self.email)
        return member_string


class Teacher(Member):
    """teacher at school"""
    def __init__(self, name, email, faculty_id):
        print("Initializing teacher")
        super().__init__(name, email)
        self.faculty_id = faculty_id
        self.courses_teaching = []

    def __str__(self):
        member_str = super().__str__()
        member_str += "\n{}".format(self.faculty_id)
        if len(self.courses_teaching) > 0:
            member_str += "\nClasses Teaching: "
            for c in self.courses_teaching:
                member_str += c + ", "
        return member_str

    def add_class(self, class_name):
        self.courses_teaching.append(class_name)


class Student(Member):

    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
        self.classes_enrolled = list()
        self.transcript = dict() #maps from classname to letter grade

    def __str__(self):
        student_str = super().__str__()
        student_str += "\n{}".format(self.student_id)
        student_str += "\nClasses:\n"
        for c in self.classes_enrolled:
            student_str += "\t{}\n".format(c)
        student_str += "\nTranscript:"
        for k,v in self.transcript.items():
            student_str += "\n\t{} : {}".format(k,v)
        student_str += "\nGPA = {}".format(self.compute_gpa())
        return student_str

    def add_class(self, class_name):
        self.classes_enrolled.append(class_name)

    def add_class_grade(self, class_name, letter_grade):
        self.transcript[class_name] = letter_grade

    def letter_to_number(self, letter):
        if letter == "A":
            return 4.0
        elif letter == "B":
            return 3.0
        elif letter == "C":
            return 2.0
        elif letter == "D":
            return 1.0
        else:
            return 0.0

    def compute_gpa(self):
        gpa_sum = 0
        for c, g in self.transcript.items():
            gpa_sum += self.letter_to_number(g)
        return gpa_sum / len(self.transcript)




#code to test classes
def main():
    bob = Member("Bob Baggins", "bb@gmail.com")
    print(bob)
    daniel = Teacher("Daniel B.", "dsbrown@something.com", 123)
    print(daniel)
    daniel.add_class("Math")
    daniel.add_class("Sleeping 101")
    print(daniel)
    print("-------")
    bill = Student("Bill Bunny", "bbunny@bunny.com", 1345)
    bill.add_class("Chemistry")
    bill.add_class("Biology")
    bill.add_class_grade("English", "B")
    bill.add_class_grade("Mermaid 101", "A")
    print(bill)

if __name__=="__main__":
    main()
