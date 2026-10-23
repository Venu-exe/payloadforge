# PayloadForge 🎯

Zero-dependency Python bug bounty payload generator & mutator.

Generate payloads for common vuln classes with encoding and WAF-bypass variants.

## Features
- 7 vuln types: xss, sqli, ssrf, lfi, ssti, redirect, cmdi
- 6 encodings: raw, url, b64, hex, double, unicode
- `--mutate` to show all encodings per payload
- `--waf` to generate WAF-bypass variants (case flip, comment injection, double encode, null byte)

## Usage
```bash
python3 payloadforge.py --list
python3 payloadforge.py -t xss -e url
python3 payloadforge.py -t sqli --mutate
python3 payloadforge.py -t xss --waf
python3 payloadforge.py --all
```

## License
MIT
"""