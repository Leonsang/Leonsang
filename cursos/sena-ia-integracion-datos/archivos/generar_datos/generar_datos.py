"""Genera los datos SIMULADOS del caso de estudio "Distribuidora Andina".

Tres fuentes heterogeneas, con los defectos de calidad tipicos de un proceso
de integracion real (formatos mixtos, duplicados, nulos, llaves inconsistentes):

  ventas_erp.csv     -> exportacion del ERP  (CSV, separador ';', latin-1)
  clientes_crm.json  -> exportacion del CRM  (JSON anidado, UTF-8)
  productos.csv      -> catalogo de producto (CSV, separador ',', UTF-8)

Todos los datos son ficticios. La semilla fija hace el resultado reproducible.
"""
import json
import random
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

SEMILLA = 3635322
random.seed(SEMILLA)
rng = np.random.default_rng(SEMILLA)
AQUI = Path(__file__).parent

# ---------------------------------------------------------------- productos
CATALOGO = {
    "Tecnologia": [("Audifonos Bluetooth", 89900), ("Teclado mecanico", 189900),
                   ("Mouse inalambrico", 59900), ("Monitor 24 pulgadas", 649900),
                   ("Disco SSD 1TB", 329900), ("Camara web HD", 139900),
                   ("Router WiFi 6", 279900), ("Memoria USB 128GB", 45900)],
    "Hogar": [("Licuadora 600W", 159900), ("Juego de sabanas", 119900),
              ("Lampara LED de mesa", 69900), ("Olla a presion 6L", 189900),
              ("Organizador plastico", 39900), ("Ventilador de torre", 229900),
              ("Cafetera 12 tazas", 149900), ("Set de toallas", 79900)],
    "Oficina": [("Silla ergonomica", 459900), ("Resma de papel carta", 21900),
                ("Archivador AZ", 12900), ("Escritorio 120cm", 389900),
                ("Tablero acrilico", 99900), ("Caja de boligrafos x12", 14900),
                ("Calculadora cientifica", 64900), ("Grapadora metalica", 27900)],
    "Deportes": [("Balon de futbol N5", 79900), ("Mat de yoga", 54900),
                 ("Mancuernas 5kg par", 119900), ("Botella termica 1L", 49900),
                 ("Cuerda para saltar", 24900), ("Bicicleta estatica", 899900),
                 ("Guantes de gimnasio", 39900), ("Banda elastica x3", 34900)],
}
productos = []
n = 0
for categoria, items in CATALOGO.items():
    for nombre, precio in items:
        n += 1
        productos.append({
            "sku": f"SKU-{n:03d}",
            "nombre_producto": nombre,
            "categoria": categoria,
            "precio_lista": precio,
            "costo_unitario": int(round(precio * rng.uniform(0.52, 0.72), -2)),
        })
df_prod = pd.DataFrame(productos)
df_prod.to_csv(AQUI / "productos.csv", index=False, encoding="utf-8")

# ----------------------------------------------------------------- clientes
CIUDADES = {"Bogotá": "Cundinamarca", "Medellín": "Antioquia", "Cali": "Valle del Cauca",
            "Barranquilla": "Atlántico", "Bucaramanga": "Santander", "Ibagué": "Tolima",
            "Pereira": "Risaralda", "Cartagena": "Bolívar"}
PESO_CIUDAD = [0.30, 0.20, 0.14, 0.10, 0.08, 0.07, 0.06, 0.05]
SEGMENTOS = ["Hogar", "Pyme", "Corporativo"]
PREFIJOS = ["Comercial", "Inversiones", "Distribuciones", "Soluciones", "Grupo", "Almacenes"]
SUFIJOS = ["del Norte", "Andina", "La 14", "El Progreso", "Central", "Los Pinos", "San Jorge",
           "del Valle", "Tolima Grande", "Caribe", "Santa Ana", "El Dorado"]

clientes = []
for i in range(1, 121):
    ciudad = str(rng.choice(list(CIUDADES), p=PESO_CIUDAD))
    segmento = str(rng.choice(SEGMENTOS, p=[0.50, 0.35, 0.15]))
    registro = date(2022, 1, 1) + timedelta(days=int(rng.integers(0, 1090)))
    cliente = {
        "id": f"C{i:04d}",
        "razon_social": f"{random.choice(PREFIJOS)} {random.choice(SUFIJOS)} {i}",
        "segmento": segmento,
        "contacto": {
            "email": f"compras{i}@ejemplo.com.co",
            "telefono": f"60{rng.integers(1, 9)}{rng.integers(2000000, 7999999)}",
        },
        "direccion": {"ciudad": ciudad, "departamento": CIUDADES[ciudad]},
        "fecha_registro": registro.isoformat(),
        "etiquetas": random.sample(["frecuente", "credito", "mayorista", "nuevo", "web"],
                                   k=random.randint(0, 3)),
    }
    # Defectos intencionales del CRM
    if i % 17 == 0:
        cliente["contacto"]["email"] = None           # email faltante
    if i % 23 == 0:
        del cliente["direccion"]["departamento"]      # clave ausente
    if i % 29 == 0:
        cliente["segmento"] = segmento.upper()        # categoria sin estandarizar
    clientes.append(cliente)

