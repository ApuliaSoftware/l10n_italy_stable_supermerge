from openupgradelib import openupgrade  # pylint: disable=W7936


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env.cr,
        "l10n_it_fatturapa_import_zip",
        "migrations/13.0.1.0.0/noupdate_changes.xml",
    )
