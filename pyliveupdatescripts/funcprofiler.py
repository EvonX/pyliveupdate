from pyliveupdate import *
from pyliveupdatescripts import *
import time

class FuncProfiler(UpdateBase):
    
    @staticmethod
    def _func_begin(start):
        start = time.time()
        remote_logger.info('func_begin; {}'.format(start))
        
    @staticmethod
    def _func_end(start):
        end = time.time()
        time_ = (end-start)*1000
        local_logger.info('{:.4f} ms'.format(time_))
        remote_logger.info('func_end; {}; {}'.format(time_, end))
    
    @staticmethod
    def profile(scope):
        scopes = scope
        if isinstance(scope, str):
            scopes = [scope]
        for scope in scopes:
            update = Update('instrument', scope, 
                            {'func_begin': FuncProfiler._func_begin, 
                             'func_end': FuncProfiler._func_end},
                           None, None, __name__)
            UpdateManager.apply_update(update)

FP = FuncProfiler
UpdateBase.register_builtin(globals())