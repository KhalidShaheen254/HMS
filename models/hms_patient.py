from odoo import models, fields, api


class hmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    CR_ratio = fields.Float()
    blood_type = fields.Selection(
        [('a', 'A'), ('b', 'B'), ('o', 'O')]
    )
    states = fields.Selection(
        [('u', 'Undetermined'), ('g', 'Good'), ('f', 'Fair'), ('s', 'Serious')]
    )
    PCR = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    department_id = fields.Many2one("hms.department")
    doctors_ids = fields.Many2many("hms.doctor")
    log_history = fields.One2many("log.history", "patient_id")

    @api.onchange("age")
    def _onchange_PCR(self):
        if not self.age:
            return {}
        if self.age < 30:
            self.PCR = True
            return {
                'warning': {
                    'title': 'Hello',
                    'message': 'Your Age Lt 30 so PCR Checked :)'
                }
            }
