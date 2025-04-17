from odoo import models, fields
from datetime import datetime

class ViderCentreImputation(models.TransientModel):
    _name = 'vider.centre.imputation'


    def vider_centre_imputation(self):

        annuaire = self.env["annuaire.telephone"].search([])
        annuaire.unlink()
        personnelle = self.env["fiche.personnelle"].search([])
        personnelle.unlink()

        matriculeko = self.env["fiche.matricule.ko"].search([])
        matriculeko.unlink()

        matriculeok = self.env["fiche.matricule.ok"].search([])
        matriculeok.unlink()

        cirhomko = self.env["fiche.cirhom.ko"].search([])
        cirhomko.unlink()

        cirhomok = self.env["fiche.cirhom.ok"].search([])
        cirhomok.unlink()

    def vider_fiche_rh(self):

        personnelle = self.env["fiche.personnelle"].search([])
        personnelle.unlink()

    def vider_fiche_poste(self):

        annuaire = self.env["annuaire.telephone"].search([])
        annuaire.unlink()

    def vider_matricule_ok(self):
        matriculeok = self.env["fiche.matricule.ok"].search([])
        matriculeok.unlink()

    def vider_matricule_ko(self):
        matriculeko = self.env["fiche.matricule.ko"].search([])
        matriculeko.unlink()





