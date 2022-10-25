docker-compose down
PID=$!
wait $PID
echo "-------------------------------------------"
echo "Restarting the container of the database"
echo "-------------------------------------------"

docker-compose up -d && sleep 10
PID=$!
wait $PID

echo "-------------------------------------------"
echo "Removing and creating the database"
echo "-------------------------------------------"

docker exec postgres-db bash /usr/local/bin/data_tables.sh &
PID=$!
wait $PID

echo "-------------------------------------------"
echo "Extracting and loading the data to postgres"
echo "-------------------------------------------"

cd ETL/
docker build -t etl-container -f $PWD/Dockerfile . &
PID=$!
wait $PID
cd ..
docker run --rm --network nt-pizza -v $PWD/ETL/csv_files:/csv_files etl-container &
PID=$!
wait $PID

echo "-------------------------------------------"
echo "Generating the reports"
echo "-------------------------------------------"

cd Reports/
docker build -t report-image -f $PWD/Dockerfile . &
PID=$!
wait $PID
cd ..
docker run --rm --network nt-pizza -v $PWD/Reports/graphs:/graphs report-image &
PID=$!
wait $PID

read -p "Want to END the connection to postgres Database? Type yes (it is case sensitive) " confirmation
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


