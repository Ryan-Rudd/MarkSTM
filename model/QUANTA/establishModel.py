from engine import QUANTA_ENGINE

class QUANTA(object):
    def __init__(self):
        self.version = "0.0.1 Pre Beta Release"
        self.modelName = "QUANTA"
        self.modelDescription = "Quantitative Analytics Neural Trading Algorithm"
        self.modelParent = "MarkSTM Engine"
        self.modelID = 0001 # FORMAT:
        """ 
            MODEL ID:
                { TIMES MODEL DATASET HAS BEEN FINALIZED }
                { MAJOR VERSION }
                { MINOR VERSION }
                { INDEX OF MODEL RELEASES}
        """
        self.engine = QUANTA_ENGINE()
