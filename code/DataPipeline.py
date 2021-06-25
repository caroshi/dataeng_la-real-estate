## Importing packages, API

import pandas as pd
import numpy as np

import time

import quandl

quandl.ApiConfig.api_key = "xxx"

## Lists of LA Zips by Region

san_gabriel_valley = ['90601', '90602', '90603', '90605', '90631', '91006', '91007', '91008', '91010', '91016',\
                      '91024', '91030', '91108', '91702', '91706', '91722', '91723', '91724', '91731', '91732',\
                      '91733', '91741', '91744', '91745', '91746', '91748', '91754', '91756', '91765', '91770',\
                      '91773', '91775', '91776', '91780', '91789', '91790','91791', '91792', '91801', '91803',\
                      '92821', '92823']

central_la = ['90004', '90005', '90006', '90012', '90013', '90014', '90015', '90017', '90019', '90021', '90026',\
              '90027', '90028', '90035', '90036', '90038', '90039', '90046', '90048', '90057', '90068', '90069',\
              '90071']

east_la = ['90022', '90023', '90031', '90032', '90033', '90063']

west_la = ['90024', '90025', '90034', '90035', '90049', '90056', '90064', '90066', '90067', '90073', '90077',\
           '90094', '90210', '90212', '90230', '90232', '90272', '90291', '90292', '90401', '90402', '90403',\
           '90404', '90405', '90265', '90290', '91301', '91302', '91361', '91362']

south_bay = ['90045', '90245', '90249', '90250', '90254', '90260', '90261', '90266', '90274', '90275', '90277',\
             '90278', '90293', '90301', '90302', '90303', '90304', '90501', '90503', '90504', '90505', '90506',\
             '90717', '90220', '90221', '90502', '90710', '90712', '90713', '90715', '90716', '90731', '90732',\
             '90744', '90745', '90746', '90755', '90802', '90803', '90804', '90805', '90806', '90807', '90808',\
             '90810', '90813', '90814', '90815', '90822', '90831', '90840']

south_la = ['90001', '90002', '90003', '90007', '90008', '90011', '90016', '90018', '90037', '90043', '90044',\
            '90047', '90059', '90061', '90062', '90089', '90220', '90305', '90040', '90058', '90201', '90220',\
            '90221', '90240', '90241', '90242', '90255', '90262', '90270', '90280', '90604', '90605', '90606',\
            '90638', '90640', '90650', '90660', '90670', '90703', '90706', '90723']

the_valley = ['91040', '91304', '91306', '91307', '91311', '91316', '91324', '91325', '91326', '91330', '91331',\
              '91335', '91340', '91342', '91343', '91344', '91345', '91352', '91356', '91364', '91367', '91401',\
              '91402', '91403', '91405', '91406', '91411', '91423', '91436', '91501', '91502', '91504', '91505',\
              '91506', '91522', '91523', '91601', '91602', '91604', '91605', '91606', '91608', '91011', '91040',\
              '91042', '91101', '91103', '91104', '91105', '91106', '91107', '91201', '91202', '91203', '91204',\
              '91205', '91206', '91207', '91208', '91210', '91214']

columns_list = ['Date', 'Sales_Count','%_Home_Increasing', '%_Home_Decreasing', 'Price_to_Rent_Ratio', 
               'Median_Rental_Studio', 'Median_Rental_1B', 'Median_Rental_2B', 'Median_Rental_3B', 
               'Median_Rental_DupTrip', 'Median_Rental_SingleFam', 'Median_Listing_2B', 'Median_Listing_3B', 
               'Median_Listing_5B+', 'Median_Listing_DupTrip', 'Median_Listing_SingleFam', 
               'Median_Sold_Condo', 'Median_Sold_SingleFam', 'Home_Value_1B', 'Home_Value_2B', 
               'Home_Value_3B', 'Home_Value_4B', 'Home_Value_5B+', 'Home_Value_DupTrip', 'Home_Value_SingleFam', 
               'Zip_Code'
               ]

## Grabbing West LA Data -> CSV

for zipcode in west_la:
    west_la_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    west_la_list.append(test_df)
    

west_la_df = pd.DataFrame(np.vstack(west_la_list), columns = columns_list)

west_la_df.set_index('Zip_Code', inplace=True)

west_la_df.to_csv('westla.csv')

## Central LA Data

for zipcode in central_la:
    central_la_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    central_la_list.append(test_df)
    

central_la_df = pd.DataFrame(np.vstack(central_la_list), columns = columns_list)

central_la_df.set_index('Zip_Code', inplace=True)

central_la_df.to_csv('centralla.csv')

## South LA Data

for zipcode in south_la:
    south_la_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    south_la_list.append(test_df)
    

south_la_df = pd.DataFrame(np.vstack(south_la_list), columns = columns_list)

south_la_df.set_index('Zip_Code', inplace=True)

south_la_df.to_csv('southla.csv')

## South Bay Data

for zipcode in south_bay:
    south_bay_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    south_bay_list.append(test_df)
    

