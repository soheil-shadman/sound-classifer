import math
from pydub import AudioSegment
import os


class MyDataMaker:
    def __init__(self, delete_raw_items):
        self.RAW_DATA_PATH = './raw_data/'
        self.DATA_PATH = './data/'
        self.split_input = 3
        self.delete_raw_items = delete_raw_items

    def get_audio(self, path):
        return AudioSegment.from_wav(self.RAW_DATA_PATH + path)

    def get_duration(self, audio):
        return audio.duration_seconds

    def single_split_seconds(self, audio, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = audio[t1:t2]
        split_audio.export(self.DATA_PATH + split_filename, format="wav")

    def multiple_split_Seconds(self, audiofile, file_name):
        counter = 0
        total_seconds = math.ceil(self.get_duration(audiofile))
        print(total_seconds)
        # 03-01-01-01-01-01-01
        for i in range(0, total_seconds, self.split_input):
            split_fn = str(counter) + '-' + file_name
            self.single_split_seconds(audiofile, i, i + self.split_input, split_fn)
            # print(str(i) + ' Done')
            counter = counter + 1
            if i == total_seconds - self.split_input:
                print('All splited successfully')

    def process_data(self):
        print("processing raw data ...")
        try:
            files = os.listdir(self.RAW_DATA_PATH)
            if len(files) == 0:
                print("now raw data found ...")
                return
            for i in files:
                if self.get_duration(self.get_audio(i)) < self.split_input:
                    print('input is lower than 3 seconds ...')
                else:
                    self.multiple_split_Seconds(self.get_audio(i), i)
                    new_files = os.listdir(self.DATA_PATH)
                    if len(new_files) > 1:
                        for i in new_files:
                            if int(i.split('-')[0]) == len(new_files) - 1:
                                os.remove(self.DATA_PATH + i)

                                print("removing last data !")

                    if self.delete_raw_items:
                        os.remove(self.RAW_DATA_PATH + i)
            print("processing raw data done !")



        except:
            print('problem processing data ...')
