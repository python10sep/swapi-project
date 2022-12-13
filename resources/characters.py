from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Characters(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people"  # plural
        self.__character_range = [1, 82]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def character_range(self):
        return self.__character_range

    @character_range.setter
    def character_range(self, new_range_):
        self.__character_range = new_range_

    def get_count(self):
        plural_character_url = self.home_url + self.relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self, resource):
        return self.home_url + self.relative_url

    def get_sample_data(self):
        complete_url = self.home_url + self.__relative_url + "/1"
        response = hit_url(complete_url)
        data = response.json()
        return data
