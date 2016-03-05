import os
import glob

def get_all_tickers_lists_csv_files():
  all_tickers_all_files = []
  for file in glob.glob('./data/conf/tickers_*.csv'):
    # print 'Found this:', file
    tickers_to_process = get_tickers_from_csv_file(file)
    # print '  >>> Found tickers:', tickers_to_process
    all_tickers_all_files.extend(tickers_to_process)
  # print 'ALL OF ALL:', all_tickers_all_files
  return all_tickers_all_files

import csv
def get_tickers_from_csv_file(filename):
  all_tickers_for_file = []
  with open(filename, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=':')
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        current_tickers = row[1].split(',')
        # print '  Tickers:', current_tickers
        all_tickers_for_file.extend(current_tickers)
  return all_tickers_for_file
