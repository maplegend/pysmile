import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.sections = {}
        self.current_section = ""

    def start(self):
        self.start_time = time.time()

    def stop(self):
        t = time.time() - self.start_time
        if self.current_section in self.sections:
            self.sections[self.current_section].append(t)
        else:
            self.sections[self.current_section] = [t]

    def new_section(self, name):
        self.current_section = name

    def save(self, fname):
        f = open(fname, "w")
        for name, sec in self.sections.items():
            f.write(name+"\n")
            for t in sec:
                f.write(str(t)+"\n")
        f.close()
