from flask import Blueprint, request, current_app

student_bp = Blueprint('student', __name__)

# Create Student
@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return {"error": "Name is required"}, 400

    students = current_app.students

    new_student = {
        "id": len(students) + 1,
        "name": data['name']
    }

    students.append(new_student)
    return new_student, 201


# Get All Students
@student_bp.route('/students', methods=['GET'])
def get_students():
    return current_app.students, 200


# Update Student
@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    students = current_app.students

    for student in students:
        if student['id'] == id:
            student['name'] = request.get_json().get('name', student['name'])
            return student, 200

    return {"error": "Student not found"}, 404


# Delete Student
@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    students = current_app.students

    for student in students:
        if student['id'] == id:
            students.remove(student)
            return {"message": "Student deleted"}, 200

    return {"error": "Student not found"}, 404