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

```
select 
    lpep_pickup_datetime::date
    , max(trip_distance) longest_trip
from green_tripdata
group by lpep_pickup_datetime::date
order by longest_trip desc;
```

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