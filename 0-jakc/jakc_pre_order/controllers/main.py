import json
import logging
import werkzeug
import werkzeug.utils
from datetime import datetime
from math import ceil

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.http import request
from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT as DTF, ustr
import json

_logger = logging.getLogger(__name__)


class WebsitePreorder(http.Controller):

    @http.route(['/preorder'], type='http', auth="user", website=True)
    def pre_order_website(self):
        values = {}
        product_obj = http.request.env['product.template']
        products = product_obj.sudo().search([], offset=20, limit=6)
        values.update({'products': products})
        return http.request.render("jakc_pre_order.pre_order", values)

    @http.route(['/preorder/products'], type='http', auth="user")
    def pre_order_products(self):
        sale_pre_order_obj = http.request.env['sale.pre.order']
        sale_pre_order_line_obj = http.request.env['sale.pre.order.line']
        args = [('state','=','open')]
        sale_pre_order_ids = sale_pre_order_obj.sudo().search_read(args)
        sale_pre_order = sale_pre_order_ids[0]
        args = [('id','in', sale_pre_order['sale_pre_order_line_ids'])]
        sale_pre_order_line_ids = sale_pre_order_line_obj.sudo().search_read(args)
        return json.dumps(sale_pre_order_line_ids)


