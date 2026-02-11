from core.logger import get_logger

logger = get_logger()

class Executor:
    def execute(self, task_func, **kwargs):
        try:
            logger.info(f"Executing task: {task_func.__name__}")
            result = task_func(**kwargs)
            logger.info(f"Task completed: {task_func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Task failed: {task_func.__name__} | Error: {str(e)}")
            raise
