#!/bin/bash
echo -n "What is the data ID (you can get it by executing list-data API)?"
read id
curl -vX GET https://your-api-endpoint/prod/data/$id