from django import forms
from django.forms import ModelForm

from way_bills_creator.models import Car, Driver, Location, Distance, WayBill


TYPE_OIL = {
    "D": "Дизель",
    "G": "Автобензин",
}


class CarForm(ModelForm):
    """Класс формы модели Автомобиль"""

    oil_type = forms.ChoiceField(
        required=False,
        label="Тип топлива",
        widget=forms.RadioSelect,
        choices=TYPE_OIL,
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverForm(ModelForm):
    """Класс формы модели Водитель"""

    class Meta:
        model = Driver
        fields = "__all__"


class LocationForm(ModelForm):
    """Класс формы модели Место назначения"""

    class Meta:
        model = Location
        fields = "__all__"


class DistanceForm(ModelForm):
    """Класс формы модели Расстояние"""

    class Meta:
        model = Distance
        fields = "__all__"


class WayBillForm(ModelForm):
    """Класс формы модели Путевой лист"""

    class Meta:
        model = WayBill
        fields = "__all__"
