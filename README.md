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
- `{created_parsed:%Y-%m-%d %H:%M}`
- `{updated_parsed:%Y-%m-%d %H:%M}`
- `{published_parsed:%Y-%m-%d %H:%M}`
- `{expired_parsed:%Y-%m-%d %H:%M}`

(See [feedparser Documentation](https://pythonhosted.org/feedparser/search.html?q=entry) for more available format arguments)

### Value conversion

feedo extends [value conversion](https://pyformat.info/#conversion_flags) syntax and support following extra conversion flags:

- `!x` converts value to a SHA-1 checksum string
- `!X` converts value to a SHA-256 checksum string
- `!f` escapes value to make it safe for a file name
- `!g` slugifys the value with [python-slugify](https://github.com/un33k/python-slugify)

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

