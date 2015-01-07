from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response

def view_invoices(request):
    context = {}
    try:
        party_id = request.user.get_profile().tryton_id
    except:
        party_id = False
    if settings.ENABLE_TRYTON and party_id:
        from tryton import POOL, DB, USER
        from trytond.tools import Cache
        invoice_obj = POOL.get('account.invoice')
        cursor = DB.cursor()
        Cache.clean(POOL.database_name)
        try:
            invoice_ids = invoice_obj.search(cursor, USER, [('party', '=', party_id)])
            context['invoices'] = invoice_obj.browse(cursor, USER, invoice_ids)
            return render_to_response('my_invoices_template.html', context)
        finally:
            cursor.commit()
            Cache.resets(POOL.database_name)
    return render_to_response('my_invoices_template.html', context)




def view_invoice_detail(request, inv_id):
    inv_id = int(inv_id)
    context = {}
    try:
        party_id = request.user.get_profile().tryton_id
    except:
        party_id = False
    if settings.ENABLE_TRYTON and party_id:
        from tryton import POOL, DB, USER
        from trytond.tools import Cache
        try:
            cursor = DB.cursor()
            Cache.clean(POOL.database_name)
            invoice_obj = POOL.get('account.invoice')
            invoice = invoice_obj.browse(cursor, USER, inv_id)
            context['invoice'] = invoice
            return render_to_response('invoice_detail.html', context)
        finally:
            cursor.commit()
            Cache.resets(POOL.database_name)
    return render_to_response('invoice_detail.html', context)




def download_invoice(request, inv_id):
    inv_id = int(inv_id)
    try:
        party_id = request.user.get_profile().tryton_id
    except:
        party_id = False
    if settings.ENABLE_TRYTON and party_id:
        import base64
        try:
            import cStringIO as StringIO
        except ImportError:
            import StringIO
        from tryton import POOL, DB, USER
        from trytond.tools import Cache
        invoice_obj = POOL.get('account.invoice', type='report')
        cursor = DB.cursor()
        Cache.clean(POOL.database_name)
        try:
            format, report, _, file_name = invoice_obj.execute(cursor,
                    USER, [inv_id], {'id': inv_id, 'ids': [inv_id]})
        finally:
            cursor.close()
            Cache.resets(POOL.database_name)
        reportIO = StringIO.StringIO()
        reportIO.write(base64.decodestring(report))
        wrapper = FileWrapper(reportIO)
        content_type = {
            'odt': 'application/vnd.oasis.opendocument.text',
            'pdf': 'application/pdf',
            }.get(format, 'application/octet-stream')
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename=%s.%s' % \
                (file_name, format)
        response['Content-Length'] = reportIO.tell()
        reportIO.close()
        return response
    return view_invoice_detail(request, inv_id)
