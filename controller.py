import inp
import imp
import exp
import logger


def start():
    if inp.mod() == '1':
        info = inp.exp()
        exp.expp(info)
        logger.log_info(info)
    else:
        info = inp.inpp()
        imp.impo(info)
        logger.log_info(info)