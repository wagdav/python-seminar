import urllib
from HTMLParser import HTMLParser


def query(start, stop):
    return {'Script': 'register',
            'SEorder': '',
            'Stop': 0,
            'Sorder': 'up',
            'SQLwhat': 'Shot,UserName,Entered,Topic,Text',
            'SQLfrom': 'Entries',
            'SQLwhere': ("(Topic = 'DDJ') and (voided is NULL) and "
                         "(Shot >= %d) and (Shot <= %d)" % (start, stop)),
            'SQLorder': 'Shot'}


def get_url(start, n=50):
    return ('http://adas.epfl.ch/perl/logbook.pl?' +
            urllib.urlencode(query(start, start + n)))


def html(url):
    fname, response = urllib.urlretrieve(url)
    return open(fname).read()


def parse(url):
    p = LogBookParser()
    p.feed(html(url))
    return p.data


class LogBookParser(HTMLParser):

    in_td = False
    data = []
    acc = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_td = False
            self.data.append(self.acc)
            acc = []

    def handle_data(self, data):
        if self.in_td:
            self.acc.append(data)
            print self.acc


def fold(l):
    il = []
    out = []
    il.extend(l)
    print len(il)
    while len(il) != 0:
        out.append(tuple(l[:5]))
        il = il[:5]
    return out




p = parse(get_url(45000))