south_bay_df = pd.DataFrame(np.vstack(south_bay_list), columns = columns_list)

south_bay_df.set_index('Zip_Code', inplace=True)

south_bay_df.to_csv('southbay.csv')

## East LA Data

for zipcode in east_la:
    east_la_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    east_la_list.append(test_df)
    

east_la_df = pd.DataFrame(np.vstack(east_la_list), columns = columns_list)

east_la_df.set_index('Zip_Code', inplace=True)

east_la_df.to_csv('eastla.csv')

## The Valley Data

for zipcode in the_valley:
    the_valley_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    the_valley_list.append(test_df)
    

the_valley_df = pd.DataFrame(np.vstack(the_valley_list), columns = columns_list)

the_valley_df.set_index('Zip_Code', inplace=True)

the_valley_df.to_csv('thevalley.csv')

## San Gabriel Valley Data

for zipcode in san_gabriel_valley:
    san_gabriel_valley_list = []
    test_df = pd.DataFrame()
    
    try:
        trying_api = quandl.get('ZILLOW/Z{}_SC'.format(zipcode))
        test_df = trying_api
    except:
        pass
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHIVAH'.format(zipcode))
        test_df['%_Home_Increasing'] = next_api 
    except:
        test_df['%_Home_Increasing'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_PHDVAH'.format(zipcode))
        test_df['%_Home_Decreasing'] = next_api
    except:
        test_df['%_Home_Decreasing'] = np.nan    

    try:
        next_api = quandl.get('ZILLOW/Z{}_PRRAH'.format(zipcode))
        test_df['Price_to_Rent_Ratio'] = next_api
    except:
        test_df['Price_to_Rent_Ratio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFST'.format(zipcode))
        test_df['Median_Rental_Studio'] = next_api
    except:
        test_df['Median_Rental_Studio'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF1B'.format(zipcode))
        test_df['Median_Rental_1B'] = next_api
    except:
        test_df['Median_Rental_1B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF2B'.format(zipcode))
        test_df['Median_Rental_2B'] = next_api
    except:
        test_df['Median_Rental_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPF3B'.format(zipcode))
        test_df['Median_Rental_3B'] = next_api
    except:
        test_df['Median_Rental_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFDT'.format(zipcode))
        test_df['Median_Rental_DupTrip'] = next_api
    except:
        test_df['Median_Rental_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MRPFSF'.format(zipcode))
        test_df['Median_Rental_SingleFam'] = next_api
    except:
        test_df['Median_Rental_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF2B'.format(zipcode))
        test_df['Median_Listing_2B'] = next_api
    except:
        test_df['Median_Listing_2B'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF3B'.format(zipcode))
        test_df['Median_Listing_3B'] = next_api
    except:
        test_df['Median_Listing_3B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPF5B'.format(zipcode))
        test_df['Median_Listing_5B+'] = next_api
    except:
        test_df['Median_Listing_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFDT'.format(zipcode))
        test_df['Median_Listing_DupTrip'] = next_api
    except:
        test_df['Median_Listing_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_MLPFSF'.format(zipcode))
        test_df['Median_Listing_SingleFam'] = next_api
    except:
        test_df['Median_Listing_SingleFam'] = np.nan
        
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFCO'.format(zipcode))
        test_df['Median_Sold_Condo'] = next_api
    except:
        test_df['Median_Sold_Condo'] = np.nan
          
    try:
        next_api = quandl.get('ZILLOW/Z{}_MSPFSF'.format(zipcode))
        test_df['Median_Sold_SingleFam'] = next_api
    except:
        test_df['Median_Sold_SingleFam'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI1B'.format(zipcode))
        test_df['Home_Value_1B'] = next_api
    except:
        test_df['Home_Value_1B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI2B'.format(zipcode))
        test_df['Home_Value_2B'] = next_api
    except:
        test_df['Home_Value_2B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI3B'.format(zipcode))
        test_df['Home_Value_3B'] = next_api
    except:
        test_df['Home_Value_3B'] = np.nan    
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI4B'.format(zipcode))
        test_df['Home_Value_4B'] = next_api
    except:
        test_df['Home_Value_4B'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVI5B'.format(zipcode))
        test_df['Home_Value_5B+'] = next_api
    except:
        test_df['Home_Value_5B+'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVICO'.format(zipcode))
        test_df['Home_Value_DupTrip'] = next_api
    except:
        test_df['Home_Value_DupTrip'] = np.nan
    
    try:
        next_api = quandl.get('ZILLOW/Z{}_ZHVISF'.format(zipcode))
        test_df['Home_Value_SingleFam'] = next_api
    except:
        test_df['Home_Value_SingleFam'] = np.nan
        
    test_df['zipcode'] = zipcode
    
    test_df.reset_index(inplace=True)
    
    san_gabriel_valley_list.append(test_df)
    

san_gabriel_valley_df = pd.DataFrame(np.vstack(san_gabriel_valley_list), columns = columns_list)

san_gabriel_valley_df.set_index('Zip_Code', inplace=True)

san_gabriel_valley_df.to_csv('sangabrielvalley.csv')