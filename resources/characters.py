from base import ResourceBase
from utils.fetch_data import hit_url


class Characters(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people"  # plural
        self.__character_range = [1, 82] # TODO implement setter method

    # TODO implement getter method to get and set "__character_range" from class

    def get_count(self):
        plural_character_url = self.home_url + self.relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self, resource):
        # TODO - implement this method similar to above
        pass
