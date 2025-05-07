from odoo import http
from odoo.http import request
from ..services import mqtt_service, db_service

mqtt = mqtt_service.MQTTService()
mqtt.start()

class MqttSensorController(http.Controller):

    @http.route('/mqtt_dashboard', type='http', auth='public', website=True)
    def mqtt_dashboard(self, **kw):
        return request.render('mqtt_sensor_app.dashboard_template', {})

    @http.route('/mqtt_sensor/data', type='json', auth='public')
    def get_sensor_data(self):
        # 1. Valor MQTT actual
        mqtt_value = mqtt.get_last_value()

        # 2. Datos históricos desde PostgreSQL
        db = db_service.ExternalDBService()
        observations = db.get_observations_for_thing('b6899396-139f-11f0-9ef6-8f16bab1c04c')

        # Formatear resultados
        labels = [r[1].strftime('%H:%M') for r in observations][::-1]
        values = [float(r[0]) for r in observations][::-1]

        return {
            'mqtt_value': mqtt_value,
            'labels': labels,
            'values': values
        }
