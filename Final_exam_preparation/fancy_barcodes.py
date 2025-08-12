import re

barcodes_count = int(input())


for _ in range(0, barcodes_count):
    digit_counter = 0
    digit_sum = ""
    barcode = input()
    matches = re.match(r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+', barcode)
    if matches:

        for element in barcode:
            if element.isdigit():
                digit_sum += element
                digit_counter += 1
        if digit_counter == 0:
            print('Product group: 00')
        else:
            print(f"Product group: {digit_sum}")

    else:
        print("Invalid barcode")