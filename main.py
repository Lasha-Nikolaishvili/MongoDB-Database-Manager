from mongo_db import DatabaseManager
# from db import DatabaseManager as SQLManager


def main():
    database_manager = DatabaseManager()

    # Inserting students
    database_manager.add_data("students", student_id=501, name="Student1", surname="StudLast1", age=20,
                           advisor_id=1)
    database_manager.add_data("students", student_id=502, name="Student2", surname="StudLast2", age=21,
                           advisor_id=1)
    database_manager.add_data("students", student_id=503, name="Student3", surname="StudLast3", age=23,
                           advisor_id=3)
    database_manager.add_data("students", student_id=504, name="Student4", surname="StudLast4", age=19,
                           advisor_id=2)
    database_manager.add_data("students", student_id=505, name="Student5", surname="StudLast5", age=22,
                           advisor_id=4)
    database_manager.add_data("students", student_id=506, name="Student6", surname="StudLast6", age=20,
                           advisor_id=2)
    database_manager.add_data("students", student_id=507, name="Student7", surname="StudLast7", age=20,
                           advisor_id=2)
    database_manager.add_data("students", student_id=508, name="Student8", surname="StudLast8", age=22,
                           advisor_id=3)
    database_manager.add_data("students", student_id=509, name="Student9", surname="StudLast9", age=19)
    database_manager.add_data("students", student_id=510, name="Student10", surname="StudLast10", age=24,
                           advisor_id=1)
    #
    # # Inserting advisors
    database_manager.add_data("advisors", age=45, advisor_id=1, name="John", surname="Paul")
    database_manager.add_data("advisors", age=32, advisor_id=2, name="Anthony", surname="Roy")
    database_manager.add_data("advisors", age=66, advisor_id=3, name="Raj", surname="Shetty")
    database_manager.add_data("advisors", age=62, advisor_id=4, name="Sam", surname="Reeds")
    database_manager.add_data("advisors", age=28, advisor_id=5, name="Arthur", surname="Eastwood")
    #
    # # Inserting relations
    database_manager.add_data("student_advisor", student_id=501, advisor_id=1)
    database_manager.add_data("student_advisor", student_id=501, advisor_id=2)
    database_manager.add_data("student_advisor", student_id=501, advisor_id=3)
    database_manager.add_data("student_advisor", student_id=502, advisor_id=1)
    database_manager.add_data("student_advisor", student_id=503, advisor_id=3)
    database_manager.add_data("student_advisor", student_id=504, advisor_id=2)
    database_manager.add_data("student_advisor", student_id=504, advisor_id=3)
    database_manager.add_data("student_advisor", student_id=505, advisor_id=4)
    database_manager.add_data("student_advisor", student_id=506, advisor_id=2)
    database_manager.add_data("student_advisor", student_id=507, advisor_id=2)
    database_manager.add_data("student_advisor", student_id=508, advisor_id=3)
    database_manager.add_data("student_advisor", student_id=509)
    database_manager.add_data("student_advisor", student_id=510, advisor_id=1)

    # Displaying Table data:
    print('students:')
    for student in database_manager.load_data("students"):
        print(student)

    print('advisors:')
    for advisor in database_manager.load_data("advisors"):
        print(advisor)

    print('relations:')
    for student_advisor in database_manager.load_data("student_advisor"):
        print(student_advisor)

    # Displaying counts:
    print('Advisors with student count:')
    for count_object in database_manager.list_advisors_with_students_count(-1):
        print(count_object)

    print('Students with advisor count:')
    for count_object in database_manager.list_students_with_advisors_count(-1):
        print(count_object)

    # Updating a result:
    # database_manager.update("students", age=21, id=501)

    # Displaying search results:
    for entry in database_manager.search("students", age=21):
        print(entry)

    # Displaying relations with method:
    for entry in database_manager.get_existing_relations():
        print(entry)


if __name__ == '__main__':
    main()
