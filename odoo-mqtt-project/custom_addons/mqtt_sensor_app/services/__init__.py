from . import mqtt_service
from . import db_service

# Instanciar servicios si quieres acceso global desde otros módulos
mqtt = mqtt_service.MQTTService()
db = db_service.ExternalDBService()

# Iniciar el cliente MQTT si quieres que empiece al cargar el módulo
mqtt.start()
