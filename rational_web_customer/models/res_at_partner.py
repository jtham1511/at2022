# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class WebFormPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    country_residence = fields.Many2one('res.country', string='Country of Residence')
    passport_number = fields.Char(string="Passport Number")
    travel_visa = fields.Char(string="Travel Visa Number")
    date_passport_issue = fields.Date()
    date_visa_issue = fields.Date()
    date_passport_expiry = fields.Date()
    date_visa_expiry = fields.Date()
    emergency_contact_name = fields.Char()
    emergency_contact_number = fields.Char()
    emergency_contact_relation = fields.Char()
    religion = fields.Many2one('rational.res.religion', string='Religion')
    hear_teaching = fields.Many2one('rational.res.source', string='From Source')
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
    vaccine_fist_dose = fields.Many2one('rational.res.vaccine', string='1st dose Vaccine Type',
                                        placeholder='Vaccine Type')
    vaccine_second_dose = fields.Many2one('rational.res.vaccine', string='2nd dose Vaccine Type')
    vaccine_third_dose = fields.Many2one('rational.res.vaccine', string='3rd dose Vaccine Type')
    vaccine_first_booster = fields.Many2one('rational.res.vaccine', string='1st booster Vaccine Type')
    vaccine_second_booster = fields.Many2one('rational.res.vaccine', string='2nd booster Vaccine Type')
    date_vaccine_first = fields.Date(string='1st dose Vaccine Date')
    date_vaccine_second = fields.Date(string='2nd dose Vaccine Date')
    date_vaccine_third = fields.Date(string='3rd dose Vaccine Date')
    date_vaccine_booster1 = fields.Date(string='1st booster Vaccine Date')
    date_vaccine_booster2 = fields.Date(string='2nd booster Vaccine Date')
    security_id = fields.Char()


class RationalResReligion(models.Model):
    _name = 'rational.res.religion'

    name = fields.Char()


class RationalTeachingSource(models.Model):
    _name = 'rational.res.source'

    name = fields.Char()


class RationalVaccineType(models.Model):
    _name = 'rational.res.vaccine'

    name = fields.Char()
