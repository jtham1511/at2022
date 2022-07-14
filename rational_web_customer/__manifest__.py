# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    #  Information
    'name': 'Rational Web Form Customer',
    'version': '1.0.1.0.0',
    'summary': 'Customized res.partner model to include Asia Teaching attribute',
    'description': """
    """,
    'category': 'Webform',

    # Author
    'author': 'Rational',
    'website': 'https://www.rational.com.sg/',

    # Dependency
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/id_data.xml',
        'data/rational.res.source.csv',
        'data/rational.res.religion.csv',
        'data/rational.res.vaccine.csv',
        'views/backup_res_at_partner_views.xml',
        'report/report.xml'
    ],
    # Other
    'installable': True,
    'license': 'LGPL-3',
}
