#!/bin/bash

set -e

for file in /sql/*; do
    psql -U aalonso -d database_pizza -f "$file"
done