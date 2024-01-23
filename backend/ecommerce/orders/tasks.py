from celery import shared_task
import datetime
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Zamówienie nr {order.id}"
    message = f"Witaj, {order.first_name}!\n\nZłożyłeś zamówienie w naszym sklepie. Identyfikator zamówienia to {order.id}."
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent


@shared_task
def send_payment_reminder_email():
    today = datetime.now()
    order = Order.objects.filter(pay_day__date=today)
    subject = f"Płatność za zamówienie nr {order.id}"
    message = f"Witaj, {order.first_name}!\n\nPrzyszedł czas aby zapłacić za zamówienie {order.id}."
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
