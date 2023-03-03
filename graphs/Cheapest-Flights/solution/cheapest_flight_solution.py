import heapq
from typing import List
from collections import defaultdict

def cheapest_flight(cities: int, flights: List[List[str]], source: str, dest: str, max_layovers: int) -> int:
    # Convert flights to an adjacency dictionary
        # adj_dict = defaultdict(list)
    # adj_dict = defaultdict(list)
    adj_dict = {}
        # visited = defaultdict(bool)
    visited = defaultdict(bool)
    # turn the list of edges into an adjacency dictionary
    # iterate through the list of flights
    for departure_city, arrival_city, flight_cost in flights:
        # the key departure city
        # value will be a list of tuples 
            # first elemnt = cost of the flight
            # second element = arrival city
        adj_dict[departure_city].append((flight_cost, arrival_city))
        # set visited to False for all keys
        visited[departure_city] = False


    # Find the shortest path (within layover limit)
    # Initialize a priority queue
    pq = []
    #Add the first element to the queue
    # first element is cost to get from source city to destination city
    # how many layovers can we still use? 
    # 3rd element: arrival city
    heapq.heappush(pq, (0, max_layovers + 1, source))

    # while there are still elements in the priority queue:
    while pq:
        # Pop the cheapest city off the queue
        current_price, layovers_left, current_city = heapq.heappop(pq)
        #if the city we are visiting is the destination city
        if current_city == dest:
            #return to the current price to get to that city
            return current_price
        # Add the city to our visited dictionary
        visited[current_city] = True

        # If we are able to add another flight:
        if layovers_left > 0:
            #Loop through the connecting flights from our current city
            for cost_to_neighbor, neighbor in adj_dict[current_city]:
            #aka loop through the node's neighbors
                # If we have not yet been to that city
                if not visited[neighbor]:
                # Add the city to the heap/priority queue
                    #price current price + cost to get to neighbor city
                    # decrease layovers by one
                    # neighbor/arrival city 
                    heapq.heappush(pq, (current_price + cost_to_neighbor, layovers_left - 1, neighbor))
    return -1