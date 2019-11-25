import xlwings as xw
from faker import Faker

fake = Faker(locale='zh_CN')

app = xw.App(visible=True, add_book=False)
file = app.books.add()
sheet1 = file.sheets[0]
for num in range(1, 100001):
    sheet1.range('A%d' % num).value = num
    sheet1.range('B%d' % num).value = fake.name()
    sheet1.range('C%d' % num).value = fake.phone_number()

file.save('e://faker.xlsx')
print("End")
