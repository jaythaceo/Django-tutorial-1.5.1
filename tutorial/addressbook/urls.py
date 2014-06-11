from django.conf.urls import patterns, include, url

import contacts.views

urlpatterns = patterns('',
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contact-list',),
        ),
url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new',
        ),
