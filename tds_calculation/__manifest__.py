{
    'name': 'TDS Calculation',
    'version': '2.0',
    'category': 'TDS',
    'summary': 'TDS Functionality',
    'description': """
This module adds support for barcode scanning and parsing.

Scanning
--------
Use a USB scanner (that mimics keyboard inputs) in order to work with barcodes in Odoo.
The scanner must be configured to use no prefix and a carriage return or tab as suffix.
The delay between each character input must be less than or equal to 50 milliseconds.
Most barcode scanners will work out of the box.
However, make sure the scanner uses the same keyboard layout as the device it's plugged in.
Either by setting the device's keyboard layout to US QWERTY (default value for most readers)
or by changing the scanner's keyboard layout (check the manual).

Parsing
-------
The barcodes are interpreted using the rules defined by a nomenclature.
It provides the following features:
- Patterns to identify barcodes containing a numerical value (e.g. weight, price)
- Definition of barcode aliases that allow to identify the same product with different barcodes
- Support for encodings EAN-13, EAN-8 and UPC-A
""",
    'depends': ['stock','product','purchase','account'],
    'data': [
        'views/tds_group_settings_view.xml',
        'views/tds_mapping.xml',
        'views/tds_group.xml',
        'views/tds_section.xml',
        'views/assesse_code.xml',
        'views/concession_code.xml',
        'views/tds_nod.xml',
        'views/nod_configuration.xml',
        'views/account_invoice.xml',

        'views/res_partner.xml',
        'views/purchase.xml'
    ],
    'installable': True,
    'auto_install': False,
}
