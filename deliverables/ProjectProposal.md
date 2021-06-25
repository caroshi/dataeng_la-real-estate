# Data Engineering Project Proposal

## Question: 
I would like to explore real estate data -- particularly if one is better off renting or buying in a particular zip code or neighborhood. Data allowing, I would like to filter out and look at different types of real estate as well: single family homes with varying # of bedrooms, condos, and apartments. For initial EDA, I plan on plotting out and visualizing the change of rental and home sale prices over time. Ideally, I would like to build an application that allows you to input zip code, type of housing, # of bedrooms and bathrooms and outputs "Rent or Buy!" Ideally, the app also incorporates a model that forecasts what your rent will be or what your house will cost in the future, but I am not sure my data will include enough features to build a robust model. For this project, I will focus on Los Angeles, looking at 100-200 zip codes in the county as needed for the data requirement. 

## Data: 
Quandl has an API that allows you to call a variety of Zillow-based datasets. I was hoping for access to specific sales history per zip code but it seems that Zillow makes that information difficult/impossible to grab. Quandl divides each zip code into a wide variety of sets ranging from: Sales Counts, Median Sold Price by Square Foot, Median Listing Price by Square Foot, Median Rental Price per Square Foot, Count of Monthly Listings, % of homes Increasing and Decreasing in value. The date range of each dataset ranges from 10+ years to 1 year -- I hope to grab at least 2-3 years of real estate data. 

In addition, I will look further into Zillow's API. 

## Tools:
* MongoDB/SQLite for data storage, EDA pending output of my data
* Numpy, Pandas for processing data, EDA
* Matplotlib, Tableau for visualization
* Google Cloud for data storage, cloud computing

## MVP:
I plan to have all my data cleaned, EDA and basic data visualizations completed, and the beginnings of my app started by EOD Tuesday. 