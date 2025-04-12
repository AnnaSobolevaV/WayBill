from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from way_bills_creator.models import Location
from way_bills_creator.services import (
    WaybillsService,
    get_location,
    get_distance,
    CalendarService,
    CSVService,
)


class ViewsTests(TestCase):
    """Тесты для модуля views"""

    def test_create_waybills(self):
        url = reverse("way_bills_creator:create_waybills")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_download_wbs_excel(self):
        url = reverse("way_bills_creator:download_wbs_excel")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_download_report(self):
        url = reverse("way_bills_creator:download_report")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_download_events(self):
        url = reverse("way_bills_creator:download_events")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_upload_file_csv(self):
        url = reverse("way_bills_creator:upload_file_csv", args=["cars"])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        url = reverse("way_bills_creator:upload_file_csv", args=["events"])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        url = reverse("way_bills_creator:upload_file_csv", args=["drivers"])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        url = reverse("way_bills_creator:upload_file_csv", args=["locations"])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class ServicesTests(TestCase):
    """Тесты для модуля services"""

    def test_create_waybills(self):
        """Тест для проверки метода создания Путевых листов"""
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/cars_data.csv"
        CSVService.cars_load(file)
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/drivers_data.csv"
        CSVService.drivers_load(file)
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/locations_data.csv"
        CSVService.locations_load(file)
        file = (
            "/Users/anna/PycharmProjects/WayBill/csv_files/events-20250404-152256.csv"
        )
        CSVService.events_load(file)
        ok = WaybillsService.create_waybills("март", "2025")
        self.assertEqual(17, ok)
        ok = WaybillsService.create_waybills("январь", "2020")
        self.assertEqual(0, ok)

    def test_download_report(self):
        """Тест для проверки метода выгрузки Отчетов"""
        ok = WaybillsService.download_report("январь", "2020")
        self.assertEqual(0, ok)

    def test_download_wbs_excel(self):
        """Тест для проверки метода выгрузки Путевых листов в excel"""
        ok = WaybillsService.download_wbs_excel("январь", "2020")
        self.assertEqual(0, ok)

    def test_get_location(self):
        """Тест для проверки метода получения Мест назначения"""
        event_loc = ""
        subj = ""
        office_loc = Location.objects.create(location_name="Офис")
        office_loc.save()
        ok = get_location(event_loc, subj)
        print("get_location ", ok)
        self.assertEqual((office_loc, office_loc), ok)

    def test_get_distance(self):
        """Тест для проверки метода получения Расстояния"""
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/locations_data.csv"
        CSVService.locations_load(file)
        location_from = ""
        location_to = ""
        ok = get_distance(location_from, location_to)
        print("get_distance ", ok)
        self.assertEqual(0.0, ok)

    def test_download(self):
        """Тест для проверки загрузки Путевых листов из TeamUp"""
        ok = CalendarService.download("январь", "2020")
        self.assertEqual(0, ok)

    def test_cars_load(self):
        """Тест для проверки загрузки Автомобилей из файла формата csv"""
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/cars_data.csv"
        ok = CSVService.cars_load(file)
        self.assertEqual(2, ok)

    def test_locations_load(self):
        """Тест для проверки загрузки Мест назначения из файла формата csv"""
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/locations_data.csv"
        ok = CSVService.locations_load(file)
        self.assertEqual(3, ok)

    def test_drivers_load(self):
        """Тест для проверки загрузки Водителей из файла формата csv"""
        file_cars = "/Users/anna/PycharmProjects/WayBill/csv_files/cars_data.csv"
        CSVService.cars_load(file_cars)
        file = "/Users/anna/PycharmProjects/WayBill/csv_files/drivers_data.csv"
        ok = CSVService.drivers_load(file)
        self.assertEqual(2, ok)

    def test_events_load(self):
        """Тест для проверки загрузки Событий из файла формата csv"""
        file = (
            "/Users/anna/PycharmProjects/WayBill/csv_files/events-20250404-152256.csv"
        )
        ok = CSVService.events_load(file)
        self.assertEqual(7, ok)
