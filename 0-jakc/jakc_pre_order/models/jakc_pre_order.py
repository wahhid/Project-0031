from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
from openerp import api, fields, models, _, exceptions
import openerp.addons.decimal_precision as dp
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SalePreOrder(models.Model):
    _name = 'sale.pre.order'

    @api.one
    def trans_open(self):
        return self.write({'state': 'open'})

    @api.one
    def trans_close(self):
        return self.write({'state': 'done'})

    @api.one
    def trans_re_open(self):
        return self.write({'state': 'open'})

    @api.multi
    def get_active(self):
        args = [('state','=','open')]
        sale_pre_order_ids = self.sudo().search(args)
        if len(sale_pre_order_ids) > 0:
            return sale_pre_order_ids
        else:
            return {'error': 'Error'}

    name = fields.Char('Name', size=100, required=True)
    date_start = fields.Date('Start Date')
    date_end = fields.Date('End Date')
    offset = fields.Integer('Offset', default=0)
    sale_pre_order_line_ids = fields.One2many('sale.pre.order.line','sale_pre_order_id', 'Lines')
    state = fields.Selection([('draft', 'New'), ('open', 'Open'), ('done', 'Close')], 'Status', default='draft')


class SalePreOrderLine(models.Model):
    _name = 'sale.pre.order.line'

    sale_pre_order_id = fields.Many2one('sale.pre.order', 'Order #')
    product_id = fields.Many2one('product.template', 'Product', required=True)
    product_uom_qty = fields.Float('Quantity', default=1)


class SalePreOrderTrans(models.Model):
    _name = 'sale.pre.order.trans'

    sale_pre_order_id = fields.Many2one('sale.pre.order', 'Order #')
    name = fields.Char('Name', size=10, readonly=True)
    partner_id = fields.Many2one('res.partner','Customer', required=True)


class SalePreOrderTransLine(models.Model):
    _name = 'sale.pre.order.trans.line'

    sale_pre_order_trans_id = fields.Many2one('sale.pre.order.trans', 'Trans #')
    product_id = fields.Many2one('product.template', 'Product', required=True)
    product_uom_qty = fields.Float('Quantity', default=1)


