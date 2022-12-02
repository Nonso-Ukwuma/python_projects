#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    import pandas as pd
    flight = pd.read_csv('flights.csv')
    airport = pd.read_csv('airports.csv')
    flight = flight[flight['ORIGIN_AIRPORT'].isin(airport.IATA_CODE)]
    flight = flight[flight['DESTINATION_AIRPORT'].isin(airport.IATA_CODE)]
    
    busiest_airport = busy_airport(flight, airport)
    print(f'(No.1) The Busiest airport in the US = {busiest_airport}\n')
    
    cancel, security, weather = cancel_delay(flight, airport)
    print(f'(No.2a) The airport where you are most likely to experience flight delay due to Weather = {weather}\n')
    print(f'(No.2b) The airport where you are most likely to experience flight delay due to Security = {security}\n')
    print(f'(No.2c) The airport where you are most likely to experience flight Cancellation = {cancel}\n')

    prob_flight = flight_prob(flight)
    print(f'(No.3) The probability that any jet is flying versus on the ground at any moment in time during the year  = {prob_flight:.2f}\n')

    active_flgt, avg_alt = flight_info()
    print(f' (No. 4a) The number of flights currently in the air = {active_flgt}\n')
    print(f' (No. 4b) The average altitude of all flights currently in the air = {avg_alt:.2f}\n')


# In[2]:


def read_data():
    flight = pd.read_csv('flights.csv')
    airport = pd.read_csv('airports.csv')
    flight = flight[flight['ORIGIN_AIRPORT'].isin(airport.IATA_CODE)]
    flight = flight[flight['DESTINATION_AIRPORT'].isin(airport.IATA_CODE)]
    
    return flight, airport


# In[3]:


def busy_airport(flight, airport):
    busy = flight[['ORIGIN_AIRPORT' ,'DESTINATION_AIRPORT', 'DEPARTURE_TIME', 'ARRIVAL_TIME']].groupby(['ORIGIN_AIRPORT']).count().sort_values(by='DEPARTURE_TIME', ascending=False).reset_index()
    b_airport = airport.AIRPORT[airport['IATA_CODE'] == busy.ORIGIN_AIRPORT[0]].to_list()
    return b_airport[0]


# In[8]:


def cancel_delay(flight, airport):
    flw = flight[flight['WEATHER_DELAY'] != 0.0]
    fls = flight[flight['SECURITY_DELAY'] != 0.0]
    flc = flight[flight['CANCELLED'] != 0.0]
    cancelled = flc[['ORIGIN_AIRPORT', 'CANCELLED']].groupby('ORIGIN_AIRPORT').sum().sort_values(by='CANCELLED', ascending=False).reset_index()
    sec_delay = fls[['ORIGIN_AIRPORT', 'SECURITY_DELAY']].groupby('ORIGIN_AIRPORT').sum().sort_values(by='SECURITY_DELAY', ascending=False).reset_index()
    weath_delay = flw[['ORIGIN_AIRPORT', 'WEATHER_DELAY']].groupby('ORIGIN_AIRPORT').sum().sort_values(by='WEATHER_DELAY', ascending=False).reset_index()
    canc_f = airport.AIRPORT[airport['IATA_CODE'] == cancelled.ORIGIN_AIRPORT[0]].to_list()
    secur_del = airport.AIRPORT[airport['IATA_CODE'] == sec_delay.ORIGIN_AIRPORT[0]].to_list()
    weather_del = airport.AIRPORT[airport['IATA_CODE'] == weath_delay.ORIGIN_AIRPORT[0]].to_list()
    return canc_f[0], secur_del[0], weather_del[0]


# In[5]:


def flight_prob(flight):
    ftime = flight.AIR_TIME.sum()
    min_per_year = 525600
    num_flights = flight.FLIGHT_NUMBER.nunique()
    prob_fl = ((ftime/num_flights)/min_per_year) * 100
    return prob_fl


# In[6]:


def flight_info():
    from flightradar24.api import FlightRadar24API
    fr_api = FlightRadar24API()
    airflights = fr_api.get_flights()
    current_flights = []
    for airflight in airflights:
        if airflight.altitude > 0:
            current_flights.append(airflight.altitude)
        #print(airflight.altitude)
    num_active_flights = len(current_flights)
    avg_altitude = sum(current_flights)/num_active_flights
    
    return num_active_flights, avg_altitude


# In[9]:


main()


# In[ ]:




