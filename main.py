from my_data_maker import MyDataMaker
from my_model import MyModel

model = MyModel(model_number=22)
model.start_processing_data()
model.predict_data(result_number=2)
# model.clear_data_folder()