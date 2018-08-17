import sys
from redfin import RedFin

if len(sys.argv) < 2:
    print('start url expected')
    sys.exit(-1)
start_url = sys.argv[1]
if len(sys.argv) < 3:
    print('output file name expected')
    sys.exit(-1)
output_file = sys.argv[2]

redfin = RedFin(start_url=start_url)
redfin.use_browser()
redfin.get_search_results()
redfin.get_property_data(output_json_file=output_file)
