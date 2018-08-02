class Member:
    """a member of a university"""

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Teacher(Member):
    """teacher at school"""
    def __init__(self, name, email, faculty_id):
        super().__init__(name, email)
        self.faculty_id = faculty_id
        self.courses_teaching = []


#code to test classes
def main():


if __name__=="__main__":
    main()
