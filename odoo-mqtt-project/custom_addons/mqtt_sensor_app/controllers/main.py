from odoo import http
from odoo.http import request

class MqttSensorController(http.Controller):

    @http.route('/mqtt_dashboard', type='http', auth='public', website=True)
    def mqtt_dashboard(self, **kw):
        return request.render('mqtt_sensor_app.dashboard_template', {})
"""
    @http.route('/mqtt_sensor/data', type='json', auth='public')
    def get_sensor_data(self):
    # Simulación por ahora
        return {
            'labels': ['12:00', '12:05', '12:10', '12:15'],
            'values': [0.5, 0.7, 0.6, 0.9]
        }"""