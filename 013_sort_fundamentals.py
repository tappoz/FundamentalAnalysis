#!/usr/bin/env python2

import fnmatch, re
import os
import pandas as pd
import dateutil

fundamentals_dir = 'data/fundamentals/'

def sort_dataframe_by_date(df, date_column_name):
  df[date_column_name] = df[date_column_name].apply(dateutil.parser.parse)
  df[date_column_name] = pd.to_datetime(df[date_column_name])
  df = df.sort([date_column_name])
  df.index = range(0,len(df))
  return df

def sort_fundamentals(files_dir):
  END_DATE_COLUMN = 'end_date'
  filename_glob = 'fundamentals_*.csv'
  filename_regex = 'fundamentals_(.*).csv'
  fundamentals_pattern = re.compile(filename_regex)
  for file_name in os.listdir(files_dir):
    if fnmatch.fnmatch(file_name, filename_glob):
      current_ticker = fundamentals_pattern.search(file_name).group(1)
      print 'Processing file:', file_name
      # print 'Processing ticker:', current_ticker
      try:
        current_ticker_fundamentals_df = pd.read_csv(files_dir + file_name)
        # making sure the dataframe is sorted by date
        current_ticker_fundamentals_df = sort_dataframe_by_date(current_ticker_fundamentals_df, END_DATE_COLUMN)
        current_ticker_fundamentals_df.to_csv(files_dir + file_name, index=False)

      except Exception, e:
        print '~~~ Failed to process fundamentals for ticker: ' + current_ticker + ' ~~~', str(e)

sort_fundamentals(fundamentals_dir)
