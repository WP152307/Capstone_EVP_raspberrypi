import node_edge
import pcf
import time

node_0 = node_edge.Node_0()
node_1 = node_edge.Node_1()
node_2 = node_edge.Node_2()
node_3 = node_edge.Node_3()
node_4 = node_edge.Node_4()
node_5 = node_edge.Node_5()
node_6 = node_edge.Node_6()
node_7 = node_edge.Node_7()
node_8 = node_edge.Node_8()
node_9 = node_edge.Node_9()
node_10 = node_edge.Node_10()

def ceremony():

    for j in range(5):
        for i in range(8):
            pcf.Rled['one'][i].value = True
            pcf.Rled['two'][i].value = True
            pcf.Rled['three'][i].value = True
            pcf.Rled['four'][i].value = True
            pcf.Rled['five'][i].value = True

            pcf.Gled['one'][i].value = False
            pcf.Gled['two'][i].value = False
            pcf.Gled['three'][i].value = False
            pcf.Gled['four'][i].value = False
            pcf.Gled['five'][i].value = False

        time.sleep(0.2)

        for i in range(8):
            pcf.Rled['one'][i].value = False
            pcf.Rled['two'][i].value = False
            pcf.Rled['three'][i].value = False
            pcf.Rled['four'][i].value = False
            pcf.Rled['five'][i].value = False

            pcf.Gled['one'][i].value = True
            pcf.Gled['two'][i].value = True
            pcf.Gled['three'][i].value = True
            pcf.Gled['four'][i].value = True
            pcf.Gled['five'][i].value = True

        time.sleep(0.2)


green = {'one': set(), 'two': set(), 'three': set(), 'four': set(), 'five': set()}
red = {'one': set(), 'two': set(), 'three': set(), 'four': set(), 'five': set()}

def make_all_red(green,red):
    names = ['one', 'two', 'three', 'four', 'five']
    for name in names:
        for i in range(8):
            if i not in green[name]:
                pcf.Gled[name][i].value = False
            if i in red[name]:
                pcf.Rled[name][i].value = False
            else:
                pcf.Rled[name][i].value = True
    for key in green:
        green[key].clear()
    for key in red:
        red[key].clear()



