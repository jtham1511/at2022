# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class WebFormPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    country_residence = fields.Many2one('res.country', string='Country of Residence', ondelete='restrict')
    passport_number = fields.Char(string="Passport Number")
    travel_visa = fields.Char(string="Travel Visa Number")
    date_passport_issue = fields.Datetime()
    date_visa_issue = fields.Datetime()
    date_passport_expiry = fields.Datetime()
    date_visa_expiry = fields.Datetime()
    emergency_contact_name = fields.Char()
    emergency_contact_number = fields.Char()
    emergency_contact_relation = fields.Char()
    religion = fields.Many2one('rational.res.religion', string='Religion', ondelete='restrict')
    hear_teaching = fields.Many2one('rational.res.source', string='From Source', ondelete='restrict')
    attend_teaching_before = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Attend Teaching Before ?")
    being_india_before = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="First Trip to India ?")
    enrol_mailing_list = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                          string="Do you wish to be part of our e-mailing list ？")
    recent_photo = fields.Binary(string="Copy of recent photograph")
    passport_upload = fields.Binary(string="Copy of passport page with personal details")
    visa_upload = fields.Binary(string="Copy of India Visa (optional)")
    vaccine_upload = fields.Binary(string="Copy of your Notarised Vaccine Certificate")
    is_ograniser = fields.Boolean(string="Is Organiser")
    is_shanga_member = fields.Boolean(string="Is Sangha")
    no_of_participant = fields.Integer(string="No of Participant")
    vaccine_fist_dose = fields.Many2one('rational.res.vaccine', string='1st dose Vaccine Type', ondelete='restrict')
    vaccine_second_dose = fields.Many2one('rational.res.vaccine', string='2nd dose Vaccine Type', ondelete='restrict')
    vaccine_third_dose = fields.Many2one('rational.res.vaccine', string='3rd dose Vaccine Type', ondelete='restrict')
    vaccine_first_booster = fields.Many2one('rational.res.vaccine', string='1st booster Vaccine Type', ondelete='restrict')
    vaccine_second_booster = fields.Many2one('rational.res.vaccine', string='2nd booster Vaccine Type', ondelete='restrict')
    date_vaccine_first = fields.Datetime(string='1st dose Vaccine Date')
    date_vaccine_second = fields.Datetime(string='2nd dose Vaccine Date')
    date_vaccine_third = fields.Datetime(string='3rd dose Vaccine Date')
    date_vaccine_booster1 = fields.Datetime(string='1st booster Vaccine Date')
    date_vaccine_booster2 = fields.Datetime(string='2nd booster Vaccine Date')

    note_01 = fields.Text(string='Note 01', readonly=True)
    note_02 = fields.Text(string='Note 02', readonly=True)
    note_03 = fields.Text(string='Note 03', readonly=True)
    note_04 = fields.Text(string='Note 04', readonly=True)
    note_05 = fields.Text(string='Note 05', readonly=True)
    note_06 = fields.Text(string='Note 06', readonly=True)
    note_07 = fields.Text(string='Note 07', readonly=True)

class RationalResReligion(models.Model):
    _name = 'rational.res.religion'

    name = fields.Char()


class RationalTeachingSource(models.Model):
    _name = 'rational.res.source'

    name = fields.Char()


class RationalVaccineType(models.Model):
    _name = 'rational.res.vaccine'

    name = fields.Char()
