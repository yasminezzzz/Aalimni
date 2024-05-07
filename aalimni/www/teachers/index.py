from frappe import db

def get_context(context):
   
    teachers = db.sql("""SELECT first_name, last_name, image, speciality, description FROM tabteacher;""", as_dict=True)
    
    
    context.teachers = teachers