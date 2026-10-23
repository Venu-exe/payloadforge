# PayloadForge 🎯

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)](#)
[![GitHub Stars](https://img.shields.io/github/stars/Venu-exe/payloadforge?style=social)](https://github.com/Venu-exe/payloadforge/stargazers)

> **Zero-dependency, pure-Python bug bounty payload generator & mutator.**  
> Generate payloads for common vulnerability classes with multiple encodings and WAF-bypass variants — in one command.

---

## 📑 Table of Contents

- [Why PayloadForge?](#-why-payloadforge)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Payload Types](#-payload-types)
- [Encodings](#-encodings)
- [WAF Bypass Mode](#-waf-bypass-mode)
- [CLI Reference](#-cli-reference)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why PayloadForge?

When hunting, you often need the same payload in 5 different encodings, plus a few WAF-bypass twists. Copy-pasting and manually encoding in CyberChef gets old fast. PayloadForge does it in one command — zero deps, runs anywhere.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 7 Vuln Types | XSS, SQLi, SSRF, LFI, SSTI, Open Redirect, Command Injection |
| 🔐 6 Encodings | raw, URL, Base64, hex, double-URL, unicode |
| 🌀 Mutate Mode | Show all encodings for every payload at once |
| 🛡️ WAF Bypass | Case flip, comment injection, double encode, null byte |
| 📦 Zero Deps | Pure Python stdlib |
| ⚡ Fast | Instant output, pipe-friendly |

---

## 🎬 Demo

```bash
$ python3 payloadforge.py -t xss --waf

  ____        _ _           ____
 |  _ \ __ _| | | ___ _ __ |  _ \ ___  __ _  __ _
 | |_) / _` | | |/ _ \ '__|| |_) / _ \/ _` |/ _` |
 |  __/ (_| | | |  __/ |   |  __/  __/ (_| | (_| |
 |_|   \__,_|_|_|\___|_|   |_|   \___|\__, |\__,_|
                                      |___/

  type=xss  encode=raw  waf=True
============================================================

[XSS]
  <script>alert(1)</script>
  <ScRiPt>aLeRt(1)</sCrIpT>
  <script>alert(1)</script>
  %253Cscript%253Ealert%25281%2529%253C%252Fscript%253E
  <script>alert(1)</script>%00
```

---

## 📦 Installation

```bash
git clone https://github.com/Venu-exe/payloadforge.git
cd payloadforge
python3 payloadforge.py --help
```

No dependencies required.

### Optional: global command

```bash
chmod +x payloadforge.py
sudo ln -s "$(pwd)/payloadforge.py" /usr/local/bin/payloadforge
payloadforge --list
```

---

## 🚀 Usage

```bash
# List available payload types
python3 payloadforge.py --list

# Generate XSS payloads URL-encoded
python3 payloadforge.py -t xss -e url

# Show all encodings for SQLi payloads
python3 payloadforge.py -t sqli --mutate

# WAF-bypass variants for XSS
python3 payloadforge.py -t xss --waf

# All types at once
python3 payloadforge.py --all

# Base64-encoded SSRF payloads
python3 payloadforge.py -t ssrf -e b64
```

### Pipe-friendly

```bash
python3 payloadforge.py -t xss -e url | sort -u > xss.txt
python3 payloadforge.py --all | grep -i "alert" > xss_only.txt
```

---

## 🎯 Payload Types

| Key | Description |
|---|---|
| `xss` | Cross-Site Scripting |
| `sqli` | SQL Injection |
| `ssrf` | Server-Side Request Forgery |
| `lfi` | Local File Inclusion |
| `ssti` | Server-Side Template Injection |
| `redirect` | Open Redirect |
| `cmdi` | Command Injection |

---

## 🔐 Encodings

| Key | Description |
|---|---|
| `raw` | No encoding |
| `url` | URL encoding (percent) |
| `b64` | Base64 |
| `hex` | Hexadecimal |
| `double` | Double URL encoding |
| `unicode` | Unicode escape (`\u00xx`) |

---

## 🛡️ WAF Bypass Mode

`--waf` generates 5 variants per payload:

1. **Original** — raw payload
2. **Case flip** — alternating upper/lower case
3. **Comment injection** — spaces replaced with `/**/` (SQL)
4. **Double encode** — double URL encoding
5. **Null byte** — appended `%00`

---

## 📋 CLI Reference

```
usage: payloadforge.py [-h] [-t TYPE] [-e ENCODE] [-l] [--all] [--mutate] [--waf]

options:
  -t, --type     Payload type (xss, sqli, ssrf, lfi, ssti, redirect, cmdi)
  -e, --encode   Encoding (raw, url, b64, hex, double, unicode) [default: raw]
  -l, --list     List available payload types
  --all          Generate all types
  --mutate       Show all encodings for each payload
  --waf          Generate WAF-bypass variants
```

---

## 🗺️ Roadmap

- [ ] Custom wordlist input (`--wordlist`)
- [ ] Combine mode (chain payloads)
- [ ] Polyglot payloads
- [ ] Output to file (`-o`)
- [ ] JSON output for tooling integration
- [ ] More vuln types (XXE, SSTI engines, NoSQLi)

---

## 🤝 Contributing

Contributions welcome! Keep the zero-dependency philosophy (stdlib only).

1. Fork → branch → commit → PR

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

## 👤 Author

**Venu-exe** — bug bounty hunter & security tooling developer.

- GitHub: [@Venu-exe](https://github.com/Venu-exe)
- Portfolio: [venu-exe.github.io](https://venu-exe.github.io)

⭐ Star the repo if it saved you time!