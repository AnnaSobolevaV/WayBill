from django.db import models


class Car(models.Model):
    """Класс, описывающий модель Автомобиль
    Car(car_name, car_num, oil_type, l100km, l100km_w)"""

    car_name = models.CharField(
        max_length=150,
        verbose_name="название авто",
        help_text="",
        blank=True,
        null=True,
    )
    car_num = models.CharField(
        max_length=150, verbose_name="номер авто", help_text="", blank=True, null=True
    )
    oil_type = models.CharField(
        max_length=15, verbose_name="тип топлива", help_text="", blank=True, null=True
    )
    l100km = models.FloatField(
        max_length=15,
        verbose_name="расход топлива летом",
        help_text="",
        blank=True,
        null=True,
    )
    l100km_w = models.FloatField(
        max_length=15,
        verbose_name="расход топлива зимой",
        help_text="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.car_name} {self.car_num}"


class Driver(models.Model):
    """Класс, описывающий модель Водитель
    Driver(name, car, snils_num, lic_num, lic_date)"""

    name = models.CharField(
        max_length=150, verbose_name="ФИО водителя", help_text="", blank=True, null=True
    )
    car = models.ForeignKey(
        Car,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Автомобиль",
        help_text="",
    )
    snils_num = models.CharField(
        max_length=150,
        verbose_name="СНИЛС водителя",
        help_text="",
        blank=True,
        null=True,
    )
    lic_num = models.CharField(
        max_length=150,
        verbose_name="Номер водительских прав",
        help_text="",
        blank=True,
        null=True,
    )
    lic_date = models.CharField(
        verbose_name="дата выдачи водительских прав",
        help_text="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    """Класс, описывающий модель Место назначения
    Location(location_name, company_name, address)"""

    location_name = models.CharField(
        max_length=150,
        verbose_name="название места",
        help_text="",
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        max_length=250,
        verbose_name="название компании",
        help_text="",
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=250, verbose_name="адрес", help_text="", blank=True, null=True
    )

    class Meta:
        verbose_name = "Место назначения"
        verbose_name_plural = "Места назначения"

    def __str__(self):
        return f"{self.location_name}"


class Distance(models.Model):
    """Класс, описывающий модель Расстояние
    Distance(loc_from, loc_to, loc_km)"""

    loc_from = models.ForeignKey(
        Location,
        related_name="loc_from",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="путь от",
        help_text="",
    )
    loc_to = models.ForeignKey(
        Location,
        related_name="loc_to",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="путь до",
        help_text="",
    )

    loc_km = models.FloatField(
        max_length=15,
        verbose_name="расстояние в км",
        help_text="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Дистанция"
        verbose_name_plural = "Дистанции"

    def __str__(self):
        return f"{self.loc_from} - {self.loc_to}"


class Event(models.Model):
    """Класс, описывающий модель Событие
    Event(event_id, start_date, end_date, subject, calendar_name, location, who)
    """

    event_id = models.PositiveIntegerField(
        verbose_name="id из TeamUp", help_text="", blank=True, null=True
    )
    start_date = models.DateField(
        verbose_name="дата начала", help_text="", blank=True, null=True
    )
    end_date = models.DateField(
        verbose_name="дата окончания", help_text="", blank=True, null=True
    )
    subject = models.CharField(
        max_length=150,
        verbose_name="описание события",
        help_text="",
        blank=True,
        null=True,
    )
    calendar_name = models.CharField(
        max_length=150,
        verbose_name="имя календаря",
        help_text="",
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=150,
        verbose_name="место события в календаре",
        help_text="",
        blank=True,
        null=True,
    )
    who = models.CharField(
        max_length=150,
        verbose_name="участник в календаре",
        help_text="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Событие в календаре"
        verbose_name_plural = "События в календаре"

    def __str__(self):
        return f"{self.subject}: {self.calendar_name} {self.start_date} - {self.end_date} {self.location} {self.who}"


class WayBill(models.Model):
    """Класс, описывающий модель Путевой лист
    WayBill(date, driver, car, event_id, location_from, location_to, distance)"""

    date = models.DateField(
        max_length=150,
        verbose_name="дата путевого листа",
        help_text="",
        blank=True,
        null=True,
    )
    driver = models.ForeignKey(
        Driver,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="водитель",
        help_text="",
    )
    car = models.ForeignKey(
        Car,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="автомобиль",
        help_text="",
    )
    event_id = models.PositiveIntegerField(
        verbose_name="id из TeamUp", help_text="", blank=True, null=True
    )
    location_from = models.ForeignKey(
        Location,
        related_name="location_from",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="место от",
        help_text="",
    )
    location_to = models.ForeignKey(
        Location,
        related_name="location_to",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="место до",
        help_text="",
    )
    distance = models.FloatField(
        max_length=15,
        verbose_name="расстояние в км",
        help_text="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Путевой лист"
        verbose_name_plural = "Путевые листы"
        ordering = [
            "date",
            "driver",
        ]

    def __str__(self):
        return f"{self.date} Водитель: {self.driver} От: {self.location_from} До:{self.location_to}"
