from django.contrib import admin

from records.models import DataRecord


class DataRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "board_id",
        "data_type",
        "consumption",
        "time",
    )
    list_filter = ["time", "data_type"]
    search_fields = ["board_id", "consumption", "data_type"]


admin.site.register(DataRecord, DataRecordAdmin)
