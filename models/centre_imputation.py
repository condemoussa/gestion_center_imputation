# -*-coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError

class AnnuaireTelephonique(models.Model):
    _name = "annuaire.telephone"
    _description = "Annuaire telephonique"


    def netoyer_la_table(self):
        records = self.env["annuaire.telephone"].search([])
        records.unlink()

    @api.model
    def create(self, vals):
        res = super(AnnuaireTelephonique, self).create(vals)
        return res



    # la methode pour vider la table
    def netoyer_la_table(self):
        existing_records = self.search([])
        existing_records.unlink()


    name = fields.Char("POSTE:")
    nom_prenom = fields.Char("Nom  et prénom :")
    matricule = fields.Char("Matricule :")
    entrep = fields.Char("Entreprise :")
    centre_fra = fields.Char("Centre de frais :")
    quo_telephoen = fields.Char("Quota telephone :")
    bonus = fields.Char("Bonus :")
    automc = fields.Char("Autocom :")
    site = fields.Char("Site :")
    droit_acces = fields.Char("Droit acces :")
    restric = fields.Char("Restriction :")
    type_poste = fields.Char("Type Poste :")


    # Les information des personnelle de la societe
