from celery import shared_task
from django.core.cache import cache
from titanic_project.utils.model_utils import predict

import logging

logger = logging.getLogger("titanic_project.task")


@shared_task
def async_predict(job_id, data):
    logger.info(f"Starting prediction for job_id: {job_id}")
    result = predict(data)
    logger.info(f"Prediction result: {result}")
    cache.set(job_id, float(result['probability']), timeout=3600)
    logger.info(f"Result cached for job_id: {job_id}")