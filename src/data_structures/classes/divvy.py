import csv
import sys
import time
import math
import datetime
import operator

class Location(object):   
    """
    Represents a geographic location
    """

    def __init__(self, latitude, longitude):
        """
        Constructor

        Parameters:
        - latitude, longitude: (float) The coordinates
          for this location.
        """
        self.latitude = latitude
        self.longitude = longitude


    def to_string(self):
        """
        Produces a string representation of the location.

        Parameters: None
        
        Returns: String representation of the location
        """
        if (self.latitude < 0.0):
            lat = "S"
        else:
            lat = "N"

        if (self.longitude < 0.0):
            lon = "W"
        else:
            lon = "E"

        return "({:.3f} {}, {:.3f} {})".format(abs(self.latitude),
                                               lat,
                                               abs(self.longitude),
                                               lon)
 

    def distance_to(self, other):
        """
        Computes the distance to another location using the
        Haversine Formula

        Parameters:
        - other: (Location object) Another location

        Returns: (float) the distance to the other location
        """
        diffLatitude = math.radians(other.latitude - self.latitude)
        diffLongitude = math.radians(other.longitude - self.longitude)

        a = math.sin(diffLatitude/2) * math.sin(diffLatitude/2) + \
            math.cos(math.radians(self.latitude)) * \
            math.cos(math.radians(other.latitude)) * \
            math.sin(diffLongitude/2) * math.sin(diffLongitude/2)
        d = 2 * math.asin(math.sqrt(a))

        return 6371000.0 * d


    def __str__(self):
        """
        Produces a string representation of the location.

        Parameters: None
        
        Returns: String representation of the location
        """
        return self.to_string()


class DivvyStation(object):
    """
    Represents a single Divvy station.

    See constructor for description of attributes.
    """

    def __init__(self, stationID, name, latitude, longitude,
                 dpcapacity, landmark, online_date):
        """
        Constructor.

        The parameters to the constructor correspond to the fields
        in the Divvy station file.

        Parameters:
        - id: (integer) A unique integer identifier.
        - name: (string) A descriptive name (e.g., "State St & Harrison St")
        - latitude: (float) Latitude of the station.
        - longitude: (float) Longitude of the station.
        - dpcapacity: (integer) The number of total docks at each station 
          as of 2/7/2014
        - landmark: (integer) An undocumented attribute
        - online_date: (string) Date the station went live in the system 
              (e.g., "6/28/2013")
        """
        self.stationID = stationID
        self.name = name
        self.location = Location(latitude, longitude)
        self.dpcapacity = dpcapacity
        self.landmark = landmark
        self.online_date = online_date


    def distance_to(self, other_station):
        '''
        Computes the distance to another station.

        Parameters:
        - other_station: (DivvyStation) Another station

        Returns: (float) distance "as the crow flies" from this
          station to other_station (in meters)
        '''
        d = self.location.distance_to(other_station.location)

        return d


class DivvyTrip(object): 
    """
    Represents a single Divvy trip.

    See constructor for description of attributes.
    """

    def __init__(self, trip_id, starttime, stoptime, bikeid,
                 tripduration, from_station, to_station, 
                 usertype, gender, birthyear):
        """
        Constructor

        The parameters to the constructor correspond to the fields
        in the Divvy trip file.

        Parameters:
        - trip_id: (integer) A unique identifier for the trip.
        - starttime, and stoptime: (string) Date and time for the start 
          and end time of the trip.
        - bikeid: (integer) A unique identifier for the bike used in this trip.
        - tripduration: (integer) The duration (in seconds) of the trip.
        - from_station_id, to_station_id: (integer) The identifiers of the 
          origin and destination stations.
        - from_station_name, to_station_name: The names of the origin and 
          destination stations.
        - usertype: This field will be either Customer or Subscriber. 
          A "customer" is a rider who purchased a 24-Hour Pass, and a 
          "subscriber" is a rider who purchased an Annual Membership.
        - gender: The gender of the rider. This field only has a value 
          when the rider is a subscriber.
        - birthday: The date of birth of the rider. This field only has a 
          value when the rider is a subscriber.
        """

        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.tripduration = tripduration
        self.from_station = from_station
        self.to_station = to_station
        self.usertype = usertype
        self.gender = gender
        self.birthyear = birthyear    
    
    def get_distance(self):
        """
        Returns the distance from the origin station to the 
        destination station
        """            
        return self.from_station.distance_to(self.to_station)
    

