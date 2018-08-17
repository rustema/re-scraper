# Redfin & Zillow scraper.
Scrape housing data from Redfin & Zillow.

Before using, make sure to add your Zillow id to zillow.py:
simply replace !ADD-ZILLOW-ID-HERE! with the Zillow id string.

Download chromedriver binary from https://sites.google.com/a/chromium.org/chromedriver/
and place it in the root directory.

Currently, scrapes data for 9 neighborhoods:
* los-altos
* santa-clara
* palo-alto
* mountain-view
* sunnyvale
* campbell
* north-san-jose
* west-valley
* central-san-jose

Adding/removing is easy: just modify run.sh.

How to run scrape:
```
$ ./run.sh
```

How to merge results into a single .csv file:
```
$ python3 merge.py YYYYMMDD
```
