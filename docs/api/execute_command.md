# Object: execute_command

**Type**: [`function`](../classes/function.md)

## Description


execute_command( (str)command [, (bool)blocking=True [, (bool)shell=False [, (bool)capture_stdout=False [, (bool)capture_stderr=False]]]]) -> tuple :

    Execute command line through the Autodesk Flame Multi-Purpose Daemon.

    This way of starting new processes is better since any native python

    subprocess command (os.system, subprocess, Popen, etc) will call fork()

    which will duplicate the process memory before calling exec().

    This can be costly especially for a process like Flame.

    

    command -- Command line to execute.

    blocking -- If True, will not return until the command line has completed.

    shell -- Should the command be executed in a sh shell.

             WARNING Using shell=True can be a security hazard.

    capture_stdout -- If True, stdout of the command will be captured and

                      returned instead of forwarded to the application stdout.

                      Requires blocking=True

    capture_stderr -- If True, stdout of the command will be captured and

                      returned instead of forwarded to the application stderr.

                      Requires blocking=True

    

    Note: Environment variables will not be forwarded to the executed command.