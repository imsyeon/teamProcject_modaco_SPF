from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notice
from django.db.models import Q


# Create your views here.
class NoticeList(ListView):
    model=Notice
    ordering = '-pk'

    # 페이징처리
    paginate_by=5
    template_name = 'notice/notice_list.html'
    context_object_name = 'notice_list'

    def get_queryset(self):
        notice_list = Notice.objects.order_by('-id')
        return notice_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context


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

def delete_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('/notice/')



class NoticeSearch(NoticeList):
#    paginate_by = None #페이징 설정되어있는것을 none으로 설정

    def get_queryset(self):
        q = self.kwargs['q']
        notice_list = Notice.objects.filter(
            Q(subject__contains=q)
        ).distinct()
        return notice_list

    def get_context_data(self, **kwargs):
        context = super(NoticeSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context