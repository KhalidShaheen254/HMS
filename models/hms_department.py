from odoo import models, fields


class hmsDepartment(models.Model):
    _name = "hms.department"

    name = fields.Char()
    is_opened = fields.Boolean()
    capacity = fields.Integer()
    patients_ids = fields.One2many("hms.patient", "department_id")
    dept_doctors_ids = fields.One2many("hms.doctor", "department_id")

