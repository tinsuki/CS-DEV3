import cProfile, pstats, io
from pstats import SortKey

global _time_profiler

def start():
    global _time_profiler
    # new profiler
    _time_profiler = cProfile.Profile()
    # enable profiler
    _time_profiler.enable()

def stop():
    global _time_profiler
    # disable profiler
    _time_profiler.disable()
    # dispkay statistics
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(_time_profiler, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
