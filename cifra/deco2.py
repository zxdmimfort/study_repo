import datetime
import inspect


def logging_decorator(logger: list):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            log = {
                'name': func.__name__,
                'arguments': inspect.getcallargs(func, *args, **kwargs),
                'call_time': datetime.datetime.now(),
                }
            res = func(*args, **kwargs)
            log['result'] = res
            logger.append(log)
            return res
        return wrap_args
    return wrap_func


logger = []



@logging_decorator(logger)
def test_simple(a, b=2):
    return 127

test_simple(1)

print(logger)
            

