from omni_model.src.utils.logger import Logger


# TODO: better overwritting
def print(*msg):
    Logger().log_message(*msg, stack_displacement=2)