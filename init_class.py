import os
class InitClass:
    def __init__(self):
        print('init paths')
        self.DATA_PATH = './data/'
        self.RESULT_PATH = './results/'
        self.MODELS_PATH = './models/'
        self.WEIGHTS_PATH = './weights/'
        self.RAW_DATA_PATH = './raw_data/'
        if not os.path.exists(self.DATA_PATH):
            os.makedirs(self.DATA_PATH)
        if not os.path.exists(self.RESULT_PATH):
            os.makedirs(self.RESULT_PATH)
        if not os.path.exists(self.MODELS_PATH):
            os.makedirs(self.MODELS_PATH)
        if not os.path.exists(self.WEIGHTS_PATH):
            os.makedirs(self.WEIGHTS_PATH)
        if not os.path.exists(self.RAW_DATA_PATH):
            os.makedirs(self.RAW_DATA_PATH)

