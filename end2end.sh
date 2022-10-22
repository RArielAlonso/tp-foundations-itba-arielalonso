docker-compose down

echo "-------------------------------------------"
echo "Restarting the container of the database"
echo "-------------------------------------------"

docker-compose up -d


echo "-------------------------------------------"
echo "Removing and creating the database"
echo "-------------------------------------------"

docker exec postgres-db bash /usr/local/bin/data_tables.sh

echo "-------------------------------------------"
echo "Extracting and loading the data to postgres"
echo "-------------------------------------------"

docker run -t ETL-container -f ETL/Dockerfile .
docker run --rm --network nt-pizza -v $PWD/ETL/csv_files:/csv_files ETL-container

echo "-------------------------------------------"
echo "Generating the reports"
echo "-------------------------------------------"

docker run -t report-image -f Reports/Dockerfile .
docker run --rm --network nt-pizza -v $PWD/Reports/graphs:/graphs report-image


read -p "Want to END the connection to postgres Database? \n Type yes (it is case sensitive) " confirmation
if [ "$confirmation" = "yes" ]
then
    docker-compose down
    echo "-------------------------------------------"
    echo "PROCESS END - DATABASE IS OFF"
    echo "-------------------------------------------"
else
    echo "-------------------------------------------"
    echo "PROCESS END - DATABASE IS ON"
    echo "-------------------------------------------"
fi

echo "-------------------------------------------"
echo "PROCESS ENDED SUCCESFULLY"
echo "-------------------------------------------"
