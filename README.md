# Managing go.dan.cv redirects

Get all redirects: `python3 main.py`

Create url shortener: `python3 create.py`

Get link id for redirect: `python3 get.py`

Delete redirect using link id: `python3 delete.py`

You need a `.env` structured like this:
```bash
export short_API_KEY="key"
export domain="domain.com"
export domain_id="id_from_short_url"
```

Then you can set the environment variables like this:
```bash
source .env
```