# capitol city flyers

Temporary repository because someone else decided to blow away the one in use, and rebuilding a website that's half a decade old currently doesn't work into my plans for today.

Oh, yeah, this is just a flask site now serving pre-generated html pages. This used to be a wagtail setup. Not anymore.


## Local development and deployment

```
direnv allow
pipenv install

flask run
```

## Production

On production, you probably want in `.env`:

```
FLASK_APP=webapp
PORT=9002
USER_RUN=1003
GROUP_RUN=1003
```