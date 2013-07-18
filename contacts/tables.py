import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from django.utils.translation import ugettext as _
from contacts.models import Person, MailTemplate, Course



class PersonTable(tables.Table):
    template_actions = "<div style='width: 75px;'><a href='{{ record.get_update_url }}' title='Edit'><i class='icon-edit'></i></a> " + \
        "<a href='{{ record.get_absolute_url }}' title='Read'><i class='icon-eye-open'></i></a> " + \
        "<a href='{{ record.get_delete_url }}'title='Delete'><i class='icon-trash'></i></a></div>"
    actions = tables.TemplateColumn(template_actions, sortable=False, verbose_name=_('Actions'))
    last_name = tables.LinkColumn('contacts_person_update',args=[A('slug')])
    first_name = tables.Column()
    contact_type = tables.TemplateColumn('{{ record.get_contact_type_display }}')
    email = tables.TemplateColumn('<a href="mailto:{{ record.email_address }}">{{ record.email_address }}</a>', sortable=False, verbose_name=_('email address'))
    # home_town = tables.Column()
    # math_society = tables.Column()
    math_society = tables.TemplateColumn('{{ record.get_math_society_display_mini }}')
    # date_registration = tables.TemplateColumn('{{ record.date_registration|date:"d/m/Y" }}', sortable=False, verbose_name=_('date registration'))
    date_registration = tables.DateColumn()
    paid = tables.Column()
    status  = tables.TemplateColumn('<span class="label label-{{ record.get_label }}">{{ record.get_status_display }}</span>', sortable=False, verbose_name=_('status'))

    # external_id = tables.Column()

class MailTemplateTable(tables.Table):
    template_actions = "<div style='width: 75px;'><a href='{{ record.get_update_url }}' title='Edit'><i class='icon-edit'></i></a> " + \
        "<a href='{{ record.get_absolute_url }}' title='Read'><i class='icon-eye-open'></i></a> " + \
        "<a href='{{ record.get_delete_url }}'title='Delete'><i class='icon-trash'></i></a></div>"
    actions = tables.TemplateColumn(template_actions, sortable=False, verbose_name=_('Actions'))
    code = tables.LinkColumn('contacts_mailtemplate_update',args=[A('code')])
    description = tables.Column()
    subject = tables.Column()
    attachment = tables.Column()
    attachment2 = tables.Column()


class ExportPersonTable(tables.Table):
    status = tables.TemplateColumn('{{ record.get_status_display }}')
    contact_type = tables.TemplateColumn('{{ record.get_contact_type_display }}')
    first_name = tables.Column()
    last_name = tables.Column()
    email_address = tables.Column(verbose_name=_('email address'))
    courses = tables.TemplateColumn('{{ record.get_courses_display }}')

    id_card = tables.Column(verbose_name=_('DNI'))

    home_address = tables.Column()
    home_postalcode = tables.Column()
    home_town = tables.Column()
    home_province = tables.Column()

    phone_number = tables.Column()
    mobile_number = tables.Column()
    math_society = tables.TemplateColumn('{{ record.get_math_society_display_mini }}')

    date_modified = tables.TemplateColumn('{{ record.date_modified|date:"Y/m/d" }}')



class CourseTable(tables.Table):
    template_actions = "<div style='width: 75px;'><a href='{{ record.get_update_url }}' title='Edit'><i class='icon-edit'></i></a> " + \
        "<a href='{{ record.get_absolute_url }}' title='Read'><i class='icon-eye-open'></i></a> " + \
        "<a href='{{ record.get_delete_url }}'title='Delete'><i class='icon-trash'></i></a></div>"
    actions = tables.TemplateColumn(template_actions, sortable=False, verbose_name=_('Actions'))
    code = tables.LinkColumn('contacts_course_update',args=[A('code')])
    title = tables.Column()
    url_moodle = tables.TemplateColumn("<a href='{{ record.url_moodle }}'>{{ record.url_moodle }}</a>",sortable=False)


