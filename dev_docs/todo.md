#TODO 

[ ] Create container class with sensors
[ ] Add actuator code that turns on/off a relay (more complex interactions not to be solved right now)
[ ] Make a file with the hash mappings between the classes and the IDs of sensors and units in the DB
[ ] Automate API generation/mapping based on the Open API generator implementation from the backend
[ ] Container class should read from teh dataabase which are the expected snesors (use list above to build them)
[ ] Send messurments from sensors to the databaases once per minute
[ ] Read the expected messurments from the database and actuators that modify the "unit"
[ ] Set actuator on/off depending on being inside or outside the range based on the direction of the expected chanve

