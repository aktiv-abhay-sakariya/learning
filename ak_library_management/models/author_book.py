# -*- coding: utf-8 -*-
# Part of Aktiv software. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class AuthorBook(models.Model):
    _name = 'author.book'
    _description = "Author Books"

    book_id = fields.Many2one(comodel_name = 'library.book', string = 'Book', required=True)
    author_id = fields.Many2one(comodel_name = 'author.author', string = 'Author')
    isbn = fields.Char(string = 'ISBN Number',related = 'book_id.isbn', readonly = False)
    publication_date = fields.Date(string = 'Date of Publication',
                                   related = 'book_id.publication_date',
                                   readonly = False)
    price = fields.Float(string = 'Book Price', related = 'book_id.price', readonly = False)
