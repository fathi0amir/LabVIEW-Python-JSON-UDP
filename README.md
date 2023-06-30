# Fast Bidirectional Data Communication Between LabVIEW and Python

In a (previous post)[https://github.com/fathi0amir/LV_Py_UDP] I have 
put together a demo to pass data between LabVIEW and Python through 
UDP socket. However it was limited to passing variables values on 
type double. On the each receiving ends the user need know the 
index of the disired variable. Additionally, if a user pass different 
datatype, then it is inportant to know the byte size to read as well. 

The more standard approach wrould be to serialized the data on the 
sending side as an JSON object. Python and LabVIEW both are natively 
capable to deserilize this object type. The data can be labeled there 
on the receiving end, the user can fetch the desired data by calling its 
label. In Addition, JSON object can be a mix of various data type. I put 
together another demo that can simply show case this approach. 
