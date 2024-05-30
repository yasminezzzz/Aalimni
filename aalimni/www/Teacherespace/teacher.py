from frappe import db, session

def get_context(context):
    current_user_email = session.user
    teachers = db.sql("""SELECT first_name, last_name, email FROM tabteacher;""", as_dict=True)
    
    context.teachers = teachers

    # Initialiser le message par défaut
    context.current_user_message = "Current user is not a teacher."

    # Vérifier si l'utilisateur actuel est un enseignant
    current_teacher_name = None
    for teacher in teachers:
        if teacher['email'] == current_user_email:
            current_teacher_name = f"{teacher['first_name']}-{teacher['last_name']}".lower()
            context.current_user_message = f"Hello {teacher['first_name']} {teacher['last_name']}"
            break

    # Si l'utilisateur actuel est un enseignant, récupérer les sessions correspondantes
    if current_teacher_name:
        sessions = db.sql("""SELECT name, offer, subject, teacher FROM tabsession WHERE teacher=%s""", (current_teacher_name,), as_dict=True)
        context.sessions = sessions
    else:
        context.sessions = []
