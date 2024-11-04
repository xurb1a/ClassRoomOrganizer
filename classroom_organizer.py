from roster import student_roster 
import itertools

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)
  
  def add_student(self, name, age, height, favorite_subject, favorite_animal):
        new_student = {
            "name": name,
            "age": age,
            "height": height,
            "favorite_subject": favorite_subject,
            "favorite_animal": favorite_animal
        }
        student_roster.append(new_student)
        self.sorted_names = self._sort_alphabetically(student_roster)
    
  def remove_student(self, name):
        for student in student_roster:
            if student['name'].lower() == name.lower():  
                student_roster.remove(student)
                self.sorted_names = self._sort_alphabetically(student_roster)  
                return f"Student {name} removed successfully!"
        return f"Student {name} not found."

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index == len(student_roster):
      raise StopIteration
    self.index += 1
    return self.index

  @staticmethod
  def student_pairs():
    pairs = itertools.combinations(student_roster, 2)
    return f'possbile pairs are :{pairs}'

  @staticmethod
  def mns_students_combo(instance):
    math_students = instance.get_students_with_subject('Math')
    science_students = instance.get_students_with_subject('Science')
    mns_students = itertools.chain(math_students, science_students)
    combo4 = itertools.combinations(mns_students, 4)
    return f'the possible combinations of math and science students are : {combo4}'
