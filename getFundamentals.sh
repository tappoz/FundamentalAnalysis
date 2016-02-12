#!/usr/bin/env bash

tickers_clothes=( 'NKE' 'UA' 'ADDYY' 'ADS' 'LULU' )
tickers_air=( 'EZJ' 'RYN' )
tickers_social=( 'NFLX' 'FB' 'TWTR' 'ETSY' 'LNKD' )
tickers_factory=( 'TSLA' 'IMG' 'IFX' 'SIE' )
tickers_online_retail=( 'AMZN' 'EBAY' 'EBA' 'BABA' )
tickers_pay=( 'PYPL' '2PP' 'SQ' )
tickers_it=( 'GOOG' 'GOOGL' 'AAPL' 'TEAM' 'GDDY' )
tickers_health=( 'FIT' )

FUNDAMENTALS_DIR='data/fundamentals/'
FUNDAMENTALS_LOG_DIR=${FUNDAMENTALS_DIR}logs/
mkdir -p ${FUNDAMENTALS_LOG_DIR}

for ticker in "${tickers_clothes[@]}" "${tickers_air[@]}" "${tickers_social[@]}" "${tickers_factory[@]}" "${tickers_online_retail[@]}" "${tickers_pay[@]}" "${tickers_it[@]}" "${tickers_health[@]}" 
do
  echo "`date +%Y-%m-%d:%H:%M:%S` processing ticker: ${ticker}"
  pystock-crawler reports ${ticker} -o ${FUNDAMENTALS_DIR}fundamentals_${ticker}.csv -s 20060101 -e 20161231 --sort -l "${FUNDAMENTALS_LOG_DIR}tickers_${ticker}.log"
done
