from odoo import models, fields, api


class Task(models.Model):
    _name = "cooperative_shop.task"
    _description = "Task Model"

    name = fields.Char()
    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    occurrences = fields.Integer()
    description = fields.Text()
    task_type = fields.Selection(
        [
            ("farming", "Farming"),
            ("shop", "Shop"),
            ("harvest", "Harvest"),
        ]
    )
