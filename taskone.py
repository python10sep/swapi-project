"""The Star Wars API lists 82 main characters in the Star Wars saga. For the
first task, we would like you to use a random number generator that picks a
number between 1-82. Using these random numbers you will be pulling 15
characters from the API using Python."""


import requests

from utils.randgen import ProduceChars
from typing import List, Optional

from models.characters import Character

start = 1
stop = 83


def get_chars(obj_: ProduceChars) -> Optional[List[int]]:
    characters_ = []  # [1, 4, 5, 13, ....]
    for i in obj_:
        characters_.append(i)

    return characters_


if __name__ == "__main__":
    print(__name__)
    print("current module getting executed")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"  # magic string

    print(f"[ INFO ] producing random 2 characters...")
    obj = ProduceChars(start, stop)
    characters = get_chars(obj)

    print(f"[ INFO ] done - producing random 2 characters")

    output = []
    for num_ in characters:  # [1, 2]
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        char_ = Character(**response)
        char_.films
        char_.height

        print("######" * 25)