def shortest_path(results):

    global green
    global red
    make_all_red(green,red)

    for i in range(len(results) - 1):

        if results[i] == 0 and results[i + 1] == 1:
            node_1.left_signal()
            green['one'].add(2)
            red['one'].add(5)
        elif results[i] == 1 and results[i + 1] == 0:
            node_0.right_signal()
            green['two'].add(5)
            red['two'].add(2)

        elif results[i] == 1 and results[i + 1] == 2:
            node_2.left_signal()
            green['one'].add(6)
            red['one'].add(1)
        elif results[i] == 2 and results[i + 1] == 1:
            node_1.right_signal()
            green['one'].add(1)
            red['one'].add(6)

        elif results[i] == 0 and results[i + 1] == 3:
            node_3.bottom_signal()
            green['two'].add(3)
            red['two'].add(4)
        elif results[i] == 3 and results[i + 1] == 0:
            node_0.top_signal()
            green['two'].add(4)
            red['two'].add(3)

        elif results[i] == 1 and results[i + 1] == 5:
            node_5.bottom_signal()
            green['four'].add(7)
            red['four'].add(0)
        elif results[i] == 5 and results[i + 1] == 1:
            node_1.top_signal()
            green['one'].add(0)
            red['one'].add(7)

        elif results[i] == 2 and results[i + 1] == 6:
            node_6.bottom_signal()
            green['three'].add(7)
            red['three'].add(0)
        elif results[i] == 6 and results[i + 1] == 2:
            node_2.top_signal()
            green['one'].add(4)
            red['one'].add(3)

        elif results[i] == 3 and results[i + 1] == 4:
            node_4.left_signal()
            green['four'].add(5)
            red['four'].add(2)
        elif results[i] == 4 and results[i + 1] == 3:
            node_3.right_signal()
            green['two'].add(1)
            red['two'].add(6)

        elif results[i] == 4 and results[i + 1] == 5:
            node_5.left_signal()
            green['four'].add(6)
            red['four'].add(1)
        elif results[i] == 5 and results[i + 1] == 4:
            node_4.right_signal()
            green['four'].add(3)
            red['four'].add(4)

        elif results[i] == 5 and results[i + 1] == 6:
            node_6.left_signal()
            green['three'].add(6)
            red['three'].add(1)
        elif results[i] == 6 and results[i + 1] == 5:
            node_5.right_signal()
            green['four'].add(4)
            red['four'].add(3)

        elif results[i] == 3 and results[i + 1] == 7:
            node_7.bottom_signal()
            green['five'].add(3)
            red['five'].add(4)
        elif results[i] == 7 and results[i + 1] == 3:
            node_3.top_signal()
            green['two'].add(0)
            red['two'].add(7)

        elif results[i] == 4 and results[i + 1] == 8:
            node_8.bottom_signal()
            green['five'].add(5)
            red['five'].add(2)
        elif results[i] == 8 and results[i + 1] == 4:
            node_4.top_signal()
            green['five'].add(7)
            red['five'].add(0)

        elif results[i] == 5 and results[i + 1] == 9:
            node_9.bottom_signal()
            green['four'].add(1)
            red['four'].add(6)
        elif results[i] == 9 and results[i + 1] == 5:
            node_5.top_signal()
            green['four'].add(2)
            red['four'].add(5)

        elif results[i] == 6 and results[i + 1] == 10:
            node_10.bottom_signal()
            green['three'].add(3)
            red['three'].add(4)
        elif results[i] == 10 and results[i + 1] == 6:
            node_6.top_signal()
            green['three'].add(4)
            red['three'].add(3)

        elif results[i] == 7 and results[i + 1] == 8:
            node_8.left_signal()
            green['five'].add(4)
            red['five'].add(3)
        elif results[i] == 8 and results[i + 1] == 7:
            node_7.right_signal()
            green['five'].add(0)
            red['five'].add(7)

        elif results[i] == 8 and results[i + 1] == 9:
            node_9.left_signal()
            green['five'].add(6)
            red['five'].add(1)
        elif results[i] == 9 and results[i + 1] == 8:
            node_8.right_signal()
            green['five'].add(1)
            red['five'].add(6)

        elif results[i] == 9 and results[i + 1] == 10:
            node_10.left_signal()
            green['three'].add(2)
            red['three'].add(5)
        elif results[i] == 10 and results[i + 1] == 9:
            node_9.right_signal()
            green['four'].add(0)
            red['four'].add(7)

        elif results[i] == 100 and results[i + 1] == 7:
            node_7.left_signal()
            green['five'].add(2)
            red['five'].add(5)
        elif results[i] == 100 and results[i + 1] == 3:
            node_3.left_signal()
            green['two'].add(2)
            red['two'].add(5)
        elif results[i] == 100 and results[i + 1] == 0:
            node_0.left_signal()
            green['two'].add(6)
            red['two'].add(1)

        elif results[i] == 300 and results[i + 1] == 10:
            node_10.right_signal()
            green['three'].add(1)
            red['three'].add(6)
        elif results[i] == 300 and results[i + 1] == 6:
            node_6.right_signal()
            green['three'].add(5)
            red['three'].add(2)
        elif results[i] == 300 and results[i + 1] == 2:
            ceremony()

        elif results[i] == 400 and results[i + 1] == 0:
            node_0.bottom_signal()
            green['two'].add(7)
            red['two'].add(0)
        elif results[i] == 400 and results[i + 1] == 1:
            node_1.bottom_signal()
            green['one'].add(3)
            red['one'].add(4)
        elif results[i] == 400 and results[i + 1] == 2:
            ceremony()

