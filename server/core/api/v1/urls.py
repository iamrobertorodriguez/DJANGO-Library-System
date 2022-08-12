from book.urls import urls as book_urls
from user.urls import urls as user_urls
from category.urls import urls as category_urls
from shelf.urls import urls as shelf_urls
from invoice.urls import urls as invoice_urls

urlpatterns = book_urls + user_urls + category_urls + shelf_urls + invoice_urls