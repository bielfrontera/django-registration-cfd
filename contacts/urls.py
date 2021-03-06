from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',

    url(r'^people/add/$',
        view = 'person.create',
        name = 'contacts_person_create',
    ),

    url(r'^people/export/$',
        view = 'person.export',
        name = 'contacts_person_export',
    ),

    url(r'^people/import/$',
        view = 'person.importCSV',
        name = 'contacts_person_import',
    ),

    url(r'^people/synchronize/$',
        view = 'person.synchronizeSPIPForm',
        name = 'contacts_person_synchronize',
    ),

    url(r'^people/map/$',
        view = 'person.map',
        name = 'contacts_person_map',
    ),

    url(r'^people/lookup/$',
        view = 'person.lookup',
        name = 'contacts_person_lookup',
    ),
    url(r'^people/stats/$',
        view = 'stats.inscription',
        name = 'contacts_stats_inscription',
    ),
    url(r'^people/updateStatus/$',
        view = 'person.updateStatus',
        name = 'contacts_person_updatestatus',
    ),
    url(r'^people/(?P<slug>[-\w]+)/delete/$',
        view = 'person.delete',
        name = 'contacts_person_delete'
    ),
    url(r'^people/(?P<slug>[-\w]+)/edit/$',
        view = 'person.update',
        name = 'contacts_person_update'
    ),
    url(r'^people/(?P<slug>[-\w]+)/cancel/$',
        view = 'person.cancel',
        name = 'contacts_person_cancel'
    ),
    url(r'^people/(?P<slug>[-\w]+)/justificantPagament.pdf$',
        view = 'reporting.justificantPagament',
        name = 'contacts_person_justificantpagament'
    ),
    url(r'^people/(?P<slug>[-\w]+)/justificantRegistre.pdf$',
        view = 'reporting.justificantRegistre',
        name = 'contacts_person_justificantregistre'
    ),
    url(r'^people/(?P<slug>[-\w]+)/mailjustificantpagament$',
        view = 'reporting.mailJustificantPagament',
        name = 'contacts_person_mailjustificantpagament'
    ),
    url(r'^people/(?P<slug>[-\w]+)/mailpagamentretrasat$',
        view = 'reporting.mailPagamentRetrasat',
        name = 'contacts_person_mailpagamentretrasat'
    ),
    url(r'^people/(?P<slug>[-\w]+)/mail/(?P<code>[-\w]+)$',
        view = 'reporting.mail',
        name = 'contacts_person_mail'
    ),
    url(r'^people/(?P<id>[-\d]+)/mailhistory/$',
        view = 'mailhistory.mail_history',
        name = 'contacts_person_mailhistory'
    ),

    url(r'^people/(?P<slug>[-\w]+)/$',
        view = 'person.detail',
        name = 'contacts_person_detail',
    ),

    url(r'^people/$',
        view = 'person.list',
        name = 'contacts_person_list',
    ),

    url(r'^mailtemplate/add/$',
        view = 'mailtemplate.create',
        name = 'contacts_mailtemplate_create',
    ),

    url(r'^mailtemplate/lookup/$',
        view = 'mailtemplate.lookup',
        name = 'contacts_mailtemplate_lookup',
    ),

    url(r'^mailtemplate/(?P<code>[-\w]+)/delete/$',
        view = 'mailtemplate.delete',
        name = 'contacts_mailtemplate_delete'
    ),
    url(r'^mailtemplate/(?P<code>[-\w]+)/edit/$',
        view = 'mailtemplate.update',
        name = 'contacts_mailtemplate_update'
    ),
    url(r'^mailtemplate/(?P<code>[-\w]+)/copy/$',
        view = 'mailtemplate.copy',
        name = 'contacts_mailtemplate_copy'
    ),

    url(r'^mailtemplate/(?P<code>[-\w]+)/$',
        view = 'mailtemplate.detail',
        name = 'contacts_mailtemplate_detail',
    ),

    url(r'^mailtemplate/$',
        view = 'mailtemplate.list',
        name = 'contacts_mailtemplate_list',
    ),

    url(r'^course/add/$',
        view = 'course.create',
        name = 'contacts_course_create',
    ),

    url(r'^course/lookup/$',
        view = 'course.lookup',
        name = 'contacts_course_lookup',
    ),

    url(r'^course/(?P<code>[-\w]+)/delete/$',
        view = 'course.delete',
        name = 'contacts_course_delete'
    ),
    url(r'^course/(?P<code>[-\w]+)/edit/$',
        view = 'course.update',
        name = 'contacts_course_update'
    ),
    url(r'^course/(?P<code>[-\w]+)/copy/$',
        view = 'course.copy',
        name = 'contacts_course_copy'
    ),

    url(r'^course/(?P<code>[-\w]+)/$',
        view = 'course.detail',
        name = 'contacts_course_detail',
    ),

    url(r'^course/$',
        view = 'course.list',
        name = 'contacts_course_list',
    ),


)
