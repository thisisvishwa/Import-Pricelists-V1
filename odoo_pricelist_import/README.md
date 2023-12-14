# Odoo 16 CE Excel Pricelist Import Module

This module allows users to import pricelists and pricelist items from Excel files into Odoo 16 Community Edition (CE). It streamlines the process of updating and managing pricelists, enhancing the operational efficiency of businesses using Odoo.

## Features

- Import pricelists from Excel files.
- The module requires the `xlrd` Python library.
- A sample Excel file is provided to demonstrate the required format.
- Supports the import of fields like Pricelist ID, Name, Currency, Product Category, Min. Quantity, Start and End Dates, and pricing computation methods.

## User Classes

- Odoo Administrators: Users who manage and configure the Odoo system.
- Sales Managers: Users who manage sales operations and require frequent updates to pricelists.

## Installation

1. Download the module from the repository.
2. Place the module in your Odoo addons folder.
3. Update the module list in your Odoo instance.
4. Install the module from the apps menu.

## Usage

1. Navigate to the pricelist import menu.
2. Click on the 'Import' button.
3. Select your Excel file and map the columns to the corresponding pricelist fields.
4. Click 'Import' to start the import process.

## Dependencies

- Odoo 16 CE
- Python `xlrd` library

## Sample Excel File

A sample Excel file is included in the module at `odoo_pricelist_import/data/sample_pricelist.xlsx`. This file demonstrates the required format for the Excel file.

## Testing

Tests for the module are included in `odoo_pricelist_import/tests/test_pricelist_import.py`.

## License

This module is released under a license compatible with Odoo CE.

## Support

If you encounter any issues or have questions about this module, please open an issue on the repository.