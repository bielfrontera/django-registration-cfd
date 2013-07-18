from django.core.management.base import NoArgsCommand, make_option

from django.core.mail import EmailMessage
from django.template.context import Context
from django.template.loader import render_to_string
from django.conf import settings
from contacts.models import Person, Course
from django.utils.translation import ugettext as _
from django.template.defaultfilters import date as _date
from datetime import date, datetime, timedelta
from django.utils import translation


import StringIO, os
from xhtml2pdf import pisa




class Command(NoArgsCommand):

    help = "Whatever you want to print here"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )


    def handle_noargs(self, **options):
        print "Testing"
        person_list = Person.objects.all()
        # person_list = person_list.filter(status='ok_all')
        person_list = person_list.filter(date_modified__gt=datetime.today() - timedelta(days=3))

        translation.activate('es')
        avui = _date(datetime.now(), "d \d\e F \d\e Y")


        for person in person_list:
            for course in person.courses.all():

                context = {
                    'object' : person,
                    'course' : course,
                    'avui' : avui
                }
                output_filename = 'generated_files/fitxaMEC/%s_ficha_participantes_%s.pdf' % (course.code, person.slug)
                if not os.path.isfile(output_filename):
                    html = render_to_string('contacts/person/ficha_participantes_mec.html',context)
                    result = file(output_filename,'wb')
                    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),
                                                            dest=result,
                                                            link_callback=fetch_resources)
                    result.close()
                    print "%s generated" % output_filename

                    if pdf.err:
                        raise Exception('Error generating pdf. %d errors' % pdf.err )


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path