# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Delice (<http://proyectodelice.es>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import api
from openerp.osv import osv, fields
from datetime import date
from dateutil import parser


class agro_project_project(osv.osv):    
    _inherit = 'project.project'
    
    _columns={
            'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion', required = True),
    }
    

agro_project_project()


class agro_project_task(osv.osv):
    _inherit = 'project.task'

    @api.one
    def weather_open(self):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        result = mod_obj.get_object_reference(self.env.cr, self.env.uid, 'agro_project', 'act_agro_project_weather')
        id = result and result[1] or False
        result = act_obj.read(self.env.cr, self.env.uid, [id], context=self.env.context)[0]

        start_date = self.date_start
        end_date = self.date_end

        #result['domain'] = "[('fecha','&gt;', '%s'), ('fecha','&lt;', '%s')]" % (start_date, end_date)

        return result

    _columns={
            'tipo_labor_id': fields.many2one('agro.project.tipo.labor', 'Tipo de labor'),
            #'pesada_ids': fields.one2many('agro.project.pesada', 'tarea_id','Pesadas'),
    }

agro_project_task()

class agro_project_tipo_labor(osv.osv):
    _name = 'agro.project.tipo.labor'
    _description = 'Tipo de labor'

    _columns={
            'name': fields.char('Tipo de labor', size=128, required = True),
              }

agro_project_tipo_labor()
