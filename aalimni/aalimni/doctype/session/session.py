from frappe.model.document import Document
from frappe import _
import frappe
class session(Document):
    def validate(self):
        # Vérifier si la combinaison de teacher, end, start et date existe déjà
        if self.exists_in_db():
            frappe.throw(_("La combinaison de teacher, end, start et date existe déjà."))

        # Vérifier si l'offre contient le sujet spécifié
        if not self.subject_in_offer():
            frappe.throw(_("L'offre ne contient pas le sujet spécifié."))

    def exists_in_db(self):
        # Vérifier si la combinaison de teacher, end, start et date existe déjà dans la base de données
        return frappe.db.exists({
            "doctype": "session",
            "teacher": self.teacher,
            "end": self.end,
            "start": self.start,
            "date": self.date
        })

    def subject_in_offer(self):
        # Vérifier si l'offre contient le sujet spécifié
        if not self.offer:
            return False  # Si aucun offre spécifié, le sujet ne peut pas être dans l'offre
        offer = frappe.get_doc("offer", self.offer)
        for subject in offer.subjects:
            if subject.subject_name == self.subject:
                return True
        return False  # Aucun sujet correspondant trouvé dans l'offre
