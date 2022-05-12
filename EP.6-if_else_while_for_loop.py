print('----if eles----')

money = 300
if money >= 300:
    print('ไปกินอาหารญี่ปุ่น')
else:
    print('ไปกินข้าวร้านป้าแดง')

print('กลับไปเรียน python ต่อ')

print('----while loop----')

money1 = 1000
tranfer = 800

while money < tranfer:
    tranfer = int(input('กรุณากรอกจำนวนเงินใหม่ : '))

print('โอนได้')

print('----for loop----')

for i in range(5):
    print('hello',i)

print('----loop in list----')
friend = ['Korkai','Khorkhai','Khorkwai','Somchai','Somsak']

for f in friend:
    print(f)

print('----loop in dictionary----')

friend2 = {
    'Korkai' : 'ก.ไก่',
    'Khorkhai' : 'ข.ไข่',
    'Khorkwai' : 'ค.ควาย'
}

#show key
for f in friend2:
    print(f)

#show item
for f in friend2.items():
    print(f)
    
#show key only
for f in friend2.keys():
    print(f)

#show value only
for f in friend2.values():
    print(f)

#ลำดับ
for i,f in enumerate(friend,start=1000):
    print(i,f)

#ลำดับdic
for i,f in enumerate(friend2.items()):
    print(i,f)

for i,(k,v) in enumerate(friend2.items()):
    print(i,k,v)
