from django.contrib import admin
from .models import Manufacturer, Phone, OperatingSystem, WirelessInterfaces, CommunicationStandards, ProcessorModel, \
    ScreenType, HeadphoneJack, ChargingConnectorType, Color, PhoneShots, RatingStar, Rating, Reviews


admin.site.register(Manufacturer)
admin.site.register(Phone)
admin.site.register(OperatingSystem)
admin.site.register(WirelessInterfaces)
admin.site.register(CommunicationStandards)
admin.site.register(ProcessorModel)
admin.site.register(ScreenType)
admin.site.register(HeadphoneJack)
admin.site.register(ChargingConnectorType)
admin.site.register(Color)
admin.site.register(PhoneShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)