#!/usr/bin/env python2

import argparse
import feedparser
import sys

from time import sleep
from formatter import Formatter
from datetime import datetime

def main():
    stdout, stderr = get_encoding_safe_stdio()

    parser = argparse.ArgumentParser(description="Read, format and output an RSS stream.")
    parser.add_argument('uri', action='store', help="load feed from uri")
    parser.add_argument('-o', '--format', action='store', required=True, help="python 3.x styled format string (see https://pyformat.info/)")
    parser.add_argument('-f', '--follow', action='store_true', help="follow feed stream updates")
    parser.add_argument('-i', '--interval', action='store', type=float, default=None, help="time between each fetch for updates (in seconds)")
    args = parser.parse_args()

    last_item_link = None
    formatter = Formatter()
    format_string = args.format.decode('utf-8')

    while True:
        try:
            d = feedparser.parse(args.uri)
        except Exception:
            print >>stderr, "Failed to parse '{}'".format(args.uri)
            continue
        interval = args.interval if args.interval else float(d.feed.ttl) if hasattr(d.feed, 'ttl') else 60
        newlines = []
        for entry in d.entries:
            if entry.link == last_item_link:
                break
            item = dict(entry)
            item['enclosures'] = entry.enclosures
            item['published'] = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else None
            item['created'] = datetime(*entry.created_parsed[:6]) if hasattr(entry, 'created_parsed') else None
            item['updated'] = datetime(*entry.updated_parsed[:6]) if hasattr(entry, 'updated_parsed') else None
            item['expired'] = datetime(*entry.expired_parsed[:6]) if hasattr(entry, 'expired_parsed') else None
            newlines.append(formatter.format(format_string, **item))
        if len(d.entries):
            last_item_link = d.entries[0].link
        for line in reversed(newlines):
            print >>stdout, line
        stdout.flush()
        if args.follow:
            sleep(interval)
            continue
        break

def get_encoding_safe_stdio(encoding='utf-8'):
    import codecs
    stdout = sys.stdout if sys.stdout.encoding else codecs.getwriter(encoding)(sys.stdout)
    stderr = sys.stderr if sys.stderr.encoding else codecs.getwriter(encoding)(sys.stderr)
    return stdout, stderr

