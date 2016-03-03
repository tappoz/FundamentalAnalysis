
fundamentals_dir = './data/fundamentals/'
fundamentals_filename_glob = 'fundamentals_*.csv'
fundamentals_filename_regex = 'fundamentals_(.*).csv'

stock_prices_dir = './data/stock_prices/'
stock_prices_ticker_pre_filename_prefix = 'close_prices_pre_2016_02_'
stock_prices_ticker_post_filename_prefix = 'close_prices_post_2016_02_'

def get_stock_prices_pre_2016_02_filename(ticker):
  return stock_prices_ticker_pre_filename_prefix + ticker.upper() + '.csv'
def get_stock_prices_post_2016_02_filename(ticker):
  return stock_prices_ticker_post_filename_prefix + ticker.upper() + '.csv'

quandl_out_shares_db_id = 'RAYMOND'

def get_quandle_outstanding_shares_filename(ticker):
  return 'outstanding_shares_' + quandl_out_shares_db_id + '_' + ticker.upper() + '.csv'

