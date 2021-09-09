from django.views.generic import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from app.models import Store


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = '/accounts/login/'

class StoreView(View):
    def get(self, request, *args, **kwargs):
        store_data = Store.objects.all()

        return render(request, 'app/store.html', {
            'store_data': store_data,
        })