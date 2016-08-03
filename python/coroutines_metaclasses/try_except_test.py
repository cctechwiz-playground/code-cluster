# untrusted try except decorator
# ##############################
def untrusted(err_handler): # decorator factory, returns decorator
    def decorator(func): # decorator, returns new function
        def func_wrapper(*args, **kwargs): # new function, modifies func
            try:
                func(*args, **kwargs) # function decorated
            except Exception as e:
                err_handler(e)
            finally:
                print("I have graciously resolved this... You're welcome...")
                # In reality I would probably log all errors to a DB here
        return func_wrapper
    return decorator

# Custom Exceptions
# #################
class CustomException(Exception):
    """My very own Exception"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Error handlers
# ##############
def err_log(e):
    print("Error:", e)
    # add logger here

def err_fatal(e):
    print("Fatal Error:", e)
    quit()

# Is the needed? Wouldn't I just make a new error handler to fix the issue?
# I could use @untrusted(err_handler, rollback=None) to have specific logic
def err_pass(e):
    print("Passing Error:", e)
    e.value = "Went through error handler."
    raise e from e

def err_squash(e):
    print("Squashing:", e)
    # need to be able to continue function execution if possible
    # supress() => python 3

# Untrusted methods
# #################
@untrusted(err_log)
def throws_logged_error():
    raise Exception('I did this on purpose!')
    print("Should not get here")

@untrusted(err_pass)
def throws_passed_error():
    raise ValueError('Something happened I should resolve where called!')
    print("Should not get here")

@untrusted(err_squash)
def throws_squashed_error():
    raise Exception('This is going away!')
    print("Should not get here")

@untrusted(err_log)
def throws_custom_error():
    raise CustomException('I\'m so custom')
    print("Should not get here")

@untrusted(err_fatal)
def throws_fatal_error():
    raise ValueError('This is a really bad error!')
    print("Should not get here")

# Main
# ####
throws_logged_error()

try:
    throws_passed_error()
except Exception as e:
    print(e, e.value)

throws_squashed_error()

throws_custom_error()

throws_fatal_error()
