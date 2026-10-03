#!/usr/bin/env python3
"""
Fuzzer de Endpoints con Autenticacion NTLM - Fuerza bruta de rutas
controlador/accion MVC en una webapp .NET usando autenticacion NTLM
para descubrir endpoints ocultos.

Uso: python3 ntlm-endpoint-fuzzer.py
  - Configurar TARGET, DOMAIN, USERNAME, PASSWORD.
"""
import requests
from requests_ntlm import HttpNtlmAuth

requests.packages.urllib3.disable_warnings()

TARGET = "https://TARGET_HOST"
DOMAIN = "DOMAIN"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

s = requests.Session()
s.auth = HttpNtlmAuth(f"{DOMAIN}\\{USERNAME}", PASSWORD)

controllers = ["Package", "Audit", "Deployment", "Home"]
actions = [
    "Index", "Details/8", "Download/8", "File/8", "Get/8", "Raw/8", "Content/8",
    "Export", "Export/8", "View/8", "Log", "Logs", "List", "All", "Search",
    "Manifest/8", "Metadata/8", "Info/8", "Status/8", "History", "History/8",
    "Report", "Report/8", "Json", "Data",
]

for c in controllers:
    for a in actions:
        p = f"/{c}/{a}"
        try:
            r = s.get(TARGET + p, verify=False, allow_redirects=False, timeout=15)
            if r.status_code not in (404,):
                print(f"[{r.status_code}] {p:28} len={len(r.content)}")
        except Exception as e:
            print(f"[ERR] {p}: {e}")
