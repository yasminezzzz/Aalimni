from frappe import db

def get_context(context):
    schedules = db.sql("""
        SELECT 
            date, 
            TIME_FORMAT(end, '%H:%i') AS end_time, 
            TIME_FORMAT(start, '%H:%i') AS start_time, 
            teacher, 
            offer,
            subject 
        FROM 
            tabsession
    """, as_dict=True)
    
    schedule_by_day_and_time = {
        "lundi": {},
        "mardi": {},
        "mercredi": {},
        "jeudi": {},
        "vendredi": {}
    }
    
    for schedule in schedules:
        day = schedule.get("date").lower() 
        start_time = schedule.get("start_time")
        schedule_by_day_and_time[day][start_time] = schedule
    
    for day in schedule_by_day_and_time:
        for time in ["16:00", "17:00", "18:00", "19:00", "20:00"]:
            if time not in schedule_by_day_and_time[day]:
                schedule_by_day_and_time[day][time] = None
    
    context.schedule = schedule_by_day_and_time
    context.schedules = schedules  