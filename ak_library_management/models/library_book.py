# -*- coding: utf-8 -*-
# Part of Aktiv software. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = "Books"

    name = fields.Char(string = "Book Title", required = True)
    isbn = fields.Char(string = 'ISBN Number', required = True)
    publication_date = fields.Date(string = 'Date of Publication', required = True)
    price = fields.Float(string = 'Book Price', required = True)
    pages = fields.Integer(string = 'Number of Pages')
    description = fields.Html(string = 'Book Summary')
    image_1920 = fields.Image(string = 'Book Image')
    category_id = fields.Many2one(comodel_name = 'book.category', string = 'Category')
    edition_ids = fields.Many2many(comodel_name = 'book.edition', string = 'Edition')
