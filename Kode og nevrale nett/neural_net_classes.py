import pygame as pg

class Game:
    """
    The main class for any pygame-related game or app
    Its instance attributes are

    |---------------------
    |Attributes
    |---------------------
    - screen: pg.display.set_mode
    - clock: pg.time.clock
    - fps: int
    |---------------------
    |Methods:
    |---------------------
    <None>
    """

    def __init__(self, screen_width: int = 1920, screen_height: int = 1200, fps: int = 10):
        pg.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.clock = pg.time.Clock() 
        self.fps = fps

class Axon:
    """
    The class for describing the connection from a neuron
    in a layer to (all?) neurons in the following layer
    
    |---------------------
    |Attributes
    |---------------------
     connects_to: list of neurons
    - weights: list of floats, or should it be dictionary?
    |---------------------
    |Methods:
    |---------------------
    <None>
    """

    def __init__(self, x, y):
        """
        Initializing the starting centre (x, y)
        Initializing an empty list
        The list will be populated by dictionaries with
        key: "node", value: <Node>
        key: "weight:, value: float
        """
        self.pos = (x,y)
        self.x = x
        self.y = y
        self.connections = []
        self.color = "green"
        
    def add_connection(self, connects_to=None, weight: float = 0):
        """
        Adds a new neuron connection
        """
        dict = {}
        dict["neuron"]=connects_to
        dict["weight"] = weight
        self.connections.append(dict)

    def draw(self, screen):
        """
        It seems a bit troublesome to have the draw funcion here
        Because the program will need the starting point for the next node
        And the starting position of this neuron is inaccessible from 
        this axon
        Unless I force it as two parameters (x, y)
        """
        for element in self.connections:
            neuron = element["neuron"]
            pg.draw.line(screen, 
                        color = "red",width = 1,
                        start_pos = (self.pos), end_pos = (neuron.pos))
    def print_connections(self):
        print(f"The connections of this axon at position {self.pos}")
        i = 0
        for connection in self.connections:
            neuron = connection["neuron"]
            print(f"{i}: neuron at position {neuron.pos}")

class Neuron:
    """
    The class for the actual nurons or nodes in the network

    |---------------------
    |Attributes
    |---------------------
    - x and y: coordinates for the center of the circle
    - radius: the radius of the neuron
    - color: color, preferrably "green" format or (R,G,B) tuple
    - width: the thickness of the outline
    - axon: one associated axon with each neuron
    - bias: The incoming bias is added to the neuron's received signal
    - activation: the value called actiavtion value, a non-negative number
    - layer: the layer number. Should it be absolute?

    |---------------------
    |Methods:
    |---------------------
    - draw: illustrates the neuron
    - receive: the process of receiving signals from the previous layer, adding bias
      and calculating the activation function using for this neuron
    """

    def __init__(self, axon, x: float = 0, y: float = 0, radius: float = 50, 
                 color = "white", width = 3, bias: float= 0,
                 layer: int = 0):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.radius = radius
        self.color = color
        self.width = width
        self.bias = bias
        self.activation = 0
        self.layer = layer
        self.axon = axon

    def draw(self, screen):
        pg.draw.circle(screen, center = (self.x, self.y), 
                       color = self.color,radius = self.radius, width = self.width)

    def receive(self, signal):
        self.activation= max(0,signal)#The ReLU function

class Dialogue_box:

    def __init__(self,x,y,length, height):

        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = "Trykk her for å starte nytt nettverk"

class Network:
    """
    The place holder for the total network of nodes with connections
    |---------------------
    |Attributes
    |---------------------
    - None
    |---------------------
    |Methods:
    |---------------------
    - add_neurons: updates the neuron-list with the neuons created in
    the main function of the program
    - add_axons: updates the axons for each neuron, adding random weights
    and connecting neurons to the next layer
    |---------------------
    |Suggested forther development:
    |---------------------
    - Move the axons and weights over to the network. Global matrices (tensors)
    that ensures the simple matrix multiplication, bias addition and activation in
    a smooth way, supporting understanding

    """

    def __init__(self, neurons_per_layer, neurons_2dim_list):
        self.neurons_per_layer = neurons_per_layer
        self.neurons_2dim_list = neurons_2dim_list

    def add_neurons(self,layer,neurons):

        #This should be a list of dictionaries where each element is
        #[{layer: value, neurons: []},....]
        pass 

    def add_axons(self):
        #process
        pass

    def show_neurons(self, screen_width, screen_height):
        """
        The purpose of this "pygame" is simply to display a neural
        network, no interaction required
        """

        game = Game(screen_width, screen_height)
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            game.screen.fill("black")
            for layer in self.neurons_2dim_list:
                for neuron in layer:
                    neuron.draw(game.screen)
                    neuron.axon.draw(game.screen)

            keys = pg.key.get_pressed()
            """ if keys[pg.K_w]:
                player_pos.y -= 300 * dt
            if keys[pg.K_s]:
                player_pos.y += 300 * dt
            if keys[pg.K_a]:
                player_pos.x -= 300 * dt
            if keys[pg.K_d]:
                player_pos.x += 300 * dt
            """
            # flip() the display to put your work on screen
            pg.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            game.clock.tick(game.fps)

        pg.quit()

def main():
    pass

if __name__=="__main__":
    main()