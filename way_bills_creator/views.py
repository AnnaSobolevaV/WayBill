from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from way_bills_creator.forms import (
    CarForm,
    DriverForm,
    LocationForm,
    DistanceForm,
    WayBillForm,
)
from way_bills_creator.models import Car, Driver, Location, Distance, WayBill, Event
from way_bills_creator.services import (
    LogsService,
    CalendarService,
    period_list,
    year_list,
    CSVService,
    WaybillsService,
)


class ServiceView(LoginRequiredMixin, TemplateView):
    """Класс представлений для Сервиса Путевых листов"""

    template_name = "way_bills_creator/service.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data["log_str_list"] = LogsService.get_logs()
        context_data["period_list"] = period_list
        context_data["year_list"] = year_list

        return context_data


def create_waybills(request):
    """Метод обрабатывающий POST-запрос при создании Путевых листов за выбранный период"""
    if request.method == "POST":
        selected_period_wb = request.POST.get("selected_period_wb")
        selected_year_wb = request.POST.get("selected_year_wb")
        if selected_period_wb not in [
            "Выберите период",
            None,
        ] and selected_year_wb not in ["Выберите год", None]:
            WaybillsService.create_waybills(selected_period_wb, selected_year_wb)

    return redirect(reverse("way_bills_creator:home"))


def download_wbs_excel(request):
    """Метод обрабатывающий POST-запрос при выгрузке Путевых листов в excel за выбранный период"""
    if request.method == "POST":
        selected_period = request.POST.get("selected_period")
        selected_year = request.POST.get("selected_year")
        if selected_period not in ["Выберите период", None] and selected_year not in [
            "Выберите год",
            None,
        ]:
            WaybillsService.download_wbs_excel(selected_period, selected_year)

    return redirect(reverse("way_bills_creator:waybill_list"))


def download_report(request):
    """Метод обрабатывающий POST-запрос при выгрузке Отчетов в excel за выбранный период"""
    if request.method == "POST":
        selected_period_excel = request.POST.get("selected_period_excel")
        selected_year_excel = request.POST.get("selected_year_excel")
        if selected_period_excel not in [
            "Выберите период",
            None,
        ] and selected_year_excel not in ["Выберите год", None]:
            WaybillsService.download_report(selected_period_excel, selected_year_excel)

    return redirect(reverse("way_bills_creator:home"))


def download_events(request):
    """Метод обрабатывающий POST-запрос при загрузке Событий из TeamUp за выбранный период"""
    if request.method == "POST":
        selected_period = request.POST.get("selected_period")
        selected_year = request.POST.get("selected_year")
        if selected_period not in ["Выберите период", None] and selected_year not in [
            "Выберите год",
            None,
        ]:
            CalendarService.download(selected_period, selected_year)

    return redirect(reverse("way_bills_creator:home"))


def upload_file_csv(request, what):
    """Метод обрабатывающий POST-запрос при загрузке
    Автомобилей, Водителей и Мест назначения из файлов формата csv за выбранный период
    """
    if request.method == "POST":
        if what == "cars":
            try:
                file = request.FILES["file_cars_csv"]
                CSVService.cars_load(file)
            except Exception as ex:
                print(ex)
            return redirect(reverse("way_bills_creator:car_list"))
        if what == "locations":
            try:
                file = request.FILES["file_locations_csv"]
                CSVService.locations_load(file)
            except Exception as ex:
                print(ex)
            return redirect(reverse("way_bills_creator:location_list"))
        if what == "drivers":
            try:
                file = request.FILES["file_drivers_csv"]
                CSVService.drivers_load(file)
            except Exception as ex:
                print(ex)
            return redirect(reverse("way_bills_creator:driver_list"))
        if what == "events":
            try:
                file = request.FILES["file_events_csv"]
                CSVService.events_load(file)
            except Exception as ex:
                print(ex)
            return redirect(reverse("way_bills_creator:home"))

    return redirect(reverse("way_bills_creator:home"))


class CarListView(LoginRequiredMixin, ListView):
    """Класс представлений для списка Автомобилей"""

    model = Car


class CarDetailView(LoginRequiredMixin, DetailView):
    """Класс представлений для просмотра экземпляра Автомобиля"""

    model = Car
    form_class = CarForm
    success_url = reverse_lazy("way_bills_creator:car_list")


