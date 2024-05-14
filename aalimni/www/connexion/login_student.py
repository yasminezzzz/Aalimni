import frappe
from frappe import _

def get_context(context):
    pass

def post():
    email = frappe.form_dict.get('email')
    password = frappe.form_dict.get('password')

    # Vérifier les informations d'identification dans la base de données
    user = frappe.db.get_value('student', {'email': email, 'password': password})

    if user:
        # Connexion réussie, rediriger l'utilisateur vers une autre page
        frappe.local.response['type'] = 'redirect'
        frappe.local.response['location'] = '/connexion/welcome'  # URL de la page de bienvenue
    else:
        # Informer l'utilisateur que les informations d'identification sont incorrectes
        frappe.msgprint(_('Invalid email or password'))

    return
