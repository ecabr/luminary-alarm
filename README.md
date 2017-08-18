# Luminary Alarm
Software for city luminary alarms via Twitter

## Requirements

Install TwitterAPI (as root if required):

```bash
$ pip install TwitterAPI
```

## Using

Create `data/authentication.json`:

```
{
  "consumer": {
    "key": <consumer key>,
    "secret": <consumer secret>
  },
  "access_token": {
    "key": <access token key>,
    "secret": <access token secret>
  }
}
```

Execute:

```bash
$ src/main.py
```
