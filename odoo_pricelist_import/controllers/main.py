```python
from odoo import http
from odoo.http import request
from . import pricelist_import

class PricelistImportController(http.Controller):

    @http.route('/pricelist_import/upload', type='http', auth='user')
    def upload_pricelist(self, **kw):
        if not request.env.user.has_group('base.group_system'):
            return request.not_found()
        return request.render('odoo_pricelist_import.upload_pricelist_template')

    @http.route('/pricelist_import/import', type='http', auth='user', methods=['POST'], csrf=False)
    def import_pricelist(self, **kw):
        if not request.env.user.has_group('base.group_system'):
            return request.not_found()
        file = kw.get('file')
        if not file:
            return request.redirect('/pricelist_import/upload')
        try:
            pricelist_import.import_pricelist(file)
            return request.redirect('/web#action=base.action_pricelist_form')
        except Exception as e:
            return request.render('odoo_pricelist_import.upload_pricelist_template', {'error': str(e)})
```