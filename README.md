# openweathermap
Examples using open weather map API

Usage:

get-wxdata.sh:
    This script uses curl to call the openweathermap service for the Paris Maine location. The
    output is piped to jq to parse the JSON data that is returned.

get-weather-data-json.py:
    This Python script performs the same operations as get-wxdata.sh. The openweathermap API key
    must be given as a command line arguement. The latitude/longitude for Paris Maine is hardcoded.
    This can eaily be extended to allow a different location to be queried.

 
