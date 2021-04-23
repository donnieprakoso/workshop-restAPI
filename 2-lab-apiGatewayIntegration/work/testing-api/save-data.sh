#!/bin/bash
curl -vX POST https://your-api-endpoint/prod/data -d @save-data.json --header "Content-Type: application/json"