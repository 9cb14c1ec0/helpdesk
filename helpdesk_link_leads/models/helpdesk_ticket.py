# Copyright 2022 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def create(self, vals):
        if vals.get("partner_email"):
            # search existing tickets for same email
            existing_tickets = self.search(
                [("partner_email", "=", vals["partner_email"])]
            )
            if existing_tickets:
                vals["related_ticket_ids"] = existing_tickets
        return super(HelpdeskTicket, self).create(vals)