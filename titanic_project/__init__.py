# titanic_project/__init__.py
from __future__ import absolute_import, unicode_literals

# 使 Celery 在项目启动时就加载
from titanic_project.celery import app as celery_app

__all__ = ('celery_app',)