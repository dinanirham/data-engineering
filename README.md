## Question 1
```
docker run -it --entrypoint=bash python:3.12.8
pip list
```
### Question 2
```
docker run -it \
 -e POSTGRES_USER='root' \
 -e POSTGRES_PASSWORD='root' \
 -e POSTGRES_DB='ny_taxi_pgdata' \
 -p 5433:5432 \
 -v c:/Users/Irham/Documents/2025/data-engineering/data-engineering-zoomcamp/cohort/01-docker-terraform/pgdata_zoomcamp:/var/lib/postgresql/data \
 postgres:17-alpine
```

### Question 3
```
select 
    count(*) filter (where trip_distance <= 1) as answ1
    , count(*) filter (where trip_distance > 1 and trip_distance <= 3) as answ2
    , count(*) filter (where trip_distance > 3 and trip_distance <= 7) as answ3
    , count(*) filter (where trip_distance > 7 and trip_distance <= 10) as answ4
    , count(*) filter (where trip_distance > 10) as answ5
from green_tripdata
where lpep_pickup_datetime >= '2019-10-01'
      and lpep_dropoff_datetime < '2019-11-01';
```

### Question 4
```
select 
    lpep_pickup_datetime::date
    , max(trip_distance) longest_trip
from green_tripdata
group by lpep_pickup_datetime::date
order by longest_trip desc;
```

### Question 5
```
select 
    taxi_zone."Zone",
    sum(total_amount) total_amount,
    count(*) frq
from green_tripdata
left join taxi_zone on green_tripdata."PULocationID" = taxi_zone."LocationID"
where lpep_pickup_datetime::date = '2019-10-18'
group by taxi_zone."Zone"
having sum(total_amount) > 13000
order by frq desc
limit 3;
```

### Question 6
```
select
    tz2."Zone"
    , tip_amount
from green_tripdata as gt
left join taxi_zone as tz1 on gt."PULocationID" = tz1."LocationID"
left join taxi_zone as tz2 on gt."DOLocationID" = tz2."LocationID"
where date_part('month', lpep_pickup_datetime) = 10
      and tz1."Zone" = 'East Harlem North'
order by tip_amount desc
limit 1;
-- if the question means to get highest single tip 
-- which was pick up zone from 'East Harlem North' on October
```