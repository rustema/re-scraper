dt=`date +%Y%m%d`

function scrape() {
    local city=$1
    local start_url=$2
    echo "processing $city"
    mkdir -p $city
    PATH=$PATH:. python3 scraper.py $start_url $city/redfin-$dt.json &&\
    python3 zillow.py $city/redfin-$dt.json $city/all-$dt.csv
}

scrape 'los-altos' 'https://www.redfin.com/city/11018/CA/Los-Altos'
scrape 'santa-clara' 'https://www.redfin.com/city/17675/CA/Santa-Clara/'
scrape 'palo-alto' 'https://www.redfin.com/city/14325/CA/Palo-Alto'
scrape 'mountain-view' 'https://www.redfin.com/city/12739/CA/Mountain-View'
scrape 'sunnyvale' 'https://www.redfin.com/city/19457/CA/Sunnyvale'
scrape 'campbell' 'https://www.redfin.com/city/2673/CA/Campbell'
scrape 'north-san-jose' 'https://www.redfin.com/neighborhood/10854/CA/San-Jose/North-San-Jose'
scrape 'west-valley' 'https://www.redfin.com/neighborhood/116902/CA/San-Jose/West-Valley'
scrape 'central-san-jose' 'https://www.redfin.com/neighborhood/119262/CA/San-Jose/Central-San-Jose'
