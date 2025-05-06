# OdooModule

# Aplicació de Sensor MQTT per a Odoo

Aplicació web desenvolupada com a prova tècnica. Mostra:

- El valor d’un sensor MQTT en temps real
- Un gràfic amb l’històric de valors de clor extret d’una base de dades PostgreSQL (estàndard SensorThings)

---

## 🐳 Requisits

- Docker
- Docker Compose

---

## ▶️ Com executar el projecte

1. Clona aquest repositori
2. Obre una terminal a la carpeta del projecte
3. PowerShell - executa:
  docker compose up -d
4. Accedeix a Odoo a través del navegador:
http://localhost:8069

  Primera execució
Quan accedeixis a Odoo, veuràs la pantalla per crear una base de dades nova.
Posa qualsevol nom de base de dades (ex: mqtt_test)
Introdueix un correu (ex: admin@example.com) i una contrasenya (ex: admin)
Fes clic a Crear base de dades

Després d’això, ja podràs navegar a la següent ruta per veure el dashboard:

👉 http://localhost:8069/mqtt_dashboard
