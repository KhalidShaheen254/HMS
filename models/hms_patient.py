from odoo import models, fields


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
    PCR = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()

