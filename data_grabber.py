import csv
import urllib.request
import traceback
import logging

# This link is just here for testing atm, should be done from config file
aex_links = {'RDS':"https://euronext.com/en/products/equities/GB00B03MLX29-XAMS#"}


class DataGrabber(object):
    """Object that handles retrieving data from the web about index and stock prices"""

    def __init__(self):
        self.data_object_list = []

    def file_grabber(self, url):
        # TODO : Decide what type of file to return

        response = urllib.request.urlopen(url)
        data  = response.read()
        text = data.decode('utf-8')

        return file

    def grab_all(self,index_links):
        # Takes in list of urls to online index files
        # Returns list of data objects
        # TODO : everything
        try:
            for i in index_links:
                self.data_object_list.append(self.file_grabber(i))

        except Exception as e:
            logging.error(traceback.format_exc())

        return None

    def csv_to_list(self, path_to_csv_file, csv_type ="default"):

        with open(path_to_csv_file, 'r') as f:
            reader = csv.reader(f)
            data_list = list(reader)

        data_list = data_list[4:]
        data_points = []
        for i in range(0, len(data_list)):
            data_points.append(float(data_list[i][3]))
        return data_points
