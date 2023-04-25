#!/bin/bash

export HOST=localhost
export BBUY_DATA=~/search_engineering/datasets/product_data/products # Set this to where your data lives

echo -d "Delete Index?: "
read VAR

if [[ $VAR == 'Y' ]]
then 
    curl -k -X DELETE -u admin:admin https://localhost:9200/bbuy_products
fi

curl -k -X PUT -u admin:admin "https://$HOST:9200/bbuy_products" -H 'Content-Type: application/json' -d "/home/elastic/search_engineering/week1/bbuy_products.json"