from cgitb import html
from io import BytesIO
from re import template
from unittest import result
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def resume_pdf(request):
    pdf = render_to_pdf('resume_pdf.html')
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        # content = "inline; filename=developer_resume.pdf"
        response['Content-Disposition'] = "attachment; filename=resume.pdf"
        return response
    return HttpResponse('Not Found !')