# ---------------- TASK 1 ----------------
def task1():
    print("------------------TASK 1------------------------------------")

    word = "java"
    with open("practise.txt", "r") as f:
        data = f.read()

    new_data = data.replace("pyhton", "java")
    print(new_data)

    if data.find(word) != -1:
        print("found")
    else:
        print("Not found")


# ---------------- TASK 2 ----------------
def check_for_line():
    print("---------------------Task 02------------------------------")

    word = "learning"
    line_no = 1

    with open("practise.txt", "r") as f:
        for line in f:
            if word in line:
                print(line_no)
                return
            line_no += 1

    print(-1)


# ---------------- TASK 3 ----------------
def task3():
    print("---------------------------Task 03--------------------------------")

    with open("name.txt", "r") as f:
        data = f.read()
        print(data)


# ---------------- TASK 4 ----------------
def task4():
    print("-----------------------Task 04-------------------------------")

    message = input("Enter the sentence: ")

    with open("name.txt", "w") as f:
        f.write(message)

    print("data added successfully")


# ---------------- TASK 5 ----------------
def task5():
    print("---------------------------Task 05-----------------------------------")

    with open("name.txt", "r") as f:
        print(f.read())


# ---------------- TASK 6 ----------------
def task6():
    print("-----------------------------Task 06------------------------------------")

    user = input("Enter names of 5 students: ")

    with open("student.txt", "w") as f:
        f.write(user)

    print("Student added successfully")


# ---------------- TASK 7 ----------------
def task7():
    print("----------------------------Task 07-------------------------------------")

    with open("student.txt", "r") as f:
        data = f.readlines()

    for student in data:
        print(student.strip())


# ---------------- TASK 8 ----------------
def task8():
    print("-------------------------------------Task 08----------------------------------------")

    count = 0

    with open("student.txt", "r") as f:
        for _ in f:
            count += 1

    print("Total lines:", count)


# ---------------- TASK 9 ----------------
def task9():
    print("-------------------------------------09----------------------------------------------")

    with open("student.txt", "w") as f:
        f.write("hey its me kami iam learning python from apna collage\n")
        f.write("iam also learning sql oop and others")

    print("Written successfully")


# ---------------- TASK 10 ----------------
def task10():
    print("-------------------------------Task 10------------------------------------------------")

    with open("student.txt", "r") as f:
        data = f.read()

    words = data.split()
    print("Total words:", len(words))


# ---------------- TASK 11 ----------------
def task11():
    print("----------------------------------Task 11------------------------------------------------")

    word = "python"

    with open("student.txt", "r") as f:
        data = f.read()

    if word in data:
        print("Found")
    else:
        print("Not found")


# ---------------- TASK 12 ----------------
def task12():
    print("----------------------------------Task 12--------------------------------------------------")

    with open("student.txt", "r") as f:
        data = f.read()

    print(data.upper())


# ---------------- TASK 13 ----------------
def task13():
    print("----------------------------------Task 13-------------------------------------------")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))

    with open("student_record.txt", "w") as f:
        f.write(f"Name: {name}\nAge: {age}\nMarks: {marks}")

    print("Successfully data added")


# ---------------- TASK 15 ----------------
def task15():
    print("--------------------------------------Task 15---------------------------------------------")

    while True:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        with open("student_record.txt", "a") as f:
            f.write(f"Name: {name}, Age: {age}, Marks: {marks}\n")

        choice = input("Add another student? (yes/no): ")

        if choice.lower() != "yes":
            break

    print("All records saved successfully")


# ---------------- MAIN MENU ----------------
if __name__ == "__main__":
    task1()
    check_for_line()
    task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    # task12()
    # task13()
    # task15()