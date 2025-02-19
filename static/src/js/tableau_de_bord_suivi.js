odoo.define('suivi_dossier_changement.tableau_de_bord_suivi', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;


   var TableauDeBordSuivi = AbstractAction.extend({
                    template: 'dashboard_template',

                    start: function () {
                           var self = this;
                           this._super.apply(this, arguments);
                           self.getNombrePc() ;
                           self.getNombreHc() ;
                           self.getNombreD1() ;
                           self.getNombreOt() ;
                           self.getNombreOd() ;
                           self.getNombreOtRapport() ;
                           self.getNombreOdRapport() ;
                            self.calculator_op() ;
                            self.getNombrePostedate ();
                    },

//           le nombre de dossiers passer au changement(PC)
                getNombrePc: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'suivi.dossier.changement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['etat_demande', '=', 'oui']]],

                                        }).then(function(count){

                                               self.nombrePc = count;
                                               var element = document.getElementById("nombre_pc");
                                               var val = document.getElementById("nombre_d1");
                                               var valod_pc = document.getElementById("nombre_od_pc");
                                                if(element) {
                                                   element.textContent = count;
                                                   val.textContent = count;
                                                   valod_pc.textContent = count;
                                                 }

                                                });
                                       },


  //           le nombre de dossiers no passer au changement(HC)
                getNombreHc: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'suivi.dossier.changement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['etat_demande', '=', 'non']]],

                                        }).then(function(count){

                                               self.nombreHc = count;
                                               var element = document.getElementById("nombre_hc");
                                                if(element) {  element.textContent = count;   }
                                                // calcul de la somme de pc et hc
                                                 self.calculateRatio();

                                                });

                                       },
 //           le nombre d'accord d1
                getNombreD1: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'suivi.dossier.changement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['etat_demande', '=', 'oui'],['decision1', '=', 'accord']]],

                                        }).then(function(count){

                                               self.nombred1 = count;
                                               var element = document.getElementById("nom_d1");
                                                if(element) {  element.textContent = count;   }

                                                // calcul de la somme de pc et hc
                                                 self.calculatQuanitedp();

                                                });

                                       },
   // Nombre OT ************************************************************************
           getNombreOt: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'ordre.travail',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[]],

                                        }).then(function(count){

                                               self.nombreot = count;
                                                 var element = document.getElementById("nombre_ot");
                                                  if(element) {  element.textContent = count;   }

                                                });

                                       },

  // Nombre OD ******************************************************************************************
           // Nombre OT
           getNombreOd: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'ordre.deploiement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[]],

                                        }).then(function(count){

                                               self.nombreod = count;
                                                  var element = document.getElementById("nombre_od");
                                                  if(element) {  element.textContent = count;   }
                                                 self.calculator_op();

                                                });

                                       },
      // Nombre OT avec rapport ************************************************************************
           getNombreOtRapport: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'ordre.travail',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['etat_rapport', '=', 'oui']]],

                                        }).then(function(count){
                                               self.nombrerapport_ot = count;
                                                  self.calculator_op();
                                                });
                                       },
   // Nombre OD avec rapport
            getNombreOdRapport: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'ordre.deploiement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['etat_rapport', '=', 'oui']]],

                                        }).then(function(count){

                                               self.nombrerapport_od = count;
                                               self.calculator_op();
                                                });

                                       },
  // calcul du nombre de suivi avec une date de poste
            getNombrePostedate: function() {
                                        var self = this;
                                        rpc.query({

                                            model: 'suivi.dossier.changement',
                                            method: 'search_count', // Méthode pour récupérer le nombre de records
                                            args: [[['dat_bila_post','!=', false]]],

                                        }).then(function(count){

                                                    self.nombreDB = count;
                                                    var element = document.getElementById("nombre_db");
                                                    if(element) {  element.textContent = count   }
                                                    self.calculatedb_pc();

                                                });

                                       },
  // ********************************************************************************************************************************

                // Calcul du ratio PC / (PC + HC)
                calculateRatio: function() {

                            var pc = this.nombrePc || 0;
                            var hc = this.nombreHc || 0;
                            var total = pc + hc;

                            // Évite la division par zéro
                            var ratio = total > 0 ? (pc / total) : 0;

                            var element = document.getElementById("nombre_pc_hc");

                             if(element) {  element.textContent = ratio.toFixed(2);;   }


                },

                  // Calcul de d1/pc
                calculatQuanitedp: function() {

                            var pc = this.nombrePc || 0;
                            var d1 = this.nombred1 || 0;

                            // Évite la division par zéro
                             var ratio = pc > 0 ? (d1 / pc) : 0;

                             var element = document.getElementById("val2");

                             if(element) {  element.textContent = ratio.toFixed(2);  }

                },

                // calcul de OR/OP

                  calculator_op: function() {

                                var ot = this.nombreot || 0;
                                var od = this.nombreod || 0;
                                var rap_ot= this.nombrerapport_ot ;
                                var rap_od = this.nombrerapport_od ;

                                // calcul de la somme de ot et od et avec rapport
                                 var total_ot_od = ot + od ;

                                 var total_rapport_ot_od = rap_ot + rap_od ;

                                 // Recuperation du total de od et ot avec rapport
                                  var element = document.getElementById("nombre_or");

                                 if(element) {  element.textContent = total_rapport_ot_od;   }

                                 // le calcul de or /pc

                                 var val_od_dt = total_ot_od > 0 ? (total_rapport_ot_od / total_ot_od) : 0;

                                 var element = document.getElementById("division_od_ot");

                                 if(element) {  element.textContent = val_od_dt.toFixed(2);   }


                },

                // calcul de db/pc

                  calculatedb_pc: function() {
                                var pc = this.nombrePc || 0;
                                var db = this.nombreDB || 0;

                                // Évite la division par zéro
                                var ratio = pc > 0 ? (db / pc) : 0;

                                var element = document.getElementById("nombre_db_pc");

                                 if(element) {  element.textContent = ratio.toFixed(2) ;  }

                },



  });

    core.action_registry.add('tableau_de_bord_suivi', TableauDeBordSuivi);

    return TableauDeBordSuivi;
});
