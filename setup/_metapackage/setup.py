import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-l10n-italy",
    description="Meta package for oca-l10n-italy Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_vat_period_end_statement',
        'odoo14-addon-l10n_it_abicab',
        'odoo14-addon-l10n_it_account',
        'odoo14-addon-l10n_it_account_stamp',
        'odoo14-addon-l10n_it_account_tax_kind',
        'odoo14-addon-l10n_it_appointment_code',
        'odoo14-addon-l10n_it_ateco',
        'odoo14-addon-l10n_it_central_journal',
        'odoo14-addon-l10n_it_delivery_note',
        'odoo14-addon-l10n_it_delivery_note_base',
        'odoo14-addon-l10n_it_delivery_note_batch',
        'odoo14-addon-l10n_it_delivery_note_order_link',
        'odoo14-addon-l10n_it_fatturapa',
        'odoo14-addon-l10n_it_fatturapa_in',
        'odoo14-addon-l10n_it_fatturapa_out',
        'odoo14-addon-l10n_it_fatturapa_out_stamp',
        'odoo14-addon-l10n_it_fiscal_document_type',
        'odoo14-addon-l10n_it_fiscal_payment_term',
        'odoo14-addon-l10n_it_fiscalcode',
        'odoo14-addon-l10n_it_ipa',
        'odoo14-addon-l10n_it_payment_reason',
        'odoo14-addon-l10n_it_pec',
        'odoo14-addon-l10n_it_rea',
        'odoo14-addon-l10n_it_split_payment',
        'odoo14-addon-l10n_it_vat_payability',
        'odoo14-addon-l10n_it_vat_registries',
        'odoo14-addon-l10n_it_vat_registries_split_payment',
        'odoo14-addon-l10n_it_vat_statement_communication',
        'odoo14-addon-l10n_it_vat_statement_split_payment',
        'odoo14-addon-l10n_it_withholding_tax',
        'odoo14-addon-l10n_it_withholding_tax_reason',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
