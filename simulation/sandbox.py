#Only for testing purpose
from simulation import container
from simulation import user_interface as ui


ui.UserInterface.draw_title("SIR Simulation")

ui.UserInterface.draw_category_name("Population Configuration")

population = int(ui.UserInterface.ask_parameter("Insert population value: "))
susceptible = int(ui.UserInterface.ask_parameter("Insert amount of susceptible people: "))
infected = int(ui.UserInterface.ask_parameter("Insert amount of infected people: "))
recovered = int(ui.UserInterface.ask_parameter("Insert amount of recovered people: "))
dead = int(ui.UserInterface.ask_parameter("Insert amount of dead people: "))

ui.UserInterface.draw_category_name("Container Configuration")

size = int(ui.UserInterface.ask_parameter("Container width and height: "))
simulation_time = int(ui.UserInterface.ask_parameter("How long simulation should take (in seconds): "))
interval = float(ui.UserInterface.ask_parameter("How long is simulation interval (in seconds): "))
move_length = float(ui.UserInterface.ask_parameter("How far population instances can move: "))

ui.UserInterface.draw_category_name("Simulation Probabilities")

infection = float(ui.UserInterface.ask_parameter("Infection probability (float): "))
infection_distance = float(ui.UserInterface.ask_parameter("Area size in with person could be infected (float): "))
recover = float(ui.UserInterface.ask_parameter("Recover probability (float): "))
dead_prob = float(ui.UserInterface.ask_parameter("Dead probability (float): "))


box = container.Container(size, population, simulation_time, interval, move_length)

box.initial_set_up(susceptible, infected, recovered, dead, infection_probability=infection,
                   recover_probability=recover, dead_probability=dead_prob,
                   infection_range=infection_distance,)
box.simulation()

ui.UserInterface.draw_category_name("Statistics after simulation")
print("RECOVERED after: {x}".format(x=box.count_recovered()))
print("INFECTED after: {x}".format(x=box.count_infected()))
print("SUSCEPTIBLE after: {x}".format(x=box.count_susceptible()))
print("DEAD after: {x}".format(x=box.count_dead()))