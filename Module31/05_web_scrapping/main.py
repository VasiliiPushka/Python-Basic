import requests
from re import findall

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки

    result_beta = findall(r'<h3.*>(.+)</h3>', text)

release = list(map(lambda x: x, result_beta))
print(release)

