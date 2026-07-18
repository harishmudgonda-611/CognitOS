class Runtime:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("🚀 Cognit OS Runtime Started")

    def stop(self):
        self.running = False
        print("🛑 Cognit OS Runtime Stopped")

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        return "Running" if self.running else "Stopped"


