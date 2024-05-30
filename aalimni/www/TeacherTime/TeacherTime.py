import frappe

def get_context(context):
    current_user_email = frappe.session.user
    teachers = frappe.db.sql("SELECT first_name, last_name, email FROM tabteacher;", as_dict=True)

    teacher_dict = {teacher['email']: teacher for teacher in teachers}

    context.current_user_message = "Current user is not a teacher."
    current_teacher_name = None

    if current_user_email in teacher_dict:
        teacher = teacher_dict[current_user_email]
        current_teacher_name = f"{teacher['first_name']}-{teacher['last_name']}".lower()
        context.current_user_message = f"the scheduler of Mr {teacher['first_name']} {teacher['last_name']}"

    if current_teacher_name:
        sessions = frappe.db.sql("""
            SELECT name, subject, date, offer, TIME_FORMAT(start, '%%H:%%i') AS start_time, TIME_FORMAT(end, '%%H:%%i') AS end_time
            FROM tabsession 
            WHERE teacher=%s
        """, (current_teacher_name,), as_dict=True)
        
        context.sessions = sessions
        
        schedule_by_day_and_time = {
            "lundi": {},
            "mardi": {},
            "mercredi": {},
            "jeudi": {},
            "vendredi": {}
        }
        
        for session in sessions:
            day = session.get("date").lower()
            start_time = session.get("start_time")
            schedule_by_day_and_time[day][start_time] = session
        
        for day in schedule_by_day_and_time:
            for time in ["16:00", "17:00", "18:00", "19:00", "20:00"]:
                if time not in schedule_by_day_and_time[day]:
                    schedule_by_day_and_time[day][time] = None
        
        context.schedule_by_day_and_time = schedule_by_day_and_time
    else:
        context.sessions = []
