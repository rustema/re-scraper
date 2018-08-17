import sys
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import pandas as pd

def get_addresses(data):
    all_properties = set()
    for v in data:
        street_address = v['street_address']
        citystatezip = v['address_locality'] + v['address_region'] + ' ' + v['postal_code']
        price = v['price']
        restimate = v['restimate']
        mls_number = v['mls_number']
        rurl = v['url']
        rstatus = v['status']
        rurgent_msg = v['urgent_msg']

        k = (street_address, citystatezip, price, restimate, mls_number, rurl, rstatus, rurgent_msg)
        if k not in all_properties:
            all_properties.add(k)
            yield k

if len(sys.argv) < 2:
    print('specify json file name')
    sys.exit(-1)
if len(sys.argv) < 3:
    print('specify output csv name')
    sys.exit(-1)

csv_file_name = sys.argv[2]
json_file_name = sys.argv[1]
with open(json_file_name) as f:
    data = json.load(f)

df = pd.DataFrame(columns=['date', 'mls_number', 'street_address', 'citystatezip', 'rprice', 'restimate', 'rstatus', 'rurl', 'rurgent_msg', 'zestimate', 'zpid', 'zurl'])
for p in get_addresses(data):
    street_address, citystatezip, price, restimate, mls_number, rurl, rstatus, rurgent_msg = p 
    f = {'zws-id': !ADD-ZILLOW-ID-HERE!, 'address': street_address, 'citystatezip': citystatezip}
    url = 'http://www.zillow.com/webservice/GetSearchResults.htm?' + urllib.parse.urlencode(f)

    with urllib.request.urlopen(url) as req:
        zillow_data = req.read()
        root = ET.fromstring(zillow_data)
        zestimate = root.find('./response/results/result/zestimate/amount')
        if zestimate is not None:
            zestimate = zestimate.text
        zpid = root.find('./response/results/result/zpid')
        if zpid is not None:
            zpid = zpid.text
        zurl = root.find('./response/results/result/links/homedetails')
        if zurl is not None:
            zurl = zurl.text
        print('url =', url, '\t', zestimate)
        df = df.append({'date': pd.Timestamp.today().date(), 'mls_number': mls_number, 'street_address': street_address,
                        'citystatezip': citystatezip, 'rprice': price,
                        'restimate': restimate, 'rstatus': rstatus, 'rurl': rurl,
                        'rurgent_msg': rurgent_msg,
                        'zestimate': zestimate, 'zpid': zpid, 'zurl': zurl}, ignore_index=True)

df.to_csv(csv_file_name, index=False)
