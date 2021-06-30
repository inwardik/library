from django.shortcuts import render, redirect
from .models import Order
from authentication.models import CustomUser
from book.models import Book
from datetime import datetime, timedelta


def create_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        user = CustomUser.get_by_id(user_id)
        book = Book.get_by_id(book_id)
        plated_end_at = request.POST.get('plated_end_at')
        Order.create(user, book, plated_end_at)
        return redirect('orders_list')

    users = CustomUser.objects.all()
    books = Book.objects.all()
    plated_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    return render(request, 'order/create_order.html', {'users': users, 'books': books, 'plated_date': plated_date})


def orders_list(request):
    orders = Order.get_all()
    return render(request, 'order/orders_list.html', {'orders': orders, 'is_all': True})


def not_returned(request):
    orders = Order.get_not_returned_books()
    return render(request, 'order/orders_list.html', {'orders': orders, 'is_all': False})


def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('orders_list')


def edit_order(request, order_id):
    order = Order.get_by_id(order_id)
    if request.method == 'POST':
        plated_end_at = request.POST.get('plated_end_at')
        end_at = request.POST.get('end_at')
        order.update(plated_end_at, end_at)
        return redirect('orders_list')
    else:
        return render(request, 'order/edit_order.html', {'order': order})