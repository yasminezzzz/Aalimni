# Dans un script Python de votre application Frappe
import frappe
from frappe import _
@frappe.whitelist(allow_guest=True)
def get_user_info():
    user_id = frappe.session.user
    user_doc = frappe.get_doc("User", user_id)
    return {"first_name": user_doc.first_name, "last_name": user_doc.last_name}


@frappe.whitelist()
def add_chapter(name1, unit, offer, subject):
    chapter = frappe.new_doc("Tabchap")
    chapter.name1 = name1
    chapter.unit = unit
    chapter.offer = offer
    chapter.subject = subject
    chapter.insert()

@frappe.whitelist()
def delete_chapter(chapter_name):
    frappe.delete_doc("TabChap", chapter_name)

@frappe.whitelist()
def update_chapter(chapter_name, name1=None, unit=None, offer=None, subject=None):
    chapter = frappe.get_doc("TabChap", chapter_name)
    if name1:
        chapter.name1 = name1
    if unit:
        chapter.unit = unit
    if offer:
        chapter.offer = offer
    if subject:
        chapter.subject = subject
    chapter.save()
