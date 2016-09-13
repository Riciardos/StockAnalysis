import csv
import urllib.request

aex_links = {'RDS':"https://euronext.com/en/products/equities/GB00B03MLX29-XAMS#"}

def file_grabber(url):

    response = urllib.request.urlopen(url)
    data  = response.read()
    text = data.decode('utf-8')
    # print(text)

def grab_all():
    for i in aex_links:
        file_grabber(aex_links[i])


def csv_to_list(path_to_csv_file):

    with open(path_to_csv_file, 'r') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    return data_list