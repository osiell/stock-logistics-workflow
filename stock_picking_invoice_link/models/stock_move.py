# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2015-2016 AvanzOSC
# Copyright 2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    invoice_line_ids = fields.Many2many(
        comodel_name='account.invoice.line',
        string='Invoice Line',
        copy=False,
        readonly=True,
    )

    # Provide this field for backwards compatibility
    invoice_line_id = fields.Many2one(
        comodel_name='account.invoice.line', string='Invoice Line',
        compute="_compute_invoice_line_id")

    @api.multi
    @api.depends('invoice_line_ids')
    def _compute_invoice_line_id(self):
        for move in self:
            move.invoice_line_id = move.invoice_line_ids[:1]
