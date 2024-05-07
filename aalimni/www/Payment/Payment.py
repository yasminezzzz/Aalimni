from frappe import db, _
import frappe

def get_context(context):
   
    
    offers = db.sql("""
        SELECT name, offer_name, price
        FROM taboffer;
    """, as_dict=True)
    
    
    context.offers = offers

