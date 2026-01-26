# Function: schedule_idle_event

**Module**: `flame`

**Signature**: `schedule_idle_event(...)`

schedule_idle_event( (object)function [, (int)delay=0]) -> None :
    Register a function callback that will be called eventually when the application is idle. The function must not block and be quick since it will be executed in the main application thread.
    Keyword arguments:
    function -- Callable object to be called.
    delay -- Minimum time (in seconds) to wait before calling function.
    

