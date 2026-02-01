# Solutions for HW2

## Q1

Check output of command

```
wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-12.csv.gz | gunzip > yellow_tripdata_2020-12.csv
```

### Q3

Run backfill execution of `flows/gcp_taxi_scheduled.yaml` in kestra between January 1st, 2020 and January 1st, 2021:

In `BQ` run the following query

```
SELECT COUNT(1) FROM
 gcp_project_id.zoomcamp.yellow_tripdata` ;

 ```

### Q4

Run backfill execution of `flows/gcp_taxi_scheduled.yaml` in kestra between January 1st, 2020 and January 1st, 2021.

In `BQ` run the following query

```
 SELECT COUNT(1) FROM
 `gcp_project_id.zoomcamp.green_tripdata` 
```

### Q5 

Run manual flow with year=2021 and month=03 of `flows/gcp_taxi_manual.yaml`

In `BQ` run the following query

```
SELECT COUNT(1) FROM
 `gcp_project_id.zoomcamp.yellow_tripdata` 
WHERE filename='yellow_tripdata_2021-03.csv'
``