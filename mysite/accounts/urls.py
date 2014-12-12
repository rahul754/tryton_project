
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/invoices/(\d+)/download$', 'accounts.views.download_invoice'),
    url(r'^accounts/invoices/(\d+)/$', 'accounts.views.view_invoice_detail'),
    url(r'^accounts/invoices/$', 'accounts.views.view_invoices'),


)
