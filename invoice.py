# This file is part account_invoice_reference_required module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta, Pool
from trytond.i18n import gettext
from trytond.exceptions import UserWarning


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'

    @classmethod
    def set_number(cls, invoices):
        pool = Pool()
        Warning = pool.get('res.user.warning')

        super().set_number(invoices)

        for invoice in invoices:
            if invoice.type != 'in':
                continue
            if not invoice.reference:
                warning_key = Warning.format('invoice_no_reference', [invoice])

                if Warning.check(warning_key):
                    raise UserWarning(warning_key, gettext(
                        'account_invoice_reference_required.msg_no_reference_found',
                        invoice=invoice.rec_name))

