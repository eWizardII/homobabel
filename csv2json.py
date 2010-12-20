import csv
import json

f = open( 'B:/Twitter/homobabel/top100.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "id","name" ) )
out = json.dumps( [ row for row in reader ] )
print out

with open('B:/Twitter/top100.json', mode='w') as f:
    json.dump(out, f, indent=2, encoding='utf-8')