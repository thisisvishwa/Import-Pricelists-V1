```python
from odoo import models, fields, api
import xlrd

class PricelistImport(models.Model):
    _name = 'pricelist.import'
    _description = 'Pricelist Import'

    name = fields.Char('Name', required=True)
    data_file = fields.Binary('Excel File', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    def import_pricelist(self):
        try:
            book = xlrd.open_workbook(file_contents=self.data_file.decode('base64'))
            sheet = book.sheet_by_index(0)

            for row in range(1, sheet.nrows):
                pricelist_id = sheet.cell(row, 0).value
                name = sheet.cell(row, 1).value
                currency = sheet.cell(row, 2).value
                product_category = sheet.cell(row, 3).value
                min_quantity = sheet.cell(row, 4).value
                start_date = sheet.cell(row, 5).value
                end_date = sheet.cell(row, 6).value
                pricing_computation_methods = sheet.cell(row, 7).value

                # Add your own logic to create/update pricelist records in Odoo

            self.state = 'done'
        except Exception as e:
            raise Warning(_('Import failed due to: %s') % tools.ustr(e))
```