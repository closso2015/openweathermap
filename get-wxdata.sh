#!/bin/bash

# lat long are for paris maine

curl -vvv "https://api.openweathermap.org/data/3.0/onecall?lat=44.26&lon=-70.5&exclude=minutely,hourly,daily&units=imperial&appid=30c462bbbc24753219c941dee1a466aa" |jq .

# exclude sample https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}

# works and gets all the wx data
#curl -k "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid=30c462bbbc24753219c941dee1a466aa" |jq .

#../git-testing/list-files-in-commit-master.sh:curl -k --header "PRIVATE-TOKEN:XUaqMH8U8ey9Ph2RmVV2" "https://gitlab.bit9.local/api/v4/projects/${ID_STR2}/repository/commits/${SHA2}/diff?redf_name=master"