class CarCreateView(LoginRequiredMixin, CreateView):
    """Класс представлений для создания экземпляра Автомобиля"""

    model = Car
    form_class = CarForm
    success_url = reverse_lazy("way_bills_creator:car_list")


class CarUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представлений для изменения экземпляра Автомобиля"""

    model = Car
    form_class = CarForm
    success_url = reverse_lazy("way_bills_creator:car_list")


class CarDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представлений для удаления экземпляра Автомобиля"""

    model = Car
    success_url = reverse_lazy("way_bills_creator:car_list")


class DriverListView(LoginRequiredMixin, ListView):
    """Класс представлений для списка Водителя"""

    model = Driver


class DriverDetailView(LoginRequiredMixin, DetailView):
    """Класс представлений для просмотра экземпляра Водителя"""

    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("way_bills_creator:driver_list")


class DriverCreateView(LoginRequiredMixin, CreateView):
    """Класс представлений для создания экземпляра Водителя"""

    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("way_bills_creator:driver_list")


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представлений для изменения экземпляра Водителя"""

    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("way_bills_creator:driver_list")


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представлений для удаления экземпляра Водителя"""

    model = Driver
    success_url = reverse_lazy("way_bills_creator:driver_list")


class LocationListView(LoginRequiredMixin, ListView):
    """Класс представлений для списка Места назначения"""

    model = Location


class LocationDetailView(LoginRequiredMixin, DetailView):
    """Класс представлений для просмотра экземпляра Места назначения"""

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("way_bills_creator:location_list")


class LocationCreateView(LoginRequiredMixin, CreateView):
    """Класс представлений для создания экземпляра Места назначения"""

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("way_bills_creator:location_list")


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представлений для изменения экземпляра Места назначения"""

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("way_bills_creator:location_list")


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представлений для удаления экземпляра Места назначения"""

    model = Location
    success_url = reverse_lazy("way_bills_creator:location_list")


class DistanceListView(LoginRequiredMixin, ListView):
    """Класс представлений для списка Расстояния"""

    model = Distance


class DistanceDetailView(LoginRequiredMixin, DetailView):
    """Класс представлений для просмотра экземпляра Расстояния"""

    model = Distance
    form_class = DistanceForm
    success_url = reverse_lazy("way_bills_creator:distance_list")


class DistanceCreateView(LoginRequiredMixin, CreateView):
    """Класс представлений для создания экземпляра Расстояния"""

    model = Distance
    form_class = DistanceForm
    success_url = reverse_lazy("way_bills_creator:distance_list")


class DistanceUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представлений для изменения экземпляра Расстояния"""

    model = Distance
    form_class = DistanceForm
    success_url = reverse_lazy("way_bills_creator:distance_list")


class DistanceDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представлений для удаления экземпляра Расстояния"""

    model = Distance
    success_url = reverse_lazy("way_bills_creator:distance_list")


class WayBillListView(LoginRequiredMixin, ListView):
    """Класс представлений для списка Путевого листа"""

    model = WayBill

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data["period_list"] = period_list
        context_data["year_list"] = year_list

        return context_data


class WayBillDetailView(LoginRequiredMixin, DetailView):
    """Класс представлений для просмотра экземпляра Путевого листа"""

    model = WayBill
    form_class = WayBillForm
    success_url = reverse_lazy("way_bills_creator:waybill_list")

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        event_id = context_data["object"].event_id
        event_subj = Event.objects.filter(event_id=event_id)[0].subject
        context_data["event_subj"] = event_subj
        return context_data


class WayBillCreateView(LoginRequiredMixin, CreateView):
    """Класс представлений для создания экземпляра Путевого листа"""

    model = WayBill
    form_class = WayBillForm
    success_url = reverse_lazy("way_bills_creator:waybill_list")


class WayBillUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представлений для изменения экземпляра Путевого листа"""

    model = WayBill
    form_class = WayBillForm
    success_url = reverse_lazy("way_bills_creator:waybill_list")


class WayBillDeleteView(LoginRequiredMixin, DeleteView):
    """Класс представлений для удаления экземпляра Путевого листа"""

    model = WayBill
    success_url = reverse_lazy("way_bills_creator:waybill_list")
