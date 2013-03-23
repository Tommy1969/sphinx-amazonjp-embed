#-*- coding:utf-8 -*-

import re
import urlparse
import urllib


DP_REGEX = re.compile(ur'/dp/([\da-zA-Z]+)[^0-9a-zA-Z]')



def parse_dp_from_url(url):
    u'''
    amazon の URL から /dp/${なんか数列} を取ってくる
    '''

    parsed = urlparse.urlparse(url)

    match = DP_REGEX.search(parsed.path)

    if match:

        return match.group(1)





class Option(object):

    def __init__(self, key, attr, values):

        self.key = key
        self.attr = attr
        self.values = values


    def get_option(self, options):

        return self.attr, self.values[self.key in options]



class SizeOption(object):

    def get_option(self, options):

        if 'small' in options:
            return 'IS1', '1'
        else:
            return 'IS2', '1'



OPTIONS = [Option(key='same_window', attr='lt1', values=('_blank', '_top')),
           Option(key='hide_border', attr='bc1', values=('000000', 'FFFFFF')),
           SizeOption()]


def build_query(url, id, options):

    dp = parse_dp_from_url(url)

    attrs = [('asins', dp),
             ('bg1', 'FFFFFF'),
             ('fc1', '000000'),
             ('lc1', '0000FF'),
             ('o', '9'),
             ('p', '8'),
             ('l', 'as4'),
             ('m', 'amazon'),
             ('f', 'ifr'),
             ('ref', 'ss_til')]

    if id is not None:
        attrs.append(('t', 'shomah4a-22'))

    for opt in OPTIONS:
        attrs.append(opt.get_option(options))

    query = urllib.urlencode(attrs)

    return query
