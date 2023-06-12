import pcf
import time

class Node_0 :
    def right_signal(self):
        pcf.Gled['two'][5].value = True
        pcf.Rled['two'][2].value = False

        pcf.Rled['two'][3].value = True
        pcf.Rled['two'][1].value = True
        pcf.Rled['two'][0].value = True
        pcf.Gled['two'][4].value = False
        pcf.Gled['two'][6].value = False
        pcf.Gled['two'][7].value = False

    def left_signal(self):
        pcf.Gled['two'][6].value = True
        pcf.Rled['two'][1].value = False

        pcf.Rled['two'][0].value = True
        pcf.Rled['two'][2].value = True
        pcf.Rled['two'][3].value = True
        pcf.Gled['two'][7].value = False
        pcf.Gled['two'][5].value = False
        pcf.Gled['two'][4].value = False

    def top_signal(self):
        pcf.Gled['two'][4].value = True
        pcf.Rled['two'][3].value = False

        pcf.Rled['two'][1].value = True
        pcf.Rled['two'][0].value = True
        pcf.Rled['two'][2].value = True
        pcf.Gled['two'][6].value = False
        pcf.Gled['two'][7].value = False
        pcf.Gled['two'][5].value = False

    def bottom_signal(self) :
        pcf.Gled['two'][7].value = True
        pcf.Rled['two'][0].value = False

        pcf.Rled['two'][2].value = True
        pcf.Rled['two'][3].value = True
        pcf.Rled['two'][1].value = True
        pcf.Gled['two'][5].value = False
        pcf.Gled['two'][4].value = False
        pcf.Gled['two'][6].value = False

class Node_1 :
    def right_signal(self):
        pcf.Gled['one'][1].value = True
        pcf.Rled['one'][6].value = False

        pcf.Rled['one'][7].value = True
        pcf.Rled['one'][5].value = True
        pcf.Rled['one'][4].value = True
        pcf.Gled['one'][0].value = False
        pcf.Gled['one'][2].value = False
        pcf.Gled['one'][3].value = False

    def left_signal(self) :
        pcf.Gled['one'][2].value = True
        pcf.Rled['one'][5].value = False

        pcf.Rled['one'][4].value = True
        pcf.Rled['one'][6].value = True
        pcf.Rled['one'][7].value = True
        pcf.Gled['one'][3].value = False
        pcf.Gled['one'][1].value = False
        pcf.Gled['one'][0].value = False
    def top_signal(self) :
        pcf.Gled['one'][0].value = True
        pcf.Rled['one'][7].value = False

        pcf.Rled['one'][5].value = True
        pcf.Rled['one'][4].value = True
        pcf.Rled['one'][6].value = True
        pcf.Gled['one'][2].value = False
        pcf.Gled['one'][3].value = False
        pcf.Gled['one'][1].value = False

    def bottom_signal(self) :
        pcf.Gled['one'][3].value = True
        pcf.Rled['one'][4].value = False

        pcf.Rled['one'][6].value = True
        pcf.Rled['one'][7].value = True
        pcf.Rled['one'][5].value = True
        pcf.Gled['one'][1].value = False
        pcf.Gled['one'][0].value = False
        pcf.Gled['one'][2].value = False

class Node_2 :
    def right_signal(self):
        pcf.Gled['one'][5].value = True
        pcf.Rled['one'][2].value = False

        pcf.Rled['one'][3].value = True
        pcf.Rled['one'][1].value = True
        pcf.Rled['one'][0].value = True
        pcf.Gled['one'][4].value = False
        pcf.Gled['one'][6].value = False
        pcf.Gled['one'][7].value = False


    def left_signal(self):
        pcf.Gled['one'][6].value = True
        pcf.Rled['one'][1].value = False

        pcf.Rled['one'][0].value = True
        pcf.Rled['one'][2].value = True
        pcf.Rled['one'][3].value = True
        pcf.Gled['one'][7].value = False
        pcf.Gled['one'][5].value = False
        pcf.Gled['one'][4].value = False


    def top_signal(self):
        pcf.Gled['one'][4].value = True
        pcf.Rled['one'][3].value = False

        pcf.Rled['one'][1].value = True
        pcf.Rled['one'][0].value = True
        pcf.Rled['one'][2].value = True
        pcf.Gled['one'][6].value = False
        pcf.Gled['one'][7].value = False
        pcf.Gled['one'][5].value = False

    def bottom_signal(self):
        pcf.Gled['one'][7].value = True
        pcf.Rled['one'][0].value = False

        pcf.Rled['one'][2].value = True
        pcf.Rled['one'][3].value = True
        pcf.Rled['one'][1].value = True
        pcf.Gled['one'][5].value = False
        pcf.Gled['one'][4].value = False
        pcf.Gled['one'][6].value = False

