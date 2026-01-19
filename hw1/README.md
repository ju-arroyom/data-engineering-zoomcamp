# Solutions for HW1

## Q1

```
docker run -it --entrypoint=bash python:3.13

pip -V

```

## Q3

```
SELECT COUNT(1)
    FROM green_taxi_data gt
    WHERE
    gt.lpep_pickup_datetime >
    '2025-11-01' AND 
    gt.lpep_pickup_datetime <= '2025-12-01'
     AND gt.trip_distance <=1
```

# Q4

```
SELECT DATE(gt.lpep_pickup_datetime) as pickup_day,
	   MAX(gt.trip_distance) as max_distance_per_day
    FROM public.green_taxi_data gt
    WHERE gt.trip_distance <=100
	GROUP BY DATE(gt.lpep_pickup_datetime)
	ORDER BY max_distance_per_day DESC
	LIMIT 1

```

# Q5

```

SELECT 
	DATE(gt.lpep_pickup_datetime) as pickup_day,
	zl."Zone",
	SUM(gt.total_amount) as total_amount
	FROM public.green_taxi_data gt
	JOIN public.zone_lookup zl
	ON gt."PULocationID"= zl."LocationID"
	WHERE DATE(gt.lpep_pickup_datetime)='2025-11-18'
	GROUP BY 1,2
	ORDER BY total_amount DESC
	LIMIT 1

```

# Q6

```
SELECT
	DATE_PART('year', gt.lpep_pickup_datetime) pickup_year,
	DATE_PART('month', gt.lpep_pickup_datetime) pickup_month,
	zl."Zone" AS pickup_zone,
	zout."Zone" AS dropoff_zone,
	MAX(tip_amount) AS max_tip
	FROM public.green_taxi_data gt
	JOIN public.zone_lookup zl
	ON gt."PULocationID"= zl."LocationID"
	JOIN public.zone_lookup zout
	ON gt."DOLocationID"= zout."LocationID"
	WHERE zl."Zone" ='East Harlem North'
	AND DATE_PART('year', gt.lpep_pickup_datetime) ='2025'
	AND DATE_PART('month', gt.lpep_pickup_datetime) ='11'
	GROUP BY 1,2,3,4
	ORDER BY max_tip DESC
	LIMIT 1;
```