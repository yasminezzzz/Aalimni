from frappe import db, _
import frappe

def get_context(context):
    offer = frappe.request.args.get('offer')
    subject = frappe.request.args.get('subject')

    # Récupérer les chapitres
    CHAPTER = db.sql("""
       SELECT name1, unit, offer, subject, name as id FROM tabchap WHERE offer=%s AND subject=%s ORDER BY unit;
    """, (offer, subject), as_dict=True)
    
    frappe.logger().info("Retrieved chapters: {}".format(CHAPTER))
    
    # Récupérer les leçons
    LESSONS = db.sql("""
        SELECT name, number, percentchap, percentsubject, chap
        FROM tablessons ;
    """, as_dict=True)

    # Associer les leçons aux chapitres correspondants
    for chapter in CHAPTER:
        chapter['lessons'] = [lesson for lesson in LESSONS if lesson['chap'] == chapter['name1']]
    
    context.CHAPTER = CHAPTER
    context.LESSONS = LESSONS  # Si nécessaire pour d'autres utilisations

    # Accès à la liste des leçons
    lesson_names = [lesson['name'] for lesson in LESSONS]
    lesson_numbers = [lesson['number'] for lesson in LESSONS]
    lesson_percent_chap = [lesson['percentchap'] for lesson in LESSONS]
    lesson_percent_subject = [lesson['percentsubject'] for lesson in LESSONS]
    lesson_chap = [lesson['chap'] for lesson in LESSONS]
    
    # Vous pouvez utiliser ces listes comme nécessaire dans le reste de votre code
