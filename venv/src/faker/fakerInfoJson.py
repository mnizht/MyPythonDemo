import json
import time
import codecs

from faker import Faker

fake = Faker(locale='zh_CN')

with codecs.open('d://data.json', 'a', 'utf-8') as fw:
    data = list()
    for num in range(1, 100):
        index = {
            "index": {
                "_id": str(num)
            }
        }
        person = {
            "id": num,
            "name": fake.name(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "company": fake.company()
        }
        data.append(index)
        data.append(person)

    print(data)
    json.dump(data, fw, ensure_ascii=False)

print("End")
