#!/usr/bin/env python3
"""Serve a Godot web export over HTTPS on the local network, so a phone on the
same wifi can open it (Godot needs a secure context; plain http only counts
as secure on localhost).

    python3 tools/serve_https.py <export_dir> [port]

A self-signed certificate is created once in ~/.cache/escoria-mobile/. The
phone browser will warn about it: Advanced -> continue to the site.
"""
import http.server, os, socket, ssl, subprocess, sys
from functools import partial

root = sys.argv[1] if len(sys.argv) > 1 else "."
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8443
cache = os.path.expanduser("~/.cache/escoria-mobile")
cert, key = os.path.join(cache, "cert.pem"), os.path.join(cache, "key.pem")
os.makedirs(cache, exist_ok=True)
if not os.path.exists(cert):
    subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
                    "-keyout", key, "-out", cert, "-days", "3650",
                    "-subj", "/CN=escoria-mobile-dev"], check=True)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("10.255.255.255", 1))  # no packet is sent; picks the LAN interface
lan_ip = s.getsockname()[0]
s.close()

handler = partial(http.server.SimpleHTTPRequestHandler, directory=root)
httpd = http.server.ThreadingHTTPServer(("0.0.0.0", port), handler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(cert, key)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
print(f"Serving {os.path.abspath(root)} at https://{lan_ip}:{port}/", flush=True)
httpd.serve_forever()
