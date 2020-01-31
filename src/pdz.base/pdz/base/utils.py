import os



def render_to_pdf_response(template_name, context=None, pdfname=None):
    from django_xhtml2pdf.utils import render_to_pdf_response

    response = render_to_pdf_response(template_name, context=context, pdfname=pdfname)
    response['Content-Length'] = str(len(response.content))
    # response['Content-Type'] = "application/octet-stream"

    return response