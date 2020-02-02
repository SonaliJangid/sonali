import sys
import traceback


def print_exec_plus():
    """
    Print the usual traceback information, followed by a listing of all the
    local variables in each frame.
    """
    print("---NEW ERROR---")
    tb = sys.exc_info()[2]
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    print("Locals by frame, innermost last")
    # for frame in stack:
    frame = stack[-1]
    print("Frame %s in %s at line %s" % (frame.f_code.co_name,
                                         frame.f_code.co_filename,
                                         frame.f_lineno))
    # for key, value in frame.f_locals.items():
    #     if key == 'soup':
    #         continue
    #     print("\t%20s = " % key, )
    #     # We have to be VERY careful not to cause a new error in our error
    #     # printer! Calling str(  ) on an unknown object could cause an
    #     # error we don't want, so we must use try/except to catch it --
    #     # we can't stop it from happening, but we can and should
    #     # stop it from propagating if it does happen!
    #     try:
    #         print(value)
    #     except:
    #         print("<ERROR WHILE PRINTING VALUE>")
