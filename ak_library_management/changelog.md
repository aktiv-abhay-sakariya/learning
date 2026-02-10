# Changelog
All notable changes to this project will be documented in this file.

[19.0.1.0.0] :
- Initial release of the Library Management module.
- Added two models: 1)library.book 2)book.category
- Added list, form and search views on book's window.
- Added list and form(default) view on category's window.

[19.0.1.1.0] :
- Added three models: 1)book.edition 2)author.book 3)author.author
- Added list, form (default) views on book edition's window.
- Added list and form view on author's window.
- Added relations :
    1. Many2one :  book.category-book.category, library.book-book.category, author.book-library.book
    2. Many2many : library.book-book.edition
    3. One2many : author.author-author.book

[19.0.1.1.1] :
- Updated module follow standard Odoo version format.
- Renamed model class name.
- Added Header comments.
- Created separate XML view files and make some form views.
- Remove unnecessary fields (book_ids) in book.editions model.

[19.0.1.1.2] :
- Added widget in XML views files.
- Added search views for Author, Category and Edition models.
- Removed _res_name attribute.
- Renamed the XML view files using or following Odoo standards