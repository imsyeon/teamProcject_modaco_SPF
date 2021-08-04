from django.shortcuts import render
from django.views.generic import ListView
<<<<<<< Updated upstream
from .models import KospiData, Kosdaq, Report, Capitalzation, Kospicap
=======
from .models import KospiData, Kosdaq, Report
>>>>>>> Stashed changes


# Create your views here.
class KospiList(ListView):
    model = KospiData
<<<<<<< Updated upstream

=======
    ordering = '-pk'
>>>>>>> Stashed changes


    # 페이징처리
    paginate_by = 10
    template_name = 'stock/kospidata_list.html'
    context_object_name = 'kospidata_list'

    def get_queryset(self):
<<<<<<< Updated upstream
        kospi_list = KospiData.objects.order_by('-kospi_date')
=======
        kospi_list = KospiData.objects.order_by('-id')
>>>>>>> Stashed changes
        return kospi_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
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

class KosdaqList(ListView):
    model = Kosdaq
<<<<<<< Updated upstream
=======
    ordering = '-pk'
>>>>>>> Stashed changes

    # 페이징처리
    paginate_by = 10


    def get_queryset(self):
<<<<<<< Updated upstream
        kospi_list = Kosdaq.objects.order_by('-kosdaq_date')
=======
        kospi_list = Kosdaq.objects.order_by('-id')
>>>>>>> Stashed changes
        return kospi_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
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

class ReportList(ListView):
    model = Report
<<<<<<< Updated upstream

=======
    ordering = '-pk'
>>>>>>> Stashed changes

    # 페이징처리
    paginate_by = 5

<<<<<<< Updated upstream
    def get_queryset(self):
        kospi_list = Report.objects.order_by('-report_date')
        return kospi_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
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

class CapitalzationList(ListView):
    model = Capitalzation


    # 페이징처리
    paginate_by = 50


    def get_queryset(self):
        kospi_list = Capitalzation.objects.order_by('-stockCap')
        return kospi_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
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

class KospicapList(ListView):
    model = Kospicap


    # 페이징처리
    paginate_by = 50


    def get_queryset(self):
        kospi_list = Kospicap.objects.order_by('-stockCap')
=======

    def get_queryset(self):
        kospi_list = Report.objects.order_by('-id')
>>>>>>> Stashed changes
        return kospi_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index
<<<<<<< Updated upstream

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

=======

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context
>>>>>>> Stashed changes
