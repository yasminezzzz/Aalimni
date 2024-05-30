frappe.ready(function() {
    frappe.web_form.validate = () => {
        let data = frappe.web_form.get_values();
    
        for (let field in data) {
            if (!data[field]) {
                frappe.msgprint('All fields are required');
                return false;
            }
        }
    
    
        if (!(/^\d{8}$/.test(data.identity))) {
            frappe.msgprint('Identity must be 8 digits long');
            return false;
        }
    
        if (data.password !== data.identity) {
            frappe.msgprint('Password must match the identity');
            return false;
        }
        
        let emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let fullName = data.first_name + '.' + data.last_name;
        if (!emailRegex.test(data.email) || data.email !== fullName.toLowerCase() + '@gmail.com') {
            frappe.msgprint('Email must be in the format: first_name.last_name@gmail.com');
            return false;
        }
        
        return true;
    };

    frappe.web_form.on('offer', (field, value) => {
        if (value) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'offer',
                    name: value
                },
                callback: function(data) {
                    var offer_doc = data.message;
                    if (offer_doc) {
                        if (offer_doc.enrollement_count >= offer_doc.enrollement_max) {
                            frappe.msgprint('Sorry, the offer is completed. You cannot choose this offer.');
                            field.set_value('');
                        } else {
                            var new_enrollement_count = (offer_doc.enrollement_count || 0) + 1;
                            if (new_enrollement_count <= offer_doc.enrollement_max) {
                                frappe.call({
                                    method: 'frappe.client.set_value',
                                    args: {
                                        doctype: 'offer',
                                        name: value,
                                        fieldname: 'enrollement_count',
                                        value: new_enrollement_count
                                    },
                                    callback: function(response) {
                                        frappe.msgprint('Welcome to our offer!!');
                                    }
                                });
                            } else {
                                frappe.msgprint('Sorry, the offer is completed. You cannot choose this offer.');
                                field.set_value('');
                            }
                        }
                    }
                }
            });
        }
    });
});