class DivvyData(object):
    """
    Encapsulates the entire Divvy dataset.

    A DivvyData object has three attributes:
    - stations: A dictionary mapping station IDs to DivvyStation objects
    - trips: A list of DivvyTrip objects, in the same order in which they
             appear in the trips file (sorted by trip start time)
    - bikeids: A set of bike IDs in the dataset
    """

    def __init__(self, stations_filename, trips_filename):
        """
        Constructor.

        Parameters:
        - stations_filename: (string) Path of Divvy stations file
        - trips_filename: (string) Path of Divvy trips file
        """

        self.stations = self.read_stations_file(stations_filename)
        self.trips = self.read_trips_file(trips_filename)

        self.bikeids = set()
        for t in self.trips:
            self.bikeids.add(t.bikeid)

    def read_single_station(self, row):
        """
        Create a DivvyStation object based on a line 
        from the stations CSV file

        Parameters:
        - row: (list of strings) Values in a single row of the
          stations CSV file

        Returns: DivvyStation object constructed with the values
          in the provided row.
        """

        if len(row) < 7:
            print("Error in parsing line: " + ",".join(row))
            return None

        try:
            station_id = int(row[0])
            name = row[1]

            latitude = float(row[2])
            longitude = float(row[3])

            dpcapacity = int(row[4])
            landmark = int(row[5])

            date = time.strptime(row[6], "%m/%d/%Y")
        except Exception as e:
            print("Error in parsing data: " + str(e))
            return None

        return DivvyStation(station_id, name, latitude, longitude, dpcapacity, landmark, date)


    def read_stations_file(self, filename):
        """
        Read a Divvy stations file.

        Parameters: 
        - filename: (string) Path to station file

        Returns: (dictionary: integer -> DivvyStation) A dictionary that 
          maps station identifiers to DivvyStation objects
        """
        stations = {}
        with open(filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                station = self.read_single_station(row)
                if station == None: 
                    print("Error reading station: " + ",".join(row))
                    sys.exit(0)
                else:
                    stations[station.stationID] = station

        return stations


    def read_single_trip(self, row):
        """
        Create a DivvyTrip object based on a line 
        from the trips CSV file

        Parameters:
        - row: (list of strings) Values in a single row of the
          trips CSV file

        Returns: DivvyTrip object constructed with the values
          in the provided row.
        """

        try:
            trip_id = int(row[0])

            starttime = time.strptime(row[1], "%Y-%m-%d %H:%M")
            endtime = time.strptime(row[2], "%Y-%m-%d %H:%M")

            bikeid = int(row[3])
            tripduration = int(row[4])

            station_id = int(row[5])
            if station_id not in self.stations:
                print("Encountered unknown station: " + str(station_id))
                return None
            from_station = self.stations[station_id]
            # Skip the station name (row[6]). We do not use it.

            station_id = int(row[7])
            if station_id not in self.stations:
                print("Encountered unknown station: " + str(station_id))
                return None
            to_station = self.stations[station_id]
            # Skip the station name (row[8]). We do not use it.

            usertype = row[9]
            gender = None
            birthyear = 0

            if usertype == "Subscriber":
                gender = row[10]
                if gender != "" and gender != "Male" and gender != "Female":
                    print("Encountered unknown gender: " + gender)
                    return None

                if len(row[11]) > 0:
                    birthyear = int(row[11])
        except Exception as e:
            print("Error in parsing line: " + str(e))
            return None

        return DivvyTrip(trip_id, starttime, endtime, bikeid, tripduration, from_station, to_station, usertype, gender, birthyear)


    def read_trips_file(self, filename):
        """
        Read a Divvy trips file.

        Parameters: 
        - filename: (string) Path to trips file

        Returns: (list of DivvyTrip) A list with all the trips in the file.
        """
        trips = []
        with open(filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                trip = self.read_single_trip(row)
                if trip == None: 
                    print("Error reading trip: " + ",".join(row))
                    sys.exit(0)
                else:
                    trips.append(trip)

        return trips


    def get_number_stations(self):
        """Returns the number of stations in the dataset"""
        return len(self.stations)
    

    def get_number_trips(self):
        """Returns the number of trips in the dataset"""
        return len(self.trips)
    

    def get_total_distance(self):
        """Returns the total distance of all the Divvy trips"""
        total_distance = 0.0
        for trip in self.trips:
            total_distance += trip.get_distance()
        
        return total_distance


    def get_total_duration(self):
        """Computes the total duration, in seconds, of all the Divvy trips"""
        total_duration = 0.0
        
        for trip in self.trips:
            total_duration += trip.tripduration
        
        return total_duration


def time_str(t):
    """
    Converts a time in seconds to a string representation
    in days, hours, minutes, seconds.

    Parameters:
    - t: (integer) A time in seconds

    Returns: (string) A string representation.
    """
    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    
    t = int(t)
    days = t // DAY
    hours = (t % DAY) // HOUR
    minutes = (t % HOUR) // MINUTE
    seconds = t % MINUTE

    if days == 0:
        return "{}h {}m {}s".format(hours, minutes, seconds)
    else:
        return "{}d {}h {}m {}s".format(days, hours, minutes, seconds)
    


def go(station_filename, trip_filename):
    """
    Print some statistics about the Divvy files.
    """
    data = DivvyData(station_filename, trip_filename)

    # Number of stations and trips
    print("# of stations: " + str(data.get_number_stations()))
    print("# of trips: " + str(data.get_number_trips()))

    print();
        
    # Average duration of trip
    print("The aggregate total duration of all Divvy trips in 2013 was " + 
          time_str(data.get_total_duration()))

    print("The average duration of a Divvy trip in 2013 was " + 
          time_str(data.get_total_duration() / data.get_number_trips()))

    print();

    # Total and average distance
    s ="The total distance travelled by all the Divvy bikes in 2013 was {:,.2f} kilometers."
    print(s.format(data.get_total_distance()/1000.0))

    s = "The average distance travelled in a single trip in 2013 was {:,.2f} meters."
    print(s.format(data.get_total_distance()/data.get_number_trips()))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        station_filename = sys.argv[1]
        trip_filename = sys.argv[2]
    else:
        print("usage: python {} <stationFile> <tripFile>".format(sys.argv[0]))
        sys.exit(0)

    go(station_filename, trip_filename)

