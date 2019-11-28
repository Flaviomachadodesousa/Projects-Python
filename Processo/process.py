import psutil 

PROCNAME = "Prog_name.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.nice(psutil.HIGH_PRIORITY_CLASS)
        print(proc.nice)
