# coding:utf-8
# Example by Ole Zorn

from base64 import b64decode
from zlib import decompress
import clipboard

url  = clipboard.get()
encoded  =  url[len('editorial://add-workflow?workflow-data-b64='):]
encoded = encoded.replace('~','=').replace('_','/').replace('-','+')
json_string = decompress(b64decode(encoded))
print json_string
