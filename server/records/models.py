from django.db import models

from records.constants import DATA_TYPES


class DataRecord(models.Model):
    board_id = models.CharField(max_length=64)
    data_type = models.CharField(max_length=1, choices=DATA_TYPES)
    consumption = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        db_table = "consumption_data_record"
        ordering = ["time"]

    def __str__(self):
        return "{} {} consumption from {} board".format(
            self.consumption, self.data_type, self.board_id
        )
