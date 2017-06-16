# feedo

[![PyPI](https://img.shields.io/pypi/v/feedo.svg)](https://pypi.python.org/pypi/feedo/)

Read, format and output an RSS stream.

feedo is inspired by [rsstail](https://github.com/flok99/rsstail) and it's python copy [rsstail.py](https://github.com/gvalkov/rsstail.py)

## Usage

To fetch an RSS stream:

```sh
feedo http://lorem-rss.herokuapp.com/feed --format '{title}'
```

Add `--follow` option to watch updates on feed.

Supported format arguments:

- `{id}`
- `{link}`
- `{title}`
- `{author}`
- `{content}`
- `{enclosures[i].href}`
- `{enclosures[i].length}`
- `{enclosures[i].type}`
- `{published}`
- `{created}`
- `{updated}`
- `{expired}`

(See [feedparser Documentation](https://pythonhosted.org/feedparser/search.html?q=entry) for more available format arguments)

Values can be styled in python 3 [string formatting](https://docs.python.org/3/library/string.html#string-formatting) syntax. For example, to format `published` value in RFC 3339:

```sh
feedo http://lorem-rss.herokuapp.com/feed --format '{title:.11} ({link}) -- {published:%Y-%m-%dT%H:%MZ%z}'
```

(See [strftime (3)](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior) for date format arguments)

### Value conversion

feedo extends [value conversion](https://pyformat.info/#conversion_flags) syntax and support following extra conversion flags:

- `!x` converts value to a SHA-1 checksum string
- `!X` converts value to a SHA-256 checksum string
- `!f` escapes value to make it safe for a file name
- `!g` slugifys the value with [python-slugify](https://github.com/un33k/python-slugify)

For example, to get the sha1 hash of a `link` value and get first 12 characters:

```sh
feedo http://lorem-rss.herokuapp.com/feed --format '{link} => {link!x} => {link!x:.12}'
```

## Example

feedo can be used in implementing some automatic job:

```sh
feedo "http://bt.byr.cn/torrentrss.php?rows=10&linktype=dl&passkey=XXXXXXXXXX" \
  --format '[ ! -f /media/.abt/{id} ] && abt add --uri "{enclosures[0].href}" --dir="/media/Downloads/{title!f}" && touch /media/.abt/{id}' \
  --follow | sh
```

This snippet watches an RSS stream of a RSS subscription and add new tasks to aria2 using [abt](https://github.com/kamikat/abt).

**WARNING** take a trust-worthy source before pipe anything generated into a shell!!!

## License

(The MIT License)

