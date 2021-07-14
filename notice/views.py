from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Notice


# Create your views here.
class NoticeList(ListView):
    model=Notice
    ordering = '-pk'

class NoticeDetail(DetailView):
    model=Notice

class NoticeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['subject', 'content', 'head_image', 'file_upload']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(NoticeCreate, self).form_valid(form)
        else:
            return redirect('/notice/')

class NoticeUpdate(LoginRequiredMixin, UpdateView):
    model=Notice
    fields=['subject', 'content', 'head_image', 'file_upload']

    template_name = 'notice/notice_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(NoticeUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied