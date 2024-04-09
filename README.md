# Movie Dashboard Using Tableau

* To view the dashboards:
	- [Dashboard #1: Revenue by Quantitative Metrics](https://public.tableau.com/app/profile/tanner.amundsen/viz/AmundsenEN_605_662FinalProject-Dashboard1/Revenuevs_QuantitativeMeasurement)
	- [Dashboard #2: Revenue by Keywords and Cast](https://public.tableau.com/app/profile/tanner.amundsen/viz/AmundsenEN_605_662FinalProject-Dashboard2/RevenuebyActorandKeyword)
	- [Dashboard #3: Revenue by Categorical Data](https://public.tableau.com/app/profile/tanner.amundsen/viz/AmundsenEN_605_662FinalProject-Dashboard3/Revenuevs_CategoricalMetrics)
* To view the dashboard in Tableau workbook form
	- Open the “Final Project Workbook.twbx” file in the root directory of the submission folder
* To build data source from scratch
	1. Navigate to the root directory of the submission file and ensure you have the folder “movies” with the following two files in it:
		- tmdb_5000_movies.csv
		- tmdb_5000_credits.csv
	2. Run python3 process_movie_data.py
	3. Import the newly created .csv files (_modified) into the flow.tfl file located in the root directory
	4. Run the flow in Tableau Prep Builder
	5. Ensure the .hyper files have been loaded into the “prep” folder


