import csv
from models import OrbitPath, NearEarthObject


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """

        self.filename = filename
        self.neo_name = {}
        self.neo_date = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        neo_data_file = open(filename, 'r')
        neo_data = csv.DictReader(neo_data_file)
        for neo_row_data in neo_data:
            orbit_path = OrbitPath(**neo_row_data)
            if not self.neo_name.get(neo_row_data['name'], None):
                self.neo_name[neo_row_data['name']] = NearEarthObject(**neo_row_data)

            near_earth_object = self.neo_name.get(neo_row_data['name'], None)
            near_earth_object.update_orbits(orbit_path)

            if not self.neo_date.get(neo_row_data['close_approach_date'], None):
                self.neo_date[neo_row_data['close_approach_date']] = []

            self.neo_date[neo_row_data['close_approach_date']].append(near_earth_object)

        return None
