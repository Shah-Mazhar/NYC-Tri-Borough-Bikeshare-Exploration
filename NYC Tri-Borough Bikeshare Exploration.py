## Getting  Libraries & Functions
# install the pint function which works with units in python
pip install pint

# install modsimpy which import modsim
import modsimpy

# import functions from the modsim library
from modsim import *

# import matplotlib.pyplot which works with graphs and visulization
import matplotlib.pyplot as plt

## Initializing values for 3 boroughs
bikeshare= State(Brooklyn=30,Bronx=30,Queens=30)

## Defining Functions
def step(state, p1, p2, p3):
"""Simulate one minute of time.
    
    state: bikeshare State object
    p1: probability of a bike coming to Brooklyn
    p2: probability of a bike coming to Bronx
    p3: probability of a bike coming to Queens
    """

    if flip(p1):
        bike_to_Brooklyn(state)
    
    if flip(p2):
        bike_to_Bronx(state)
        
    if flip(p3):
        bike_to_Queens(state)

def bike_to_Brooklyn(state):
    """Move one bike from Quens to Brooklyn or
       Move one bike from Bronx to Brooklyn.
    
    state: bikeshare State object
    """
    if state.Queens == 0:
        return
    state.Queens -= 1
    state.Brooklyn += 1
    
    if state.Bronx==0:
        return
    state.Bronx -= 1
    state.Brooklyn += 1
    
def bike_to_Bronx(state):
    """Move one bike from Brooklyn to Bronx or
       Move one bike from Queens to Bronx.
    
    state: bikeshare State object
    """
    if state.Brooklyn == 0:
        return
    state.Brooklyn -= 1
    state.Bronx += 1
    
    if state.Queens==0:
        return
    state.Queens -= 1
    state.Bronx += 1
    
def bike_to_Queens(state):
    """Move one bike from Bronx to Queens or
       Move one bike from Brooklyn to Queens.
    
    state: bikeshare State object
    """

    if state.Bronx == 0:
        return
    state.Bronx -= 1
    state.Queens += 1
    
    if state.Brooklyn==0:
        return
    state.Brooklyn -= 1
    state.Queens += 1

def run_simulation(state, p1, p2,p3, num_steps):
     """Simulate the given number of time steps.
    
    p1: probability of a customer's arrival at Brooklyn
    p2: probability of a customer's arrival at Bronx
    p3: probability of a customer's arrival at Queens
    num_steps: number of time steps
    """
    resultsBrooklyn = TimeSeries(state.Brooklyn)    
    resultsBronx = TimeSeries(state.Bronx)
    resultsQueens = TimeSeries(state.Queens) 
    for i in range(num_steps):
        step(state, p1, p2, p3)
        resultsBrooklyn[i] = state.Brooklyn
        resultsBronx[i] = state.Bronx
        resultsQueens[i] = state.Queens
    plt.plot(resultsBrooklyn, label='Brooklyn')
    plt.plot(resultsBronx, label='Bronx')
    plt.plot(resultsQueens, label='Queens')
    decorate(title='NYC Tri-Borough Bikeshare Exploration',
             xlabel='Time(hrs)', 
             ylabel='Number of bikes')
   
## Result and Plot
#Giving initial value of the number bikes for each borough
bikeshare= State(Brooklyn=30,Bronx=30,Queens=30)

#running the run_simulation() function with defined state, probabilities and time steps
run_simulation(bikeshare, 0.33, 0.33,0.33, 16)
