import logging
import time
import inspect
from functools import wraps

def log(level=logging.DEBUG):
    def decorator(target):
        
        if inspect.isclass(target):

            original_init = target.__init__
            
            @wraps(original_init) # dzieki temu nie zmienia nazwy
            def new_init(self, *args, **kwargs):
                start = time.time()
                
                original_init(self, *args, **kwargs)
                
                duration = time.time() - start
                
                logging.log(level, 
                    f"[CLASS] Instantiated: {target.__name__} | "
                    f"Init duration: {duration:.4f}s | "
                    f"Arguments: args={args}, kwargs={kwargs}"
                )
            
            target.__init__ = new_init
            return target
            
        else:
            @wraps(target)
            def wrapper(*args, **kwargs):
                start = time.time()
                
                result = target(*args, **kwargs)
                
                duration = time.time() - start
                
                logging.log(level, 
                    f"[FUNCTION] Name: {target.__name__} | "
                    f"Call time (timestamp): {start:.2f} | "
                    f"Duration: {duration:.4f}s | "
                    f"Arguments: args={args}, kwargs={kwargs} | "
                    f"Returned: {result}"
                )
                
                return result
            return wrapper
            
    return decorator

if __name__ == '__main__':

    # Konfiguracja loggera
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

    @log(level=logging.INFO)
    def pomnoz(a, b):
        time.sleep(0.1)  # for tests
        return a * b

    @log(level=logging.DEBUG)
    class BazaDanych:
        def __init__(self, adres_ip):
            time.sleep(0.2) # for tests
            self.adres_ip = adres_ip

    result_funkcji = pomnoz(5, 4)
    mojabaza = BazaDanych("192.168.1.1")