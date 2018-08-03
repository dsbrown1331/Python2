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




#code to test classes
def main():
    bob = Member("Bob Baggins", "bb@gmail.com")
    print(bob)
    daniel = Teacher("Daniel B.", "dsbrown@something.com", 123)
    print(daniel)
    daniel.add_class("Math")
    daniel.add_class("Sleeping 101")
    print(daniel)

if __name__=="__main__":
    main()
