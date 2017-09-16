'''
Project: PayU Turkey Reports API Python3 Sample Code
Author: Göktürk Enez
'''
# Importing required libraries.
import hmac
import hashlib
from urllib.request import Request, urlopen
import collections
import time

#Secret Key
secret = 'SECRET_KEY'

array = collections.OrderedDict()
array['merchant'] = 'OPU_TEST'
array['startDate'] = '2017-09-14'
array['endDate'] = '2017-09-15'
array['timestamp'] = str(time.time()).split('.')[0]

# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in array.items():
    print(v)

# Adding the UTF-8 byte length of each field value at the beginning of field value
    hashstring += str(len(v.encode('UTF-8'))) + str(v)
print(hashstring)

# Calculating signature
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()
print(signature)

# Adding Signature @param to dict
array['signature'] = signature

# Endpoint
url = 'https://secure.payu.com.tr/reports/orders?merchant={merchant}&startDate={startDate}&endDate={endDate}&timeStamp={timestamp}&signature={signature}'.format(**array)
print(url)

# Sending Request to Endpoint
request = Request(url)
response = urlopen(request).read().decode()

# Printing result/response
print(response)

