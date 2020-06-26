import csv
import os
from django.db import migrations
from django.conf import settings

DATE = 0
COUNTRY = 1
CONFIRMED = 2
RECOVERED = 3
DEATHS = 4

def add_covid(apps, schema_editor):
    Passenger = apps.get_model('chart', 'Covid')  # (app_label, model_name)
    csv_file = os.path.join(settings.BASE_DIR, 'countries-aggregated.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        for entry in reader:                            # 판독기에 대하여 반복 처리
            Covid.objects.create(                       # DB 행 생성
                Date=entry[DATE],
                Country=entry[COUNTRY],
                Confirmed=entry[CONFIRMED],
                Recovered=entry[RECOVERED],
                Deaths=entry[DEATHS],
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('covid', '0001_initial'),         # app_label, preceding migration file
    ]
    operations = [                              # 작업
        migrations.RunPython(add_covid),   # add_passengers 함수를 호출
    ]