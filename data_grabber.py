import csv
import urllib.request

aex_links = {'RDS':"https://euronext.com/en/products/equities/GB00B03MLX29-XAMS#"}

def file_grabber(url):

    response = urllib.request.urlopen(url)
    data  = response.read()
    text = data.decode('utf-8')
    # print(text)

def grab_all():
    # This function downloads all
    # TODO : everything
    #
    for i in aex_links:
        file_grabber(aex_links[i])
    return None

def csv_to_list(path_to_csv_file, csv_type ="default"):

    with open(path_to_csv_file, 'r') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    data_list = data_list[4:]
    data_points = []
    for i in range(0, len(data_list)):
        data_points.append(float(data_list[i][3]))
    return data_points