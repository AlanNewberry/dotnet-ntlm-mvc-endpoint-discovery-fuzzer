# Fuzzer de Endpoints MVC en .NET con Autenticacion NTLM

## Descripcion

Escribi este script para automatizar el descubrimiento de endpoints ocultos en aplicaciones web .NET que usan autenticacion NTLM. Genera combinaciones de controladores y acciones MVC tipicas y las prueba una por una, filtrando las respuestas 404 para mostrar solo los endpoints que existen.

## Como funciona

1. **Autenticacion NTLM**: Se autentica automaticamente contra el servidor usando credenciales de dominio
2. **Generacion de rutas**: Combina una lista de controladores con una lista de acciones MVC comunes (`Index`, `Details/8`, `Download/8`, `Export`, etc.)
3. **Fuerza bruta**: Prueba cada combinacion `/{Controlador}/{Accion}` y muestra las que no devuelven 404
4. **Reporte**: Muestra el status code y el tamanio de respuesta de cada endpoint encontrado

## Requisitos

```bash
pip install requests requests-ntlm
```

## Uso

Configura las variables al inicio del script:

```python
TARGET = "https://TARGET_HOST"
DOMAIN = "DOMAIN"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
```

Personaliza las listas de controladores y acciones segun la aplicacion objetivo:

```python
controllers = ["Package", "Audit", "Deployment", "Home"]
actions = ["Index", "Details/8", "Download/8", ...]
```

```bash
python3 dotnet-ntlm-mvc-endpoint-discovery-fuzzer.py
```

## Ejemplo de salida

```
[200] /Package/Index              len=15234
[200] /Package/Details/8          len=8721
[302] /Admin/Index                len=0
[403] /Deployment/Export           len=1203
```

## Cuando usar este script

- Cuando tenes credenciales validas de dominio pero no sabes que endpoints expone la aplicacion
- Para encontrar funcionalidades ocultas que no estan linkeadas en la interfaz web
- Como paso de reconocimiento antes de buscar vulnerabilidades especificas (SQLi, IDOR, etc.)

## Aviso legal

Este script es unicamente para pruebas de seguridad autorizadas y fines educativos. Siempre obtene la autorizacion correspondiente antes de testear contra cualquier sistema.

## Autor

**Alan Newberry**
