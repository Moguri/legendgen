from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core import serializers

from collections import OrderedDict

from cgen.models import Character, ClassChassis, Race, ATT_VALUES


def index(request):
    clist = Character.objects.all()
    context = {'char_list': clist}
    return render(request, 'cgen/index.html', context)

def detail(request, cid):
    char = get_object_or_404(Character, pk=cid)
    attribs = OrderedDict()
    for i in ATT_VALUES:
        attribs[i[0].lower()] = (i[1], getattr(char, i[0].lower()))
    return render(request, 'cgen/detail.html', {
		'char': char,
		'classes': ClassChassis.objects.all(),
        'races': Race.objects.all(),
		'attribs': attribs,
	})

def new(request):
    char = Character(class_chassis=ClassChassis.objects.all()[:1].get(),
                     race=Race.objects.all()[:1].get())
    char.save()
    return HttpResponseRedirect(reverse('cgen:detail', args=(char.id,)))

def delete(request, cid):
    char = get_object_or_404(Character, pk=cid)
    char.delete()

    return HttpResponseRedirect(reverse('cgen:index'))

def save(request, cid):
    char = get_object_or_404(Character, pk=cid)

    # Details
    char.cname = request.POST['cname']
    char.pname = request.POST['pname']
    try:
        class_chassis = ClassChassis.objects.get(pk=request.POST['class_chassis'])
    except (KeyError, ClassChassis.DoesNotExist):
        return render(request, 'cgen/detail.html', {
            'char': char,
            'classes': ClassChassis.objects.all(),
            'error_message': "Invalid class chassis.",
        })

    char.class_chassis = class_chassis

    # Attributes
    for i in [i[0].lower() for i in ATT_VALUES]:
        setattr(char, i, request.POST[i])

    char.save()

    return HttpResponseRedirect(reverse('cgen:detail', args=(char.id,)))
    
def get_class(request, ccid):
    cc = get_object_or_404(ClassChassis, pk=ccid)
    return HttpResponse(serializers.serialize('json', (cc,)))
