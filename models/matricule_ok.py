# -*-coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError, _logger
import re
import logging

class FicheMatriculeKo(models.Model):
    _name = "fiche.matricule.ok"

    def cirhom_ko_v2(self):
        fiche_personnelle_records = self.env["fiche.personnelle"].search([])
        annuaires = self  # Suppose que `self` est un recordset d'annuaires
        matricule_ko = self.env["fiche.cirhom.ko"].search([]).unlink()

        # Créer un dictionnaire pour la recherche rapide
        valctra_mapping = {}
        for fiche in fiche_personnelle_records:
            centre_frais_num = ''.join(re.findall(r'\d+', fiche.c_c_pers))
            valctra = centre_frais_num + str(fiche.act_pers) + str(fiche.ctra_pers)
            valctra_mapping[valctra] = fiche

        # Boucler sur les annuaires seulement une fois
        for annuaire in annuaires:
            centre_frais_num_annuaire = ''.join(re.findall(r'\d+', annuaire.centre_fra))
            # Vérification directe dans le dictionnaire
            if centre_frais_num_annuaire not in valctra_mapping:
                # As there is no corresponding fiche, you cannot access valctra_mapping with centre_frais_num_annuaire
                self.env["fiche.cirhom.ko"].create({
                    "entrep": annuaire.entrep,
                    "name": annuaire.name,
                    "matricule": annuaire.matricule,
                    "nom_prenom": annuaire.nom_prenom,
                    "centre_fra": annuaire.centre_fra,
                    "nbre": 1
                })

    def cirhom_ok_v2(self):
        fiche_personnelle_records = self.env["fiche.personnelle"].search([])
        matricule_ok= self.env["fiche.cirhom.ok"].search([]).unlink()
        cirhom_ko = self.env["fiche.cirhom.ko"].search([]).unlink()
        annuaires = self  # Suppose que `self` est un recordset d'annuaires

        # Créer un dictionnaire pour la recherche rapide
        valctra_mapping = {}
        for fiche in fiche_personnelle_records:
            # centre_frais_num = ''.join(re.findall(r'\d+', fiche.c_c_pers))
            valctra = str(fiche.c_c_pers) + str(fiche.act_pers)
            valctra_mapping[valctra] = fiche


        for annuaire in annuaires:
            centre_frais_num_annuaire = ''.join(re.findall(r'\d+', annuaire.centre_fra))
            # Vérification directe dans le dictionnaire
            if centre_frais_num_annuaire in valctra_mapping:
                self.env["fiche.cirhom.ok"].create({
                    "entrep": annuaire.entrep,
                    "name": annuaire.name,
                    "matricule": annuaire.matricule,
                    "nom_prenom": annuaire.nom_prenom,
                    "centre_fra": annuaire.centre_fra,
                    "nbre": 1
                })

            else :

                self.env["fiche.cirhom.ko"].create({
                    "entrep": annuaire.entrep,
                    "name": annuaire.name,
                    "matricule": annuaire.matricule,
                    "nom_prenom": annuaire.nom_prenom,
                    "centre_fra": annuaire.centre_fra,
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