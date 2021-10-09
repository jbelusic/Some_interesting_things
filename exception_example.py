import sys
import traceback

def my_exception_hook(type, value, tb):
    """
    Intended to be assigned to sys.exception as a hook.
    Gives programmer opportunity to do something useful with info from uncaught exceptions.

    Parameters
    type: Exception type
    value: Exception's value
    tb: Exception's traceback
    """

    # NOTE: because format() is returning a list of string,
    # I'm going to join them into a single string, separating each with a new line
    traceback_details = '\n'.join(traceback.extract_tb(tb).format())

    error_msg = "An exception has been raised outside of a try/except!!!\n" \
                f"Type: {type}\n" \
                f"Value: {value}\n" \
                f"Traceback: {traceback_details}"
    print(error_msg)

sys.excepthook = my_exception_hook

# Let's do something silly now
x = 10 + "10"
