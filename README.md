
# Ubuntu installs
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```
```
apt-get purge python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```

```
$ pip install --upgrade pip
```

# Ubuntu uninstalls
```
$ sudo apt-get remove python3-pip; sudo apt-get install python3-pip
```

# Pip installs
```
$ sudo pip3 install numpy
$ sudo pip3 install scipy
$ sudo pip3 install matplotlib
$ sudo pip3 install pandas
```

Matplotlib does not show plots on Ubuntu and python3, then you need:
```
$ sudo pip3 install cairocffi
$ sudo apt-get install cmake
$ sudo pip3 install pyside
```
Then in the code use:
```
matplotlib.rcParams['backend'] = "Qt4Agg"
```
rather than using the default `GTK3Agg` (use `matplotlib.get_backend()` to get that information)

# Plots tutorial
http://www.labri.fr/perso/nrougier/teaching/matplotlib/


# Stocks fundamentals

```
$ sudo pip install pystock-crawler
```

To get fundamentals
```
$ pystock-crawler reports NKE -o out.csv -s 20150101 -e 20161231
```


# List tickers

```
$ curl -o data/nasdaq_listed.csv ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt
$ curl -o data/nasdaq_traded.csv ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqtraded.txt
```
cfr.: http://www.quantatrisk.com/2015/06/22/get-list-nasdaq-securities-python-csv/


# Financial Fundamentals packages

https://github.com/andrewkittredge/financial_fundamentals
http://github.com/andrewkittredge/vector_cache

```
sudo pip2 install git+git://github.com/andrewkittredge/vector_cache.git
sudo pip2 install FinancialFundamentals
```

git clone https://github.com/humdings/pynance-legacy
sudo pip2 install git+git://github.com/humdings/pynance-legacy.git

https://github.com/humdings/yahoo_pynance
sudo pip2 install git+git://github.com/humdings/yahoo_pynance.git
git clone https://github.com/humdings/yahoo_pynance.git

$ sudo pip2 install quandlpy
$ sudo pip2 install Quandl

$ sudo pip2 install stopit

$ sudo pip2 install pandas-datareader
