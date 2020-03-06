class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """

        self.orbits = []
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', 'No name found')
        self.diameter_min_km = float(kwargs.get('estimated_diameter_min_kilometers', 0))
        self.is_potentially_hazardous_asteroid = kwargs.get('is_potentially_hazardous_asteroid', False)

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        self.orbits.append(orbit)

    def __repr__(self):
        return f'NearEarthObject id:{self.id} name:{self.name} \
                                    orbits: {[orbit.neo_name for orbit in self.orbits]} \
                                    orbit_dates:{[orbit.close_approach_date for orbit in self.orbits]}'


class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """

        self.neo_name = kwargs.get('name', 'no name')
        self.miss_distance_kilometers = float(kwargs.get('miss_distance_kilometers', 0))
        self.close_approach_date = kwargs.get('close_approach_date', None)

    def __repr__(self):
        return f'OrbitPath name:{self.neo_name} orbit_date:{self.close_approach_date} \
                                miss_distance_km:{self.miss_distance_kilometers}'