with open(AQUI / "clientes_crm.json", "w", encoding="utf-8") as f:
    json.dump({"exportado": "2026-01-05", "origen": "CRM", "clientes": clientes},
              f, ensure_ascii=False, indent=2)

# ------------------------------------------------------------------- ventas
CANALES = ["Tienda", "Web", "Televentas"]
MES_PESO = np.array([0.8, 0.75, 0.85, 0.9, 1.0, 1.05, 0.95, 0.9, 0.95, 1.0, 1.25, 1.6])
dias = pd.date_range("2025-01-01", "2025-12-31", freq="D")
peso_dia = MES_PESO[dias.month - 1]
peso_dia = peso_dia / peso_dia.sum()

MULT_SEGMENTO = {"Hogar": 1.0, "Pyme": 2.2, "Corporativo": 4.5}
seg_de = {c["id"]: c["segmento"].capitalize() for c in clientes}
ciudad_de = {c["id"]: c["direccion"]["ciudad"] for c in clientes}

ventas = []
for k in range(1, 1501):
    cli = f"C{int(rng.integers(1, 121)):04d}"
    prod = df_prod.iloc[int(rng.integers(0, len(df_prod)))]
    canal = str(rng.choice(CANALES, p=[0.45, 0.40, 0.15]))
    cantidad = max(1, int(rng.poisson(1.6 * MULT_SEGMENTO[seg_de[cli]])))
    # El canal Web vende con un descuento leve; cada linea tiene ruido de precio
    descuento = 0.07 if canal == "Web" else 0.0
    precio = prod["precio_lista"] * (1 - descuento) * rng.uniform(0.97, 1.03)
    ventas.append({
        "id_venta": f"V{k:05d}",
        "fecha": pd.Timestamp(rng.choice(dias, p=peso_dia)),
        "cod_cliente": cli,
        "sku": prod["sku"],
        "cantidad": cantidad,
        "precio_unitario": round(float(precio), 2),
        "canal": canal,
        "ciudad": ciudad_de[cli],
    })
df = pd.DataFrame(ventas).sort_values("fecha").reset_index(drop=True)
df["id_venta"] = [f"V{k:05d}" for k in range(1, len(df) + 1)]

# --- Defectos intencionales del ERP (se documentan en el README del caso)
df = df.astype({"cantidad": "object"})
idx = rng.permutation(len(df))

def fmt_fecha(i, ts):                       # dos formatos de fecha conviviendo
    return ts.strftime("%Y-%m-%d") if i % 4 == 0 else ts.strftime("%d/%m/%Y")
df["fecha"] = [fmt_fecha(i, ts) for i, ts in enumerate(df["fecha"])]

df["precio_unitario"] = df["precio_unitario"].map(lambda v: f"{v:.2f}".replace(".", ","))  # coma decimal

for i in idx[:30]:
    df.at[i, "cantidad"] = None             # cantidades nulas
for i in idx[30:42]:
    df.at[i, "cantidad"] = -int(df.at[i, "cantidad"])   # negativas (devoluciones mal cargadas)
for i in idx[42:120]:
    df.at[i, "cod_cliente"] = f" {df.at[i, 'cod_cliente'].lower()} "   # llave sucia
for i in idx[120:180]:
    df.at[i, "sku"] = df.at[i, "sku"].lower()
for i in idx[180:400]:                      # ciudades escritas de varias formas
    c = df.at[i, "ciudad"]
    sin_tilde = c.translate(str.maketrans("áéíóú", "aeiou"))
    df.at[i, "ciudad"] = random.choice([c.upper(), sin_tilde, f" {sin_tilde.lower()}"])
for i in idx[400:408]:
    df.at[i, "cod_cliente"] = f"C{int(rng.integers(900, 999)):04d}"     # clientes que no existen en el CRM
for i in idx[408:413]:
    df.at[i, "precio_unitario"] = None
df = pd.concat([df, df.iloc[idx[420:445]]], ignore_index=True)           # 25 filas duplicadas
df = df.sample(frac=1, random_state=SEMILLA).reset_index(drop=True)

df.to_csv(AQUI / "ventas_erp.csv", sep=";", index=False, encoding="latin-1")

print("productos.csv     ", df_prod.shape)
print("clientes_crm.json ", len(clientes), "clientes")
print("ventas_erp.csv    ", df.shape)
