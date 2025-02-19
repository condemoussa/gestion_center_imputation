from odoo import models, fields
from datetime import datetime

class WizardMatriculeOK(models.TransientModel):
    _name = 'wizard.matricule.ok'

    # Champs par défaut
    mois = fields.Char(string="Mois", default=lambda self: datetime.now().strftime('%m'))
    annee = fields.Char(string="Année", default=lambda self: str(datetime.now().year))

    def action_matricule_ok(self):
        lines = []
        matricule_ok = self.env["fiche.matricule.ok"].search([])
        nbre = 1
        for line in matricule_ok:
            vals = {
                'societ_id': line.entrep,
                'numero': line.name,
                'matricule': line.matricule,
                'nom': line.nom_prenom,
                'cc_ci': line.centre_fra,
                'nbre': line.nbre,
                'compte':nbre
            }
            nbre = nbre + 1
            lines.append(vals)


        # Inclure les champs mois et annee dans les données envoyées au rapport
        data = {
            'form_date': self.read()[0],
            'line_data': lines,
            'mois': self.mois,  # Mois par défaut
            'annee': self.annee  # Année par défaut
        }
        return self.env.ref('gestion_center_imputation.report_matricule_ok_views_action').report_action(self, data=data)
