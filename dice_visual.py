from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
# create two D6 dice
die_1 = Die()
die_2=Die()

#make some rolls and store the results in a list.
#results=[]
#for roll_num in range(100_000):
#    result=die_1.roll() * die_2.roll()
#    results.append(result)

results=[die_1.roll() + die_2.roll() for num in range(100_000)]

#Analyze results
frequencies=[]
max_result=die_1.num_sides + die_2.num_sides 
for value in range(2, max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values=list(range(2,max_result+1))
data=[Bar(x=x_values, y=frequencies)]
x_axis_config={'title':'Result','dtick':1}
y_axis_config={'title':'Frequency of results'}
my_layout=Layout(title='Results of rolling two D6, 100 000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout},filename='d6_d6.html')
