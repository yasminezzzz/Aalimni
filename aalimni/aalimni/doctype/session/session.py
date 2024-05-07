from frappe.model.document import Document
from frappe import _
import frappe
class session(Document):
    def validate(self):
        # Vérifier si la combinaison de teacher, end, start et date existe déjà
        if self.exists_in_db():
            frappe.throw(_("La combinaison de teacher, end, start et date existe déjà."))

    def exists_in_db(self):
        # Vérifier si la combinaison de teacher, end, start et date existe déjà dans la base de données
        return frappe.db.exists({
            "doctype": "session",
            "teacher": self.teacher,
            "end": self.end,
            "start": self.start,
            "date": self.date
        })