class Node_3:
    def right_signal(self):
        pcf.Gled['two'][1].value = True
        pcf.Rled['two'][6].value = False

        pcf.Rled['two'][7].value = True
        pcf.Rled['two'][5].value = True
        pcf.Rled['two'][4].value = True
        pcf.Gled['two'][0].value = False
        pcf.Gled['two'][2].value = False
        pcf.Gled['two'][3].value = False

    def left_signal(self):
        pcf.Gled['two'][2].value = True
        pcf.Rled['two'][5].value = False

        pcf.Rled['two'][4].value = True
        pcf.Rled['two'][6].value = True
        pcf.Rled['two'][7].value = True
        pcf.Gled['two'][3].value = False
        pcf.Gled['two'][1].value = False
        pcf.Gled['two'][0].value = False

    def top_signal(self):
        pcf.Gled['two'][0].value = True
        pcf.Rled['two'][7].value = False

        pcf.Rled['two'][5].value = True
        pcf.Rled['two'][4].value = True
        pcf.Rled['two'][6].value = True
        pcf.Gled['two'][2].value = False
        pcf.Gled['two'][3].value = False
        pcf.Gled['two'][1].value = False

    def bottom_signal(self):
        pcf.Gled['two'][3].value = True
        pcf.Rled['two'][4].value = False

        pcf.Rled['two'][6].value = True
        pcf.Rled['two'][7].value = True
        pcf.Rled['two'][5].value = True
        pcf.Gled['two'][1].value = False
        pcf.Gled['two'][0].value = False
        pcf.Gled['two'][2].value = False

class Node_4:
    def right_signal(self):
        pcf.Gled['four'][3].value = True
        pcf.Rled['four'][4].value = False

        pcf.Rled['five'][0].value = True
        pcf.Rled['four'][2].value = True
        pcf.Gled['five'][7].value = False
        pcf.Gled['four'][5].value = False

    def left_signal(self):
        pcf.Gled['four'][5].value = True
        pcf.Rled['four'][2].value = False

        pcf.Rled['four'][4].value = True
        pcf.Rled['five'][0].value = True
        pcf.Gled['four'][3].value = False
        pcf.Gled['five'][7].value = False

    def top_signal(self):
        pcf.Gled['five'][7].value = True
        pcf.Rled['five'][0].value = False

        pcf.Rled['four'][2].value = True
        pcf.Rled['four'][4].value = True
        pcf.Gled['four'][5].value = False
        pcf.Gled['four'][3].value = False

class Node_5:
    def right_signal(self):
        pcf.Gled['four'][4].value = True
        pcf.Rled['four'][3].value = False

        pcf.Rled['four'][5].value = True
        pcf.Rled['four'][1].value = True
        pcf.Rled['four'][0].value = True
        pcf.Gled['four'][2].value = False
        pcf.Gled['four'][6].value = False
        pcf.Gled['four'][7].value = False

    def left_signal(self):
        pcf.Gled['four'][6].value = True
        pcf.Rled['four'][1].value = False

        pcf.Rled['four'][0].value = True
        pcf.Rled['four'][3].value = True
        pcf.Rled['four'][5].value = True
        pcf.Gled['four'][7].value = False
        pcf.Gled['four'][4].value = False
        pcf.Gled['four'][2].value = False

    def top_signal(self):
        pcf.Gled['four'][2].value = True
        pcf.Rled['four'][5].value = False

        pcf.Rled['four'][1].value = True
        pcf.Rled['four'][0].value = True
        pcf.Rled['four'][3].value = True
        pcf.Gled['four'][6].value = False
        pcf.Gled['four'][7].value = False
        pcf.Gled['four'][4].value = False

    def bottom_signal(self):
        pcf.Gled['four'][7].value = True
        pcf.Rled['four'][0].value = False

        pcf.Rled['four'][3].value = True
        pcf.Rled['four'][5].value = True
        pcf.Rled['four'][1].value = True
        pcf.Gled['four'][4].value = False
        pcf.Gled['four'][2].value = False
        pcf.Gled['four'][6].value = False

