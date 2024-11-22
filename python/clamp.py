def clamp(lo, hi):
    """
    Generic clamp function.
    """
    def f(val):
        if val > hi: return hi
        if val < lo: return lo
        return val
    return f
