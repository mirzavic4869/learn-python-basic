from . import Database
from .Util import random_string
import time


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{
        data["judul"]},{data["penulis"]},{data["tahun"]}'

    print(data_str)

    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('gagal ditambahkan bro')


def create_first_data():

    penulis = input('Penulis: ')
    judul = input('Judul: ')
    while (True):
        try:
            tahun = int(input('Tahun\t: '))
            if (len(str(tahun))) == 4:
                break
            else:
                print('masukkan tahun dengan format (yyyy). masukkan lagi!')
        except:
            print('masukkan tahun dengan angka. masukkan lagi!')

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{
        data["judul"]},{data["penulis"]},{data["tahun"]}'

    print(data_str)

    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('gagal bro')


def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print('read database error')
        return False
