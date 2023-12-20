import mlrun.serving

class SlotFillerServe(mlrun.serving.V2ModelServer):

    def load(self):
        pass

    def predict(self, body: dict):
        return 1
