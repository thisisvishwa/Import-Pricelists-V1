{
    "name": "odoo_pricelist_import",
    "version": "1.0",
    "category": "Sales",
    "summary": "Import Pricelists from Excel files",
    "sequence": 1,
    "author": "Your Company",
    "website": "http://www.yourcompany.com",
    "description": """
    This module allows for the efficient import of pricelists and pricelist items from Excel files.
    """,
    "depends": ["base", "sale", "product"],
    "data": [
        "views/pricelist_import_view.xml",
        "data/sample_pricelist.xlsx"
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "external_dependencies": {
        "python": ["xlrd"]
    }
}