# coding: utf-8

from django import forms
from django.forms import ModelForm, Form, TextInput, CheckboxSelectMultiple
from django.utils.translation import ugettext as _

from contacts.models import Person, LABORAL_LEVEL_CHOICES, MailTemplate, Course
from contacts.widgets import ColumnCheckboxSelectMultiple
from bootstrap_toolkit.widgets import BootstrapTextInput, BootstrapDateInput

from models import STATUS_CHOICES


class PersonCreateForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        for key in self.fields:
            if self.fields[key] and 'class' not in self.fields[key].widget.attrs:
                self.fields[key].widget.attrs['class'] = 'v%s' % self.fields[key].__class__.__name__

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'contact_type')


class PersonIdentificationForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['about'].widget.attrs['rows']  = 3
        self.fields['about'].widget.attrs['cols']  = 75
        self.fields['last_name'].widget.attrs['class']  = 'input-xlarge'
        self.fields['id_card'].widget.attrs['class']  = 'input-small'

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'nickname','about','id_card',)

class PersonRegistrationForm(ModelForm):

    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['date_registration'].widget.format = '%d/%m/%Y'
        self.fields['date_registration'].input_formats = ['%d/%m/%Y']
        self.fields['date_registration'].widget.attrs['class']  = 'input-small'

        self.fields['date_paid'].widget.format = '%d/%m/%Y'
        self.fields['date_paid'].input_formats = ['%d/%m/%Y']
        self.fields['date_paid'].widget.attrs['class']  = 'input-small'
        self.fields['math_society'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['remarks'].widget.attrs['rows']  = 3
        self.fields['remarks'].widget.attrs['cols']  = 60
        self.fields['remarks'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['paid'].widget = BootstrapTextInput(append='€')
        self.fields['paid'].widget.attrs['class']  = 'input-mini'
        # self.fields['lang'].widget.attrs['class']  = 'input-medium'
        self.fields['courses'].widget  = forms.CheckboxSelectMultiple()
        self.fields['courses'].help_text = ''

    class Meta:
        model = Person
        fields = ('contact_type','courses','math_society','date_registration','revision','paid','date_paid','remarks')

class PersonAddressForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['phone_number'].widget.attrs['class']  = 'input-small'
        self.fields['mobile_number'].widget.attrs['class']  = 'input-small'
        self.fields['twitter'].widget.attrs['class']  = 'input-medium'
        self.fields['phone_number'].widget.attrs['class']  = 'input-small'
        self.fields['home_postalcode'].widget.attrs['class']  = 'input-mini'
        self.fields['home_address'].widget.attrs['class']  = 'input-xxlarge'


    class Meta:
        model = Person
        fields = ('email_address','phone_number','mobile_number','twitter','home_address','home_postalcode','home_town','home_province',)




class PersonLaboralForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['laboral_category'].widget.attrs['class']  = 'input-xxlarge'
        # self.fields['laboral_levels'] = forms.MultipleChoiceField(choices=LABORAL_LEVEL_CHOICES, required=False, widget=forms.CheckboxSelectMultiple())
        self.fields['laboral_cuerpo'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['laboral_degree'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['laboral_centername'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['laboral_centercode'].widget.attrs['class']  = 'input-small'
        self.fields['laboral_centeraddress'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['laboral_centerpostalcode'].widget.attrs['class']  = 'input-mini'
        self.fields['laboral_centerphone'].widget.attrs['class']  = 'input-small'
        self.fields['laboral_years'].widget.attrs['class']  = 'input-mini'

    # laboral_levels = forms.MultipleChoiceField(choices=LABORAL_LEVEL_CHOICES, required=False, widget=ColumnCheckboxSelectMultiple())


    class Meta:
        model = Person
        fields = ('laboral_category','laboral_nrp','laboral_years','laboral_cuerpo','laboral_degree',
                  'laboral_centername','laboral_centercode','laboral_centeraddress','laboral_centerpostalcode','laboral_centertown','laboral_centerprovince',
                  'laboral_centerphone')

class PersonLaboralLevelsForm(Form):
    laboral_levels = forms.MultipleChoiceField(label=_('laboral levels'),choices=LABORAL_LEVEL_CHOICES, required=False, widget=ColumnCheckboxSelectMultiple())


FILTERCONTACT_TYPE_CHOICES = (
    ('', ''),
    ('R', _('Registrant')),
    ('G', _('Guest')),
    ('S', _('Sponsor')),
    ('O', _('Organizer')),
)

FILTERREVISION_CHOICES = (
    ('', ''),
    ('dataok', _('Data ok')),
    ('datanook', _('Incorrect data')),
    ('missdata', _('Missed data')),
    ('unknown', _('Unknown person'))
)

class PersonFilterForm(Form):
    COURSE_CHOICES = tuple ( (obj.id, "%s %s" % (obj.code,obj.title)) for obj in Course.objects.all() )

    last_name = forms.CharField(label=_('last name'),required = False)
    contact_type = forms.ChoiceField(label=_('contact type'),required = False, choices = FILTERCONTACT_TYPE_CHOICES )
    id_card = forms.CharField(label=_('ID card'),required = False)
    status = forms.ChoiceField(label=_('status'),required = False, choices =  ( ('', ''),) + STATUS_CHOICES )
    course = forms.ChoiceField(label=_('course'),required = False, choices =  ( ('', ''),) + COURSE_CHOICES )
    mailnotpaid_unsent = forms.BooleanField(label=_('mail not paid unsent'),required = False)
    mailregister_unsent = forms.BooleanField(label=_('mail registration unsent'),required = False)


class ImportCSVForm(Form):
    fitxer = forms.FileField(label='Fitxer CSV')

class SynchronizeSPIPForm(Form):
    confirma = forms.BooleanField(required=True)

STATS_CHOICES = (
    ('', ''),
    ('contact_type', _('contact type')),
    ('math_society', _('math society')),
    ('province', _('province')),
    ('course', _('Course')),
    # ('lang', _('lang')),

)

class StatsForm(Form):
    stats_by = forms.ChoiceField(label=_('stats by'),required = False, choices =  STATS_CHOICES )


class MailTemplateForm(ModelForm):
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['body'].widget.attrs['rows']  = 8
        self.fields['body'].widget.attrs['cols']  = 75
        self.fields['body'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['description'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['subject'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['attachment'].widget.attrs['class']  = 'input-large'
        self.fields['attachment2'].widget.attrs['class']  = 'input-large'

    class Meta:
        model = MailTemplate
        fields = ('code','description','subject','body','attachment','attachment2')

class CourseForm(ModelForm):
    url_moodle = forms.URLField(label='URL', initial='http://')
    def __init__(self,*args,**kwrds):
        super(ModelForm,self).__init__(*args,**kwrds)
        self.fields['description'].widget.attrs['rows']  = 8
        self.fields['description'].widget.attrs['cols']  = 75
        self.fields['description'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['title'].widget.attrs['class']  = 'input-xxlarge'
        self.fields['url_moodle'].widget.attrs['class']  = 'input-xxlarge'

    class Meta:
        model = Course
        fields = ('code','title','url_moodle','description')
