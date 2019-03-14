from urllib.request import urlopen
import re
import csv

def write_to_CSV(data):
    with open('email.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['url'],
                         ', '.join(e for e in data['email'])))
    f.close()

def read_urls(file):
    urls = []
    with open(file) as f:
        for line in f:
            urls.append(line)
    return urls

def get_email(url):
    response = urlopen(url)
    html = response.read()
    html = html.decode('utf-8')
    match = re.findall(r'[\w\.-]+@[\w\.-]+', html)
    return set(match)

def main():
    for url in read_urls('urls.txt'):
        data = {'url': url, 'email': get_email(url)}
        write_to_CSV(data)

if __name__ == '__main__':
    main()
