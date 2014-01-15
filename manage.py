#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line
    sys.path.append('/env/sessions/sessions-model')
    sys.path.append('/env/sessions/users-model')
    execute_from_command_line(sys.argv)
