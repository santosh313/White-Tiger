# from education.education.doctype.student.student import Student
# from frappe.model.document import Document

# class SantoshStudent(Document):
#     def validate(self):
#         print("\n\n\n THis is place where we want add logic... \n\n\n")
#         return

from education.education.doctype.student.student import Student

class SantoshStudent(Student):  # Inherit from Student instead of Document
    def validate(self):
        print("\n\n\n This is the place where we want to add logic... \n\n\n")
        super().validate()  # Call the original validate method
