import requests
url = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMjljNGRjZDAtOTBmOC0xMWVkLWEyYWYtYmQwM2JkNzRkZDEz"
header = {"content-type": "application/json; charset=utf-8", "authorization":"Bearer OTA4N2ZhOWQtNzZiOC00Y2M1LWJhOWMtNTAxYzNiYzE3NDRmMGFiMTBjOWItZjA5_PE93_f451a09f-5fe6-4b74-a13a-2fde64738081"}
requests.get(url, headers = header, verify = True)

