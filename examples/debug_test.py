import debugpy
import time

if __name__ == '__main__':
    # Start debugpy listening on 5678 so you can Attach from VS Code
    debugpy.listen(("0.0.0.0", 5678))
    print("debugpy listening on 5678")
    print("Press Ctrl-C to exit")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
