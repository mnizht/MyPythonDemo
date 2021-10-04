import codecs
import json
import time
import uuid

from faker import Faker

fake = Faker(locale='zh_CN')

with codecs.open('/home/zhuht/data2.json', 'a', 'utf-8') as a:
    for num in range(1, 10001):
        uuid = uuid.uuid1()
        index = {
            "index": {
                "_id": uuid.hex
            }
        }
        json.dump(index, a, ensure_ascii=False)
        a.write("\n")
        person = {
            "id": uuid.hex,
            "name": fake.name(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "company": fake.company()
        }
        json.dump(person, a, ensure_ascii=False)
        a.write("\n")

print("End")
