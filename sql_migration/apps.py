from django.apps import AppConfig


class SqlMigrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sql_migration'
