from odoo import models, fields
from datetime import datetime

class WizardCirhomOK(models.TransientModel):
    _name = 'wizard.cirhom.ok'

    # Champs par défaut
    mois = fields.Char(string="Mois", default=lambda self: datetime.now().strftime('%m'))
    annee = fields.Char(string="Année", default=lambda self: str(datetime.now().year))

    def action_cirhom_ok(self):
        lines = []
        cirhom_ok = self.env["fiche.cirhom.ok"].search([])

        nbre = 1
        for line in cirhom_ok:
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

        return self.env.ref('gestion_center_imputation.report_cirhom_ok_views_action').report_action(self, data=data)
