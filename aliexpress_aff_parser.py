import os
import csv


# CSV Files pool #
pool = 'C:\\Users\\Station\\Desktop\\aliexpress csv\\'
parsed = 'C:\\Users\\Station\\Desktop\\aliexpress csv\\parsed\\'
csv_list = os.listdir(pool)
extension = '.txt'
print(csv_list)

# Choose what CSV file we want to parse #
choice = input('CSV to parse: ')

# List of wanted columns #
with open(f'{pool}{choice}', encoding='utf-8') as products:
    heading = next(products)
    product = csv.reader(products)
    for row in product:
        print(f'\t--------------------\n'
        f'video_url\t||\t{row[2]}\n'
        f'img_url\t||\t{row[1]}\n'
        f'\t--------\t\n'
        f'prod_desc\t||\t{row[3]}\n'
        f'discount_price\t||\t{row[4]}\n'
        f'sales\t||\t{row[9]}\n'
        f'discount_precent\t||\t{row[5]}\n'
        f'score\t||\t{row[10]}/5\n'
        f'affurl\t||\t{row[11]}\n')