class Node_6:
    def right_signal(self):
        pcf.Gled['three'][5].value = True
        pcf.Rled['three'][2].value = False

        pcf.Rled['three'][3].value = True
        pcf.Rled['three'][1].value = True
        pcf.Rled['three'][0].value = True
        pcf.Gled['three'][4].value = False
        pcf.Gled['three'][6].value = False
        pcf.Gled['three'][7].value = False

    def left_signal(self):
        pcf.Gled['three'][6].value = True
        pcf.Rled['three'][1].value = False

        pcf.Rled['three'][0].value = True
        pcf.Rled['three'][2].value = True
        pcf.Rled['three'][3].value = True
        pcf.Gled['three'][7].value = False
        pcf.Gled['three'][5].value = False
        pcf.Gled['three'][4].value = False

    def top_signal(self):
        pcf.Gled['three'][4].value = True
        pcf.Rled['three'][3].value = False

        pcf.Rled['three'][1].value = True
        pcf.Rled['three'][0].value = True
        pcf.Rled['three'][2].value = True
        pcf.Gled['three'][6].value = False
        pcf.Gled['three'][7].value = False
        pcf.Gled['three'][5].value = False

    def bottom_signal(self):
        pcf.Gled['three'][7].value = True
        pcf.Rled['three'][0].value = False

        pcf.Rled['three'][2].value = True
        pcf.Rled['three'][3].value = True
        pcf.Rled['three'][1].value = True
        pcf.Gled['three'][5].value = False
        pcf.Gled['three'][4].value = False
        pcf.Gled['three'][6].value = False

class Node_7:
    def right_signal(self):
        pcf.Gled['five'][0].value = True
        pcf.Rled['five'][7].value = False

        pcf.Rled['five'][5].value = True
        pcf.Rled['five'][4].value = True
        pcf.Gled['five'][2].value = False
        pcf.Gled['five'][3].value = False

    def left_signal(self):
        pcf.Gled['five'][2].value = True
        pcf.Rled['five'][5].value = False

        pcf.Rled['five'][4].value = True
        pcf.Rled['five'][7].value = True
        pcf.Gled['five'][3].value = False
        pcf.Gled['five'][0].value = False

    def bottom_signal(self):
        pcf.Gled['five'][3].value = True
        pcf.Rled['five'][4].value = False

        pcf.Rled['five'][7].value = True
        pcf.Rled['five'][5].value = True
        pcf.Gled['five'][0].value = False
        pcf.Gled['five'][2].value = False

class Node_8:
    def right_signal(self):
        pcf.Gled['five'][1].value = True
        pcf.Rled['five'][6].value = False

        pcf.Rled['five'][3].value = True
        pcf.Rled['five'][2].value = True
        pcf.Gled['five'][4].value = False
        pcf.Gled['five'][5].value = False

    def left_signal(self):
        pcf.Gled['five'][4].value = True
        pcf.Rled['five'][3].value = False

        pcf.Rled['five'][2].value = True
        pcf.Rled['five'][6].value = True
        pcf.Gled['five'][5].value = False
        pcf.Gled['five'][1].value = False

    def bottom_signal(self):
        pcf.Gled['five'][5].value = True
        pcf.Rled['five'][2].value = False

        pcf.Rled['five'][6].value = True
        pcf.Rled['five'][3].value = True
        pcf.Gled['five'][1].value = False
        pcf.Gled['five'][4].value = False

class Node_9:
    def right_signal(self):
        pcf.Gled['four'][0].value = True
        pcf.Rled['four'][7].value = False

        pcf.Rled['five'][1].value = True
        pcf.Rled['four'][6].value = True
        pcf.Gled['five'][6].value = False
        pcf.Gled['four'][1].value = False

    def left_signal(self):
        pcf.Gled['five'][6].value = True
        pcf.Rled['five'][1].value = False

        pcf.Rled['four'][6].value = True
        pcf.Rled['four'][7].value = True
        pcf.Gled['four'][1].value = False
        pcf.Gled['four'][0].value = False

    def bottom_signal(self):
        pcf.Gled['four'][1].value = True
        pcf.Rled['four'][6].value = False

        pcf.Rled['four'][7].value = True
        pcf.Rled['five'][1].value = True
        pcf.Gled['four'][0].value = False
        pcf.Gled['five'][6].value = False

class Node_10:
    def right_signal(self):
        pcf.Gled['three'][1].value = True
        pcf.Rled['three'][6].value = False

        pcf.Rled['three'][5].value = True
        pcf.Rled['three'][4].value = True
        pcf.Gled['three'][2].value = False
        pcf.Gled['three'][3].value = False

    def left_signal(self):
        pcf.Gled['three'][2].value = True
        pcf.Rled['three'][5].value = False

        pcf.Rled['three'][4].value = True
        pcf.Rled['three'][6].value = True
        pcf.Gled['three'][3].value = False
        pcf.Gled['three'][1].value = False

    def bottom_signal(self):
        pcf.Gled['three'][3].value = True
        pcf.Rled['three'][4].value = False

        pcf.Rled['three'][6].value = True
        pcf.Rled['three'][5].value = True
        pcf.Gled['three'][1].value = False
        pcf.Gled['three'][2].value = False






