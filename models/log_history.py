from odoo import models,fields


class LogHistory(models.Model):
    _name = "log.history"
    _rec_name = "name"

    date = fields.Date()
    description = fields.Text()
    patient_id = fields.Many2one("hms.patient")
    name = fields.Char(related= "patient_id.first_name")