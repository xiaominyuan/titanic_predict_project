from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
from .task.async_task import async_predict
from .utils.model_utils import predict
from django.core.cache import cache

import logging

logger = logging.getLogger(__name__)

# 同步 API
@csrf_exempt
def titanic_sync(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = predict(data)
            logger.info(f"post body sync: {data}")
            return JsonResponse(result, status=202)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Please use POST"}, status=405)

# 异步 API
@csrf_exempt
def titanic_async(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            job_id = str(uuid.uuid4())
            logger.info(f"post body async before: {data}")
            async_predict.delay(job_id, data)
            logger.info(f"post body async after: {data}")
            return JsonResponse({"job_id": job_id}, status=202)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Please use POST"}, status=405)



# 结果获取 API
def titanic_result(request, job_id):

    result = cache.get(job_id)

    if result is not None:
        # 如果任务完成，返回结果
        return JsonResponse({"status": "success", "result": result})
    else:
        # 如果任务仍在进行或未完成
        return JsonResponse({"status": "PENDING", "message": "Job not completed or job_id does not exist"}, status=404)


# # 结果获取 API
# def titanic_result(request, job_id):
#     # 使用 Celery AsyncResult 获取任务状态和结果
#     result = AsyncResult(job_id)
#
#     if result.state == 'SUCCESS':
#         # 任务成功，返回结果
#         return JsonResponse({
#             'status': result.state,
#             'result': result.result
#         })
#     elif result.state == 'FAILURE':
#         # 任务失败
#         return JsonResponse({
#             'status': result.state,
#             'error': str(result.result)  # 错误信息
#         })
#     else:
#         # 任务尚未完成
#         return JsonResponse({
#             'status': result.state,
#             'message': 'Job not completed or job_id does not exist'
#         }, status=404)
#
def test_alive(request):
    return JsonResponse({"message": "i am alive"}, status=200)
