# coding: utf-8

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.utils.html import escape
from contacts.models import Course
from contacts.forms import CourseForm
from contacts.tables import CourseTable
from django.utils import simplejson

from copy import deepcopy

def list(request, page=1, template='contacts/course/list.html'):
    """List of all the courses

    :param template: Add a custom template.
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    course_list = Course.objects.all()

    table = CourseTable(course_list, order_by = request.GET.get("sort",'code') )
    table.paginate(page=request.GET.get("page", 1))

    kwvars = {
        'table' : table
    }

    return render_to_response(template, kwvars, RequestContext(request))

def detail(request, code, template='contacts/course/detail.html'):
    """Detail of a course.

    :param template: Add a custom template.
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    try:
        course = Course.objects.get(code__iexact=code)
    except Course.DoesNotExist:
        raise Http404

    kwvars = {
        'object': course,
    }

    return render_to_response(template, kwvars, RequestContext(request))

def copy(request, code, template='contacts/course/create.html'):
    """Copia un course.

    :param template: Add a custom template.
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    user = request.user
    if not user.has_perm('add_course'):
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            p = form.save(commit=False)
            p.user_add = user
            p.user_modify = user
            p.save()
            return HttpResponseRedirect(p.get_update_url())
    else:
        try:
            course = Course.objects.get(code__iexact=code)
        except Course.DoesNotExist:
            raise Http404

        new_course = deepcopy(course)
        new_course.id = None
        new_course.code = "%s_cp" % course.code

        form = CourseForm(instance=new_course)

    kwvars = {
        'form': form,
    }

    return render_to_response(template, kwvars, RequestContext(request))


def create(request, template='contacts/course/create.html'):
    """Create a course.

    :param template: A custom template.
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    user = request.user
    if not user.has_perm('add_course'):
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            p = form.save(commit=False)
            p.user_add = user
            p.user_modify = user
            p.save()
            return HttpResponseRedirect(p.get_update_url())
    else:
        form = CourseForm()

    kwvars = {
        'form': form
    }

    return render_to_response(template, kwvars, RequestContext(request))


def update(request, code, template='contacts/course/update.html'):
    """Update a course.

    :param template: A custom template.
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    user = request.user
    if not user.has_perm('change_course'):
        #todo: posar al missatge que no es pot realitzar l'accio si no es te permis
        return detail(request,code)

    try:
        course = Course.objects.get(code__iexact=code)
    except Course.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            course.user_modify = user
            form.save()
            return HttpResponseRedirect(course.get_absolute_url())
    else:
        form = CourseForm(instance=course)

    kwvars = {
        'form': form,
        'object': course,
    }

    return render_to_response(template, kwvars, RequestContext(request))

def delete(request, code, template='contacts/course/delete.html'):
    """Delete a course.

    :param template: A custom template.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    user = request.user
    if not user.has_perm('delete_course'):
        return HttpResponseForbidden()

    try:
        course = Course.objects.get(code__iexact=code)
    except Course.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        new_data = request.POST.copy()
        if new_data['delete_course'] == 'Yes':
            course.delete()
            return HttpResponseRedirect(reverse('contacts_course_list'))
        else:
            return HttpResponseRedirect(course.get_absolute_url())

    kwvars = {
        'object': course
    }

    return render_to_response(template, kwvars, RequestContext(request))

def lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'term'):
            value = request.GET[u'term']
            model_results = Course.objects.filter(code__istartswith=value)
        else:
            model_results = Course.objects.all()
        results = [ {'label' : x.title, 'value': x.code } for x in model_results ]

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

