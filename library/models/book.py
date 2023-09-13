from odoo import models, fields


class Book(models.Model):
    _name = "library.book"
    _description = "Book Model"

    name = fields.Char()
    active = fields.Boolean(Default=True)
    isbn = fields.Char()
    genre = fields.Char()
    summary = fields.Text()
    author = fields.Char()
    book_format = fields.Selection(
        [
            ("paperback", "Paperback"),
            ("hardcover", "Hardcover"),
            ("audiobook", "Audiobook"),
            ("e-book", "E-Book"),
        ]
    )
    language = fields.Selection(
        [
            ("en", "English"),
            ("es", "Spanish"),
            ("fr", "French"),
            ("de", "Deutsch"),
        ]
    )
    edition = fields.Integer()
    publisher = fields.Char()
    publish_date = fields.Date()
    price = fields.Float()
