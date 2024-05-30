import frappe

def get_context(context):
    current_user_email = frappe.session.user
    teachers = frappe.db.sql("SELECT first_name, last_name, email FROM tabteacher;", as_dict=True)

    teacher_dict = {teacher['email']: teacher for teacher in teachers}

    if current_user_email in teacher_dict:
        teacher = teacher_dict[current_user_email]
        current_teacher_name = f"{teacher['first_name']}-{teacher['last_name']}".lower()
    else:
        current_teacher_name = None
      
    if current_teacher_name:
        sessions = frappe.db.sql("""
           SELECT 
               tsub.subject_image,
               tsub.name,
               tsess.offer
           FROM 
               tabsubjects tsub
           INNER JOIN 
               tabsession tsess ON tsess.subject = tsub.name
           WHERE 
               tsess.teacher = %s;
        """, (current_teacher_name,), as_dict=True)
        
        context.sessions = sessions
    else:
        context.sessions = []

    return context
