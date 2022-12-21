"""

TODO

1. pull data for the movie "A New Hope" and save in DB

2. Replace the data for each of the endpoint listed in the JSON object
 and insert that data into respective database tables
 (using following instructions)

    (For example - "A New Hope" has following resource endpoints)
        - characters
        - planets
        - vehicles
        - starships
        - species

3. Convert height and weight in each character to standard units

4. You have to remove all cross-referencing URLs from each resource

"""

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

from dal.db_conn_helper import insert_resource


if __name__ == "__main__":

    film_data = Film().get_sample_data(id_=1)
    film_data = Film_(**film_data)

    film_columns = ["title", "opening_crawl",
                    "director", "producer", "release_date", "created", "edited",
                    "url"]

    film_values = [film_data.title,
                   film_data.opening_crawl, film_data.director,
                   film_data.producer, film_data.release_date,
                   film_data.created.strftime("YYYY-MM-DD"),
                   film_data.edited.strftime("YYYY-MM-DD"),
                   film_data.url]

    result = insert_resource(
        "film", "film_id", film_data.episode_id,
        film_columns, film_values
    )



