import psycopg2
import logging

_logger = logging.getLogger(__name__)

class ExternalDBService:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="10.8.21.61",
                port=5432,
                user="mosquitto",
                password="2024.PERTE",
                database="postgres"
            )
            _logger.info("[DB] Conexión exitosa a PostgreSQL externa")
        except Exception as e:
            _logger.error(f"[DB] Error al conectar a PostgreSQL: {e}")

    def get_data(self, query):
        if not self.conn:
            self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            _logger.error(f"[DB] Error ejecutando consulta: {e}")
            return []

    def get_observations_for_thing(self, thing_id):
        if not self.conn:
            self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT o.result, o."phenomenonTime"
                    FROM things t
                    JOIN datastreams d ON t.ID = d."THING_ID"
                    JOIN observations o ON d.ID = o."DATASTREAM_ID"
                    WHERE t.ID = %s
                    ORDER BY o."phenomenonTime" DESC
                    LIMIT 10
                """, (thing_id,))

                return cursor.fetchall()
        except Exception as e:
            _logger.error(f"[DB] Error al obtener observaciones: {e}")
            return []
