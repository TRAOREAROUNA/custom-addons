from odoo import models,fields, api

class User(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property", "sales_id", sstring="Properties")

class ResUsers(models.Model):
    _inherit = "res.users"

    type_id = fields.Many2one(
        "estate.property.type",
        string="Property Type"
    )