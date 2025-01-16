# Example file showing a circle moving on screen
from neural_net_classes import *
import pygame as pg
#running = True
#dt = 0

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800





def main():

    number_of_layers = 0
    global neur_in_lay
    """ while True:
        try:
            number_of_layers = int(input("How many layers of neurons?"))
        except:
            pass
        else:
            break
    while True:
        try:
            neurons_in_layers = (input("How many neurons in each layer? Type in numbers, separate by comma"))
            neurons_in_layers = neurons_in_layers.split(",")

            neur_in_lay = []

            for number in neurons_in_layers:
                neur_in_lay.append(int(number)) 
            print(neur_in_lay)

        except:
            pass
        else:
            break """
    div_horisontal = number_of_layers+2
    div_vertical = max(neur_in_lay)
    print(div_vertical)

    
    
def main2():

    #The list of number of neurons in each layer
    neur_in_lay = [1,2,1]
    number_of_layers = len(neur_in_lay)

    #The horisontal and vertical division of available space    
    div_horisontal = number_of_layers+1
    div_vertical = max(neur_in_lay)+1
    #print(div_vertical)

    #initialiazing list of neurons as a list, a list of lists and a 
    #list of dictionaries. Planning to delete all but one of these later
    neurons_2dim_list = []
    
    #setting up the neurons in the layers
    for i in range(len(neur_in_lay)):

        #standard way of making 2-dim lists
        row = []

        for j in range(neur_in_lay[i]):
            x = SCREEN_WIDTH/div_horisontal*(i+1)
            y = SCREEN_HEIGHT/div_vertical*(j+1+0.5*(max(neur_in_lay)-neur_in_lay[i]))
            neur = Neuron(x = x, y = y, layer = i, 
                          radius = SCREEN_HEIGHT/(3*div_vertical), 
                                                  axon = Axon(x,y))
            #it shows to be helpful to include the position of the axon
            #neur.axon = Axon(neur.x, neur.y)
            row.append(neur)
        neurons_2dim_list.append(row)

    neural_net = Network(neur_in_lay,neurons_2dim_list)
    
    #for almost all layers, except the last layer
    for i in range(len(neurons_2dim_list)-1):
        #except the last layer

        for neur_j in ((neurons_2dim_list[i])):
            #for all neurons in the layer
            #neur_j = neurons_2dim_list[i][j]

            for neur_k in (neurons_2dim_list[i+1]):
                #for all neurons in the next layer
                #neur_k = neurons_2dim_list[k][k]
                neur_j.axon.add_connection(neur_k)


    
    """ for row in neurons:
        for neuron in row:
            print("(",neuron.x,",",neuron.y,")",end = "")
        print() """
    for layer in neurons_2dim_list:
        for neuron in layer:
            #print(neuron.axon)
            neuron.axon.print_connections()
        

    neural_net.show_neurons(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT)



if __name__=="__main__":
    main2()