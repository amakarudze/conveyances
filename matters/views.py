from django.shortcuts import render

from .stages import create_conveyance_object, matters

matters = [
    'transfer',
    'mortgage_bond',
    'mortgage_bond_other_lawyers',
    'lost_deed_application',
    ['mortgage_bond_cancellation']
]


def index(request):
    pass


def create_matter(request):
    pass


def update_matter(request):
    pass
