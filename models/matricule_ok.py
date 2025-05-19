# -*-coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError, _logger
import re
import logging

class FicheMatriculeKo(models.Model):
    _name = "fiche.matricule.ok"

    @api.model
    def cirhom_ok_version2(self):
        centre_annuaire = self.env["annuaire.telephone"].search([])
        fiche_rh = self.env["fiche.personnelle"].search([])

        annuaire_dict = {a.matricule: a for a in centre_annuaire}
        for fiche in fiche_rh:
            annuaire = annuaire_dict.get(fiche.mat_pers)
            if annuaire:
                val_c_c_pers_act_pers = str(fiche.c_c_pers)+str(fiche.act_pers)
                if '_' in annuaire.centre_fra:
                    centre_frais = annuaire.centre_fra.split('_', 1)[1]
                    if val_c_c_pers_act_pers in centre_frais :
                        self.env["fiche.cirhom.ok"].create({
                            "entrep": annuaire.entrep,
                            "name": annuaire.name,
                            "matricule": annuaire.matricule,
                            "nom_prenom": annuaire.nom_prenom,
                            "centre_fra": annuaire.centre_fra +"       "+val_c_c_pers_act_pers,
                            "nbre": 1
                        })
                    else :
                        self.env["fiche.cirhom.ko"].create({
                            "entrep": annuaire.entrep,
                            "name": annuaire.name,
                            "matricule": annuaire.matricule,
                            "nom_prenom": annuaire.nom_prenom,
                            "centre_fra": annuaire.centre_fra +"        "+val_c_c_pers_act_pers ,
                            "nbre": 1
                        })













    name = fields.Char("Numero :")
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
    nbre = fields.Char("Nbre :")