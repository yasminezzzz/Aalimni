frappe.ui.form.on("student", {
    offer: function(frm) {
        var offer_field = frm.fields_dict['offer'];
        var offer_value = offer_field.get_value();
        if (offer_value) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'offer',
                    name: offer_value
                },
                callback: function(data) {
                    var offer_doc = data.message;
                    if (offer_doc) {
                        if (offer_doc.enrollement_count >= offer_doc.enrollement_max) {
                            frappe.msgprint('Sorry, the offer is completed. You cannot choose this offer.');
                            offer_field.set_value('');
                        } else {
                            var new_enrollement_count = (offer_doc.enrollement_count || 0) + 1;
                            if (new_enrollement_count <= offer_doc.enrollement_max) {
                                frappe.call({
                                    method: 'frappe.client.set_value',
                                    args: {
                                        doctype: 'offer',
                                        name: offer_value,
                                        fieldname: 'enrollement_count',
                                        value: new_enrollement_count
                                    },
                                    callback: function(response) {
                                        frappe.msgprint('Welcome to our offer!!');
                                    }
                                });
                            } else {
                                frappe.msgprint('Sorry, the offer is completed. You cannot choose this offer.');
                                offer_field.set_value('');
                            }
                        }
                    }
                }
            });
        }
    }
});
