import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.addons.asterisk_plus.models.settings import debug


logger = logging.getLogger(__name__)


class CrmChannel(models.Model):
    _inherit = 'asterisk_plus.channel'

    @api.model
    def on_ami_hangup(self, event):
        chan_id = super().on_ami_hangup(event)
        channel = self.env['asterisk_plus.channel'].browse(chan_id)
        if channel.call:
            try:
                channel.call._auto_create_lead()
            except Exception:
                logger.exception('Error atuo creating lead:')
        return chan_id

