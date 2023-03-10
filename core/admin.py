from django.contrib import admin
from .models import Item, OrderItem, Order, Address, Payment, ItemReview
from .models import Contact

import datetime

from django.urls import reverse
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .models import Order, OrderItem

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'phone_number',
        'default'
    ]
    list_filter = ['default']
    search_fields = ['user__username', 'street_address', 'apartment_address']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','slug','description','price','discount_price','is_featured', 'num_available']
    search_fields = ['title','slug','price','discount_price','is_featured', 'num_available']

    def set_price_to_one(self,request,queryset):
        queryset.update(price=1)

    actions =['set_price_to_one',]
    list_editable = ['price','slug','description','is_featured', 'num_available']



def order_name(obj):
    return '%s %s' % (obj.user, obj.ref_code)
order_name.short_description = 'Name'

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))
order_name.short_description = 'PDF'

def admin_order_shipped(modeladmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        html = render_to_string('order_sent.html', {'order': order})
        send_mail('Order sent', 'Your order has been sent!', 'noreply@saulgadgets.com', ['mail@saulgadgets.com', order.email], fail_silently=False, html_message=html)
    return 
admin_order_shipped.short_description = 'Set shipped'



class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, order_pdf]
    list_filter = []
    search_fields = ['user',
					 'ref_code'
				]
    actions = [admin_order_shipped]

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(ItemReview)
admin.site.register(Contact)






