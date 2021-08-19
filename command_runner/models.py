import json
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from pexpect import pxssh


class SSHConnection:
    def __init__(self, connection_name):
        self.connection_name = connection_name

    def load_config(self):
        config_path = f'{settings.BASE_DIR}/connections.json'
        with open(config_path, 'r') as f:
            self.config = json.loads(f.read())

    def connect(self):
        self.load_config()
        conn_params = self.config.get(self.connection_name)
        self.ssh_conn = pxssh.pxssh()
        self.ssh_conn.login(
            conn_params.get('host'),
            conn_params.get('user'),
            conn_params.get('password')
        )

    def send_command(self, command):
        self.ssh_conn.sendline(command)
        self.ssh_conn.prompt()

    def disconnect(self):
        self.ssh_conn.logout()


class Machine(models..Model):
    name = models.CharField(max_length=255)


class Command(models.Model):
    name = models.CharField(max_length=255)
    line = models.TextField()


class Result(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'S', _('success')
        FAILED = 'F', _('failed')
        PENDING = 'P', _('pending')

    created = models.DateTimeField(auto_add_now=True)
    command = models.ForeignKey(Command, on_delete=models.IGNORE) # keep results
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.PENDING)

class Execute(models.Model):
    command = # todo
