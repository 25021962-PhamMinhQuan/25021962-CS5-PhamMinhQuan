# Phạm Minh Quân 25021962
# Nguyễn Việt Quang 25021955

students = []
student_index = {}


def add_student():
    global students, student_index
    student_id = input("Nhập ID học sinh: ")
    if student_id in student_index:
        print("ID đã tồn tại! Hãy dùng ID khác.\n")
        return

    name = input("Nhập tên học sinh: ")
    score = float(input("Nhập điểm: "))

    student = {"id": student_id, "name": name, "score": score}
    students.append(student)
    student_index[student_id] = student

    print("Đã thêm học sinh thành công!\n")


def search_student():
    global student_index
    student_id = input("Nhập ID học sinh cần tìm: ")
    student = student_index.get(student_id)

    if student:
        print(f"Tìm thấy: {student['name']} - Điểm: {student['score']}\n")
    else:
        print("Không tìm thấy học sinh.\n")


def display_all():
    global students
    if not students:
        print("📭 Chưa có dữ liệu học sinh.\n")
        return
    print("Danh sách học sinh:")
    for student in students:
        print(
            f"ID: {student['id']}, Tên: {student['name']}, Điểm: {student['score']}")
    print()


# Menu chính
while True:
    print("=== Classroom Data Manager ===")
    print("1. Thêm học sinh mới")
    print("2. Tìm học sinh theo ID")
    print("3. Hiển thị tất cả học sinh")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        display_all()
    elif choice == "4":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.\n")
