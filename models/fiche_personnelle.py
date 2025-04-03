# -*-coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError

class FichePersonnelle(models.Model):
    _name = "fiche.personnelle"

    def netoyer_la_table(self):
        records = self.env["fiche.personnelle"].search([])
        records.unlink()



    @api.model
    def fiche_matriculeko(self):
        # Récupération des lignes de la table "annuaire.telephone"
        centre_annuaire = self.env["annuaire.telephone"].search([])
        fiche_personnelle = self.env["fiche.personnelle"].search([])

        for annuaire in centre_annuaire:
            if annuaire.matricule !=False:
                if annuaire.matricule[-4:] !="0000":
                    if not fiche_personnelle.filtered(lambda p: p.mat_pers == annuaire.matricule):
                        # Création d'un nouvel enregistrement dans la table "fiche.matricule.ko"
                        self.env["fiche.matricule.ko"].create({
                            "entrep": annuaire.entrep,
                            "name": annuaire.name,
                            "matricule": annuaire.matricule,
                            "nom_prenom": annuaire.nom_prenom,
                            "centre_fra": annuaire.centre_fra,
                            "nbre": 1
                        })
    #

    @api.model
    def fiche_matricule(self):
        centre_annuaire = self.env["annuaire.telephone"].search([])
        for annuaire in centre_annuaire:
            # Comparaison des matricules ou autre logique
            if annuaire.matricule != False:
                if annuaire.matricule[-4:] == "0000":
                    self.env["fiche.matricule.ok"].create({
                        "entrep": annuaire.entrep,
                        "name": annuaire.name,
                        "matricule": annuaire.matricule,
                        "nom_prenom": annuaire.nom_prenom,
                        "centre_fra": annuaire.centre_fra,
                        "nbre": 1
                    })


    @api.model
    def fiche_matriculeok(self):
        centre_annuaire = self.env["annuaire.telephone"].search([])
        fiche_rh = self.env["fiche.personnelle"].search([])
        for fiche in fiche_rh:
            # Parcourir également les enregistrements de "annuaire.telephone"
            for annuaire in centre_annuaire:
                if fiche.mat_pers == annuaire.matricule:

                    self.env["fiche.matricule.ok"].create({
                        "entrep": annuaire.entrep,
                        "name": annuaire.name,
                        "matricule": annuaire.matricule,
                        "nom_prenom": annuaire.nom_prenom,
                        "centre_fra": annuaire.centre_fra,
                        "nbre": 1
                    })

        self.fiche_matriculeko()
        self.fiche_matricule()


    # Les information des personnelle de la societe
    societ_id = fields.Char("Société :")
    mat_pers = fields.Char("Matricule :")
    nom_pers = fields.Char("Nom :")
    pren_pers = fields.Char("Prénom :")
    c_c_pers = fields.Char("CC-C :")
    act_pers = fields.Char("ACT :")
    ctra_pers = fields.Char("CTRA :")