from odoo import fields, models

class StudentManagement(models.Model):
    _name = 'collage.student'
    _inherit = ['mail.thread']
    _description = 'student data'

    name = fields.Char(string="Name",required=True, tracking =True)
    date_of_birth = fields.Date(string="DOB", tracking =True)
    gender = fields.Selection([('male',"Male"),("female","Female")], string="Gender", tracking =True)
    dept = fields.Char(string="Department", tracking =True)