#TODO 

[x] Enable package installation

[x] Create a main entry-point for the daemon

[x] Automate version management

[x] Create container class with sensors

[x] Automate API generation/mapping based on the Open API generator implementation from the backend

[ ] Add actuator code that turns on/off a relay (more complex interactions not to be solved right now)

[ ] Create `class` => `Sensor` mappings on the DB and use these to load the correct sensors, the results are currently available in the `get_chamber` API call

[ ] Use the list of API `Sensor` to instantiate the Chamber sensor objects

[ ] Send measurements from sensors to the databases once per minute

[ ] Read the expected measurements from the database and actuators that modify the "unit"

[ ] Set actuator on/off depending on being inside or outside the range based on the direction of the expected change

