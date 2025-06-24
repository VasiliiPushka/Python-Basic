ip_address = input('Введите IP: ').split('.')
new_ip = []

for ip in ip_address:
    if len(ip_address) < 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    if ip.isdigit() == False:
        print(ip,'— это не целое число.')
        break
    elif ip.isdigit() == True:
        if 0 <= int(ip) <= 255:
            new_ip.append(ip)
        else:
            print(ip, 'превышает 255.')
count = 0
for ip in new_ip:
    count += 1
if count == 4:
    print('IP-адрес корректен.')




