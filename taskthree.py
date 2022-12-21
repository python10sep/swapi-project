"""
# 1. TODO import all resource classes here
# 2. TODO get count of each resource
# 3. TODO get "singular" resource urls of each resource
# 4. TODO pull data from random 3 "singular" resource URLs
# 5. TODO convert swapi project into CLI application
      # task1 task2 task3

"""

import requests

# pydantic models
from models.datamodels.characters import Character_
from models.datamodels.films import Film_
from models.datamodels.planets import Planet_
from models.datamodels.spacies import Species_
from models.datamodels.starships import Starship_
from models.datamodels.vehicles import Vehicle_

# resource-classes
from resources.planets import Planet
from resources.films import Film
from resources.characters import Characters
from resources.vehicles import Vehicle
from resources.species import Species
from resources.spaceships import Spaceship

if __name__ == "__main__":

    planet_data = Planet().get_sample_data()
    planet_data = Planet_(**planet_data)

    film_data = Film().get_sample_data()
    film_data = Film_(**film_data)

    vehicle_data = Vehicle().get_sample_data()
    vehicle_data = Vehicle_(**vehicle_data)

    spaceship_data = Spaceship().get_sample_data()
    spaceship_data = Starship_(**spaceship_data)

    character_data = Characters().get_sample_data()
    character_data = Character_(**character_data)

    species_data = Species().get_sample_data()
    species_data = Species_.get_sample_data()
