from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from datetime import timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

class TdsWizard(models.TransientModel):
    _name = 'tds_report.report.tds'

    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' is clicked.
        """
        data = {
        'ids': self.ids,
        'model': self._name,
        'form': {
        'date_start': self.date_start,
        'date_end': self.date_end,
            },}
        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('tds_report.action_report_tds').report_action(self,data)

class TdsAbstract(models.AbstractModel):
    """Abstract Model for report template.
    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """
    _name = 'report.tds_report.report_template_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = datetime.strptime(data['form']['date_start'], DATE_FORMAT)
        date_end = datetime.strptime(data['form']['date_end'], DATE_FORMAT)
        
        if not data.get('form'):
            raise UserError("Form content is missing, this report cannot be printed.")
        docs = []

        tds_name = self.env['account.invoice'].search(
            [('type','=','in_invoice'),
            ('state','=','paid'),
            ('create_date','>=',date_start.strftime(DATE_FORMAT)),
            ('create_date','<=',date_end.strftime(DATE_FORMAT))])
        for line_1 in tds_name:
            ass_no = self.env['account.nod.confg'].search(
                [('partner_id','=',line_1.partner_id.id)])
            for line_2 in ass_no:
                for line_3 in self.env['account.invoice.line'].search([
                    ('invoice_id','=',line_1.id),
                    ]):   
                # tds_p = self.env['account.invoice.line'].search([])
                # for line_3 in tds_p:
                    docs.append({
                            'date_inv':line_1.date_invoice,
                            'doc_no':line_1.number,
                            'vendor_no':line_1.partner_id.ref_code,
                            'partner':line_1.partner_id.name,
                            'pan_no':line_1.partner_id.pan_no,
                            'assess_code':line_2.assesse_code.name,
                            'tds_percent':line_3.tds_percent,
                            'tds_base':line_3.price_unit,
                            'tds_amount':line_3.tds_percent_amount,
                        })
        # map_env = self.env['account.tds.mapping'].search([
        #     ('id','=',nod_name),
        #     ('create_date','>=',date_start.strftime(DATE_FORMAT)),
        #     ('create_date','<=',date_end.strftime(DATE_FORMAT)),
        #     ])
        # acc_inv = map_env.env['account.invoice'].search([('type','=','in_invoice')])
        # for acc_nod_env in acc_inv.env['account.nod.confg.line'].search([]):
        #     docs.append({
        #         'map':map_env.name,
        #         'nod':acc_nod_env.partner_id.name,
        #         })

        # acc_inv = self.env['account.nod.confg.line'].search([])
        # for map_env in acc_inv.env['account.tds.mapping'].search(
        #     [('name','=',nod_name.name),
        #     ('create_date','>=',date_start.strftime(DATE_FORMAT)),
        #     ('create_date','<=',date_end.strftime(DATE_FORMAT))]):
        #     docs.append({
        #         'map': map_env.name
        #         })


        return {
        'doc_ids': data['ids'],
        'doc_model': data['model'],
        'date_start': date_start.strftime(DATE_FORMAT),
        'date_end': date_end.strftime(DATE_FORMAT),
        'docs': docs,
        }