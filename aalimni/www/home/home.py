from frappe import db

import frappe

def get_context(context):
    # Fetch data from tabsubjects table
    subjects = db.sql("""SELECT subject_name , subject_image from tabsubjects ;
""", as_dict=True)
    context.subjects = subjects
    
    # Fetch data from tabdetails_offers table
    details = db.sql(""" SELECT details_name, image FROM tabdetails_offers;
 ;
""", as_dict=True)
    context.details = details

    goals = db.sql(""" SELECT gaols_name , goals_image from tabgoals ;               
""" ,as_dict=True)
    context.goals = goals
