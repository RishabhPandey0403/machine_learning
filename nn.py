import keras
l0 = keras.layers.Dense(units=1, input_shape=[1])
"""
units=1 — This specifies the number of neurons in the layer. 
The number of neurons defines how many internal variables the layer has to try to 
learn how to solve the problem (more later). Since this is the final layer, 
it is also the size of the model's output — a single float value representing 
degrees Fahrenheit. (In a multi-layered network, the size and shape of the layer
would need to match the input_shape of the next layer.)

input_shape=[1] — This specifies that the input to this layer is a single value. 
That is, the shape is a one-dimensional array with one member. Since this is the 
first (and only) layer, that input shape is the input shape of the entire model. 
The single value is a floating point number, representing degrees Celsius.
"""