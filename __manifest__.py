# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'Gestion annuaire',
    'version': '1.0',
    'category': 'Gestion annuaire',
    'description': """
      ce module permet de corrige les anomalie dans le centre d'imputation
    """,
    'depends': ['base','mail'],
    'data': [
        "security/ir.model.access.csv",
        "views/centre_imputation.xml",
        "views/fiche_personnelle.xml",
        "views/matricule_ko.xml",
        "views/matricule_ok.xml",
        "views/cirhom_ok.xml",
        "views/cirhom_ko.xml",
        "rapport/template_matricule_ok.xml",
        "rapport/template_matricule_ko.xml",
        "rapport/template_cirhom.xml",
        "rapport/template_cirhom_ok.xml",
        "wizard/wizard_matricule_ok.xml",
        "wizard/wizard_matricule_ko.xml",
        "wizard/vider_table_centre_imputation.xml",
        "wizard/wizard_cirhom_ok.xml",
        "wizard/wizard_cirhom_ko.xml",
        "views/menu_general.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
