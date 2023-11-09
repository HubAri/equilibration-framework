# network-equilibration

Counterpart of Thesis: "Traffic Equilibrium Models: A Comparison of User Equilibrium Models and Implementation of
Framework using Link Flow Assignment". As explained in the paper, the presented framework is based on the UE model 
implementation from the TA-lab https://github.com/nlperic/ta-lab [57]. Furthermore, all network data 
(input values of SiouxFalls_network.csv and SiouxFalls_trips.json) used in this tool was provided 
by the Transportation Networks-Repository https://github.com/bstabler/TransportationNetworks [58].
In this case, equilibrium results were computed on the network of Sioux Falls. 
Corresponding outputs of Sioux Falls further visualized in "PythonNotebook- AdditionalResults", which are discussed in the paper.
OD demand of Sioux Falls used in "PythonNotebook- AdditionalResults" extracted from http://jlitraffic.appspot.com/tap.html [60].

## TUM Project at the FTM / Chair of Automotive Technology
Student: **Arian Moharramzadeh**   
Supervisor: **David Ziegler**

## Usage: 
1. Specify Input-Data: network structure as .csv and user trips/demand as .json 
2. Open executeModel.py and provide relative input paths in lines 20 and 32 <br>
   Determine possible origin and destination nodes in lines 37 to 38  
3. Run executeModel.py to start equilibration 
4. Inspect documented equilibrium results in "Output- Equilibrium Results"  

