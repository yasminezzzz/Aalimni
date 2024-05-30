from frappe import db

def get_context(context):
    schedules = db.sql("""
     SELECT 
    tsess.date,
    TIME_FORMAT(tsess.end, '%H:%i') AS end_time,
    TIME_FORMAT(tsess.start, '%H:%i') AS start_time,
    tsess.teacher,
    tsess.offer,
    tsess.subject
FROM 
    tabsession tsess
JOIN (
    SELECT DISTINCT ts.parent AS offer
    FROM tabsubject ts
    LEFT JOIN (
        SELECT DISTINCT offer, subject
        FROM `tabsession`
    ) tsess_sub ON ts.parent = tsess_sub.offer AND ts.subject_name = tsess_sub.subject
    GROUP BY ts.parent
    HAVING COUNT(DISTINCT tsess_sub.subject) = (
        SELECT COUNT(DISTINCT subject_name)
        FROM tabsubject
        WHERE parent = ts.parent
    )
) filtered_offers ON tsess.offer = filtered_offers.offer

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