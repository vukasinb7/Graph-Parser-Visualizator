from django.apps.registry import apps
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import re

from .models import *


def index(request):
    visualization_plugins = apps.get_app_config('app_core').visualization_plugins
    parser_plugins = apps.get_app_config('app_core').parser_plugins
    return render(request, "index.html",
                  {"visualization_plugins": visualization_plugins, "parser_plugins": parser_plugins})


def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']

        with open("upload/" + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

            parser_plugins = apps.get_app_config('app_core').parser_plugins
            for key in parser_plugins.keys():
                if file.name.split(".")[-1] == parser_plugins[key]['ext']:
                    return redirect('/parser/' + parser_plugins[key]['ext'] + '/' + file.name)
    return HttpResponse("File upload unsuccessful!")


commands_dict = {"/search", "/reset", "/filter"}

operators = {"!=", "=<", ">=", "=", "<", ">"}


def _get_key_value_from_expression(expression):
    opr = None
    for operator in operators:
        if operator in expression:
            opr = operator
            break
    if opr is None:
        return

    print(opr)
    tokens = expression.split(opr)
    print(tokens)
    return tokens[0].strip(), tokens[1].strip(), opr


def parse_console_command(request):
    view: str = request.GET.get('view')
    command_line: str = request.GET.get('value')

    tokens = command_line.strip().split(' ', 1)
    command = tokens[0].strip()
    try:
        params = tokens[1]
    except:
        params = None

    if command not in commands_dict:
        return redirect('/layout/' + view)

    if command == "/search":
        if params is None:
            return redirect('/layout/' + view)
        Node.objects.exclude(data__key__icontains=params).exclude(data__value__icontains=params).update(
            is_visible=False)
        Edge.objects.filter(Q(first_node__is_visible=False) | Q(second_node__is_visible=False)).update(is_visible=False)
    elif command == "/filter":
        print("line 81")
        try:
            key, value, operator = _get_key_value_from_expression(params.strip())
        except:
            return redirect('/layout/' + view)
        print(key, value, operator)
        if operator == "!=":
            print("!=")
            Node.objects.exclude(Q(data__key__iexact=key), ~Q(data__value__iexact=value)).update(is_visible=False)
        elif operator == "<=":
            print("<=")
            Node.objects.exclude(Q(data__key__iexact=key), Q(data__value__lte=value)).update(is_visible=False)
        elif operator == ">=":
            print(">=")
            Node.objects.exclude(Q(data__key__iexact=key), Q(data__value__gte=value)).update(is_visible=False)
        elif operator == "=":
            print("=")
            Node.objects.exclude(Q(data__key__iexact=key), Q(data__value__iexact=value)).update(is_visible=False)
        elif operator == "<":
            print("<")
            Node.objects.exclude(Q(data__key__iexact=key), Q(data__value__lt=value)).update(is_visible=False)
        elif operator == ">":
            print(">")
            Node.objects.exclude(Q(data__key__iexact=key), Q(data__value__gt=value)).update(is_visible=False)
        Edge.objects.filter(Q(first_node__is_visible=False) | Q(second_node__is_visible=False)).update(is_visible=False)
    elif command == "/reset":
        Node.objects.all().update(is_visible=True)
        Edge.objects.all().update(is_visible=True)

    return redirect('/layout/' + view)
