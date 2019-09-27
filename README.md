# Bikeshare-Exploration-Model
# install the pint function which works with units in python
!pip install pint

# Configure Jupyter so figures appear in the notebook
%matplotlib inline

# Configure Jupyter to display the assigned value after an assignment
%config InteractiveShell.ast_node_interactivity='last_expr_or_assign'

# import functions from the modsim library
from modsim import *

# set the random number generator
np.random.seed(7)
bikeshare= State(A=30,B=30,C=30)
#step function takes state which are the locations and 3 different probablities of those locations with given probablities.

def step(state, p1, p2, p3):

    if flip(p1):
        bike_to_A(state)
    
    if flip(p2):
        bike_to_B(state)
        
    if flip(p3):
        bike_to_C(state)

#bike_to_A, bike_to_B, bike_to_C contains logic of eliminating the chance of having negative bikes, and increase or decrease bikes depending on which state the bike goes to. 

def bike_to_A(state):
    if state.C == 0:
        return
    state.C -= 1
    state.A += 1
    
    if state.B==0:
        return
    state.B -= 1
    state.A += 1
    
def bike_to_B(state):

    if state.A == 0:
        return
    state.A -= 1
    state.B += 1
    
    if state.C==0:
        return
    state.C -= 1
    state.B += 1
    
def bike_to_C(state):

    if state.B == 0:
        return
    state.B -= 1
    state.C += 1
    
    if state.A==0:
        return
    state.A -= 1
    state.C += 1
    
# decorate_bikeshare function is how the plot will be and label title, x and y axis, after given exact variables for bikeshare.

def decorate_bikeshare():
    decorate(title='Bikeshare Model',
             xlabel='Time(hrs)', 
             ylabel='Number of bikes')
# run_simulation function takes 3 states, it's probablilites, and the time steps, it runs a for loop and generate numbers for different time steps and number of bikes for each location. 

def run_simulation(state, p1, p2,p3, num_steps):
    resultsA = TimeSeries(state.A)    
    resultsB = TimeSeries(state.B)
    resultsC = TimeSeries(state.C) 
    for i in range(num_steps):
        step(state, p1, p2, p3)
        resultsA[i] = state.A
        resultsB[i] = state.B
        resultsC[i] = state.C
    plot(resultsA, label='A')
    plot(resultsB, label='B')
    plot(resultsC, label='C')

# After giving values of 3 different states, their probabilities and time steps, it generates this plot.

bikeshare= State(A=30,B=30,C=30)
run_simulation(bikeshare, 0.33, 0.33,0.33, 24)
decorate_bikeshare()
