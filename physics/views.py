from django.shortcuts import render


def p_start(request):
    return render(request, 'physics/list.html')


# def ticket_view(request, id):
#     pages = MathImg.objects.filter(ticket__num=id).order_by('pos')
#     for p in pages:
#         print(p.image.url)
#     return render(request, 'maths/watch.html', {'pages': pages})
