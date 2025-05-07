import paho.mqtt.client as mqtt
import logging

_logger = logging.getLogger(__name__)

class MQTTService:
    def __init__(self, host='10.8.21.61', port=1883, topic='counter/topic'):
        self.client = mqtt.Client()
        self.host = host
        self.port = port
        self.topic = topic
        self.last_value = None  # ⚠️ aquí se guarda el último valor

    def on_connect(self, client, userdata, flags, rc):
        _logger.info(f"[MQTT] Conectado al broker MQTT con código: {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        self.last_value = msg.payload.decode()
        _logger.info(f"[MQTT] Valor recibido del counter: {self.last_value}")

    def start(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.host, self.port, 60)
        self.client.loop_start()

    def get_last_value(self):
        return self.last_value
