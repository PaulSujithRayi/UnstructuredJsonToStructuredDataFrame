# we are importing the python json package that has functions to handle json formatted data
import json

# we are importing url.lib to extract JSON data through a url
import urllib.request

# i am storing my JSON url data in a variable
nyc_demographic_url = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD"

#i am using the urlopen function as part of the the urllib.request package and storing the opened url in a variable
response = urllib.request.urlopen(nyc_demographic_url)
#i am printing the data type of the varibale on the screen
print(type(response))
# as you can see on the console our url type is http.client.HTTPRepsonse which is what we have to expect

# we are printing a new line for readability sake
print('\n')

# we are parsing and decoding our json url stored in the response variable using the read and decode functions
json_string = response.read().decode('utf-8')
#now we are printing the first 500 lines of the decoded and parsed output
print(json_string[:500])

# we are printing a new line for readability sake
print('\n')

#now we use the json package to transform the string into python data structures consisting of lists and dictionaries
nycdem_parsed_json = json.loads(json_string)

# the outermost level is a dictionary 
print(type(nycdem_parsed_json))
# as you can see on the console the type of our variable is a dictionary

# we are printing a new line for readability sake
print('\n')

#let us look at the keys for a moment now
print(nycdem_parsed_json.keys())
# as you can see on the console the keys are meta and data

# we are printing a new line for readability sake
print('\n')

# now let us see what meta contains
print(nycdem_parsed_json['meta'])
# as you can see on the console. It is a mixture of dictionaries and lists

# we are printing a new line for readability sake
print('\n')

#now let us also see what data contains
print(nycdem_parsed_json['data'])
# as you can see on the console it is a list of lists

# we are printing a new line for readability sake
print('\n')

# now lets dig a little deeper and look at the keys inside meta
print(nycdem_parsed_json['meta'].keys())
# as you can see on the console there is one key inside meta which is called view 

# we are printing a new line for readability sake
print('\n')

#now the demographic data is in lists under data
# i got to know this by looking at the metadata in the website from where I extracted my json file
demlist = nycdem_parsed_json['data']

#now let us look at the length of the lists in our newly created list variable demlists
print(len(demlist))

# we are printing a new line for readability sake
print('\n')

#now let us look at the lists which contain our demographic data stored in our variable
print(demlist)
#as you can see on the console it is a list of lists

# we are printing a new line for readability sake
print('\n')

# we will be importing pandas package which will help us do our data analysis using dataframes
import pandas as pd

# now let us convert this list of lists into a dataframe on which we can do our analysis
# here each list will be one observation/row
nycdem_df = pd.DataFrame(demlist)

#now let us look at our dataframe
print(nycdem_df)
#awesome! as you can see in the console, the dataframe is displayed

# we are printing a new line for readability sake
print('\n')

#now we do not need some columns from our dataframe and we will be removing those columns
# i got to know this by looking at the metadata in the website from where I extracted my json file
# and these columns are 0 - 7
nycdem_df1 = nycdem_df.drop([0,1,2,3,4,5,6,7], axis = 1)

# now let us look at our new dataframe with our necessary columns
print(nycdem_df1)
#awesome! the dataframe looks beatiful on the console

# we are printing a new line for readability sake
print('\n')

# now let us rename the columns of the dataframe 
# i got to know the names of columns by looking at the metadata in the website from where I extracted my json file
nycdem_df1.columns = ['jurisdiction name', 'count participants', 'count female', 'percent female', 'count male',
'percent male', 'count gender unknown', 'percent gender unknown', 'count gender total', 'percent gender total',
'count pacific islander', 'percent pacific islander', 'count hispanic latino', 'percent hispanic latino',
'count american indian', 'percent american indian', 'count asian non hispanic', 'percent asian non hispanic',
'count white non hispanic', 'percent white non hispanic', 'count black non hispanic', 'percent black non hispanic',
'count other ethnicity', 'percent other ethnicity', 'count ethnicity unknown', 'percent ethnicity unknown',
'count ethnicity total', 'percent ethnicity total', 'count permanent resident alien', 'percent permanent resident alien',
'count us citizen', 'percent us citizen', 'count other citizen status', 'percent other citizen status',
'count citizen status unknown', 'percent citizen status unknown', 'count citizen status total',
'percent citizen status total', 'count receives public assistance', 'percent receives public assistance',
'count nreceives public assistance', 'percent nreceives public assistance', 'count public assistance unknown',
'percent public assistance unknown', 'count public assistance total', 'percent public assistance total']
#phew! what a task it was!

# now let us print our dataframe with the column headers assigned to them
print(nycdem_df1)
# wow! that looks wonferful

# we are printing a new line for readability sake
print('\n')

# now I am going to remove all the percent columns from my dataframe as I think we do not need them for further analysis
nycdem_df1.drop(['percent female', 'percent male', 'percent gender unknown', 'percent gender total', 
'percent pacific islander', 'percent hispanic latino', 'percent american indian', 'percent asian non hispanic', 
'percent white non hispanic', 'percent black non hispanic', 'percent other ethnicity', 'percent ethnicity unknown', 
'percent ethnicity total', 'percent permanent resident alien', 'percent us citizen', 'percent other citizen status', 
'percent citizen status unknown', 'percent citizen status total', 'percent receives public assistance', 
'percent nreceives public assistance', 'percent public assistance unknown', 'percent public assistance total'], axis = 1, 
inplace=True)

#now let us print the dataframe again with columns we need
print(nycdem_df1)
# as you can see in the console we have a total of 24 columns and 236 rows

# we are printing a new line for readability sake
print('\n')

# here jurisdiction name is the zip codes of the location in new york city
# our data frame consists of the demographic data per zipcode in New York City
# i know this as I have looked at the metadata in the website from which I have extracted my json dataset

# I am going to remove further columns which are basically the total of counts of categories
nycdem_df1.drop(['count participants', 'count gender total', 'count ethnicity total', 'count citizen status total',
'count public assistance total'], axis=1, inplace=True)

# now let us print the dataframe with our desired columns again
print(nycdem_df1)
#awesome

# we are printing a new line for readability sake
print('\n')

# now let us check whether any of our columns in our dataframe contain any missing values
print(nycdem_df1.isnull().sum())
# as you can see in the console, beside each column name there is zero which tells us that there are no missing values
# in any of our columns in our dataframe

# we are printing a new line for readability sake
print('\n')

# based on looking at the dataframe now, I can say that there are four sub-categories of data that are presnt in the
# dataset. One is sex, the other is race, next is citizenship status and lastly public assistance. Now what i plan to do is, is to
# subdivide the dataframe into smaller dataframes based on the categories and do analysis on them.

#sub-dividing the dataframe based on sex
nycdem_sex = nycdem_df1[['jurisdiction name', 'count female', 'count male', 'count gender unknown']]
#let us print the new subdivided dataframe on the console
print(nycdem_sex)
# awesome the subdivided dataframe looks wonderful

# we are printing a new line for readability sake
print('\n')

# now let us perform a summary statistic on our subset dataframe and explore it further
print(nycdem_sex.describe())
# looking at the console, I can say that the results produced for each column are count, unique, top and freq
# these results correspond to values of strings. That is the data type of column values is string.
# the first column is zip code and we will leave it as is, whereas the other columns are counts and hence it 
# makes more analytical sense to convert them as integers.

# we are printing a new line for readability sake
print('\n')

# we are using the to_numeric function to do the conversion
nycdem_sex['count female'] = pd.to_numeric(nycdem_sex['count female'])
nycdem_sex['count male'] = pd.to_numeric(nycdem_sex['count male'])
nycdem_sex['count gender unknown'] = pd.to_numeric(nycdem_sex['count gender unknown'])

# now let us do the summary statistics again on our dataframe of demographic sexes in new york city
print(nycdem_sex.describe())
# awesome now we can see the summary statistics for our values in the count female, count male and count gender unknown columns
# There are some useful insights we can garner here. The mean of females amongst all zip codes is 10.29 and for males is
# 7.36. By this we can say that there are more women in new york city as compared to men. The highest number of women
# living in a zipcode is 194 and that of men is 157

# we are printing a new line for readability sake
print('\n')

# its not a good python practice to have spaces in column names so let us replace the spaces with underscores
nycdem_sex.columns = ['jurisdiction_name', 'count_female', 'count_male', 'count_gender_unknown']

# now let us print our dataframe with our new columns names
print(nycdem_sex)
# awesome. we can see the data frame with the new columns names

# we are printing a new line for readability sake
print('\n')

# now let us look at the unique values of one of our columns in our data frame which is the count_gender_unknown
print(nycdem_sex.count_gender_unknown.unique())
# as you can see on the console, 0 gets printed. Hence there is only one unique value in that column, and that is zero. This tells us that there are no gender
# unknown people in any zip code in new york city. And hence I am going to delete that column from our data frame.
nycdem_sex.drop(['count_gender_unknown'], axis=1, inplace=True)

# now lets do some querying and produce some output files
# first we are going to look at all zipcodes where females are greater than males and store the data frame produced
# in a variable
nycdem_fmgtthma = nycdem_sex.query('count_female > count_male')
# query function returns a data frame

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of female is
# greater than count of male and also the respective count columns for both female and male.
print(nycdem_fmgtthma)

# we are printing a new line for readability sake
print('\n')

# we are importing the matplotlib package in our python file to use it to make some cool visualizations
import matplotlib.pyplot as plt

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_fmgtthma.plot(x = 'jurisdiction_name', y = ['count_female', 'count_male'])
plt.show()
# an image file pops out with the graph. As you can see for yourself, the line depicting count of females is higher than
# the one depicting count of males

# we will be importing xlwt package for writing excel data
import xlwt

# now let us produce an output excel file of our data frame that we queried
nycdem_fmgtthma.to_excel('output1.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# no we are going to look at all zipcodes where females are greater than the mean female count of 10. This mean value
# was found when we ran the descirbe function on our subdivided dataframe
nycdem_fmgtthme = nycdem_sex.query('count_female > 10.0')
# query function returns a data frame

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of female is
# greater than mean count of female and also the correspondong male count column 
print(nycdem_fmgtthme)

# we are printing a new line for readability sake
print('\n')

# let us produce a visualization of a plot that contains pattern of our values for female counts from our newly queried data frame
nycdem_fmgtthme.plot(x = 'jurisdiction_name', y = 'count_female')
plt.show()
# an image file pops out with the graph. As you can see for yourself. The line depicting count of females is higher than
# than the value 10 on the y-axis.

# now let us produce an output excel file of our data frame that we queried
nycdem_fmgtthme.to_excel('output2.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# Similarly we can use the query function to pass any expression we want and view the dataframe that gets produced based
# on the result we want and then visualize/analyze the results along with outputing them into a file.

#sub-dividing the dataframe based on race
nycdem_race = nycdem_df1[['jurisdiction name', 'count pacific islander', 'count hispanic latino', 'count american indian',
'count asian non hispanic', 'count white non hispanic', 'count black non hispanic', 'count other ethnicity', 
'count ethnicity unknown']]
#let us print the new subdivided dataframe on the console
print(nycdem_race)

# we are printing a new line for readability sake
print('\n')

# now let us perform a summary statistic on our subset dataframe and explore it further
print(nycdem_race.describe())
# looking at the console, I can say that the results produced for each column are count, unique, top and freq
# these results correspond to values of strings. That is if the data type of column values is string
# the first column is zip code and we will leave it as is, whereas the other columns are counts and hence it 
# makes more analytical sense to convert them as integers

# we are printing a new line for readability sake
print('\n')

# we are using the to_numeric function to do the conversion
nycdem_race['count pacific islander'] = pd.to_numeric(nycdem_race['count pacific islander'])
nycdem_race['count hispanic latino'] = pd.to_numeric(nycdem_race['count hispanic latino'])
nycdem_race['count american indian'] = pd.to_numeric(nycdem_race['count american indian'])
nycdem_race['count asian non hispanic'] = pd.to_numeric(nycdem_race['count asian non hispanic'])
nycdem_race['count white non hispanic'] = pd.to_numeric(nycdem_race['count white non hispanic'])
nycdem_race['count black non hispanic'] = pd.to_numeric(nycdem_race['count black non hispanic'])
nycdem_race['count other ethnicity'] = pd.to_numeric(nycdem_race['count other ethnicity'])
nycdem_race['count ethnicity unknown'] = pd.to_numeric(nycdem_race['count ethnicity unknown'])

# now let us do the summary statistics again on our dataframe of demographic races in new york city
print(nycdem_race.describe())
# awesome now we can see the summary statistics for our values in the count columns for all ethnicities
# There are some useful insights we can garner here. The mean of hispanics amongst all zip codes is 1.85 and for ethnicity
# unknown is 0.68. By this we can say that there are more hispanics in new york city as compared to people who do not
# know what their ethnicity is. The highest number of hispanics iving in a zipcode is 51 and that of pacific islander
# is 2

# we are printing a new line for readability sake
print('\n')

# its not a good python practice to have spaces in column names so let us replace the spaces with underscores
nycdem_race.columns = ['jurisdiction_name', 'count_pacific_islander', 'count_hispanic_latino', 'count_american_indian',
'count_asian_non_hispanic', 'count_white_non_hispanic', 'count_black_non_hispanic', 'count_other_ethnicity',
'count_ethnicity_unknown']

# now let us print our dataframe with our new column names
print(nycdem_race)
# awesome. we can see the data frame with the new column names

# we are printing a new line for readability sake
print('\n')

# now let us look at the unique values of some of our columns in our data frame 
print(nycdem_race.count_other_ethnicity.unique())
print(nycdem_race.count_ethnicity_unknown.unique())
# the reason I checked unique values for these columns is becasue if there were very few unique values then I would delete
# them for our analysis. After looking at the results in the console. I would like to keep them and not delete.

# we are printing a new line for readability sake
print('\n')

# now lets do some querying and produce some output files
# first we are going to look at all zip codes where the count of hispanics is greater than 20
nycdem_his = nycdem_race.query('count_hispanic_latino > 20.0')
# now in the resultant dataframe we get, we are going to look for zip codes where black populaiton is greater than 20
nycdem_hisanbl = nycdem_his.query('count_black_non_hispanic > 20.0')
# now what I get is a dataframe where the zipcodes are places in NYC where the population of blacks and hispanics is greater
# than 20. And it is also going to give us the counts of other races in those zipcodes too.

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of hispanics 
# and blacks is greater than 20.0. 
print(nycdem_hisanbl)

# we are printing a new line for readability sake
print('\n')

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_hisanbl.plot(x = 'jurisdiction_name', y = ['count_hispanic_latino', 'count_black_non_hispanic'])
plt.show()


# now let us produce an output excel file of our data frame that we queried
nycdem_hisanbl.to_excel('output3.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# now we are going to look at all zipcodes where other ethnicity is greater than 5. 
nycdem_oegrthfi = nycdem_race.query('count_other_ethnicity > 5.0')
# now from the dataframe that gets returned I am going to look for ethnicity unknown less than 4.
nycdem_oeaneu = nycdem_oegrthfi.query('count_ethnicity_unknown < 4.0')

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of other
# ethnicity is greater than 5 and ethnicity unknown less than 4. And it is also going to give us the counts of other 
# races in those zipcodes too.
print(nycdem_oeaneu)

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_oeaneu.plot(x = 'jurisdiction_name', y = ['count_other_ethnicity', 'count_ethnicity_unknown'])
plt.show()

# now let us produce an output excel file of our data frame that we queried
nycdem_oeaneu.to_excel('output4.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# Similarly we can use the query function to pass any expression we want and view the dataframe that gets produced based
# on the result we want and then visualize/analyze the results.

#sub-dividing the dataframe based on citizenship status
nycdem_cs = nycdem_df1[['jurisdiction name', 'count permanent resident alien', 'count us citizen', 
'count other citizen status', 'count citizen status unknown']]
#let us print the new subdivided dataframe on the console
print(nycdem_cs)

# we are printing a new line for readability sake
print('\n')

# now let us perform a summary statistic on our subset dataframe and explore it further
print(nycdem_cs.describe())
# looking at the console, I can say that the results produced for each column are count, unique, top and freq
# these results correspond to values of strings. That is if the data type of column values is string
# the first column is zip code and we will leave it as is, whereas the other columns are counts and hence it 
# makes more analytical sense to convert them as integers

# we are printing a new line for readability sake
print('\n')

# we are using the to_numeric function to do the conversion
nycdem_cs['count permanent resident alien'] = pd.to_numeric(nycdem_cs['count permanent resident alien'])
nycdem_cs['count us citizen'] = pd.to_numeric(nycdem_cs['count us citizen'])
nycdem_cs['count other citizen status'] = pd.to_numeric(nycdem_cs['count other citizen status'])
nycdem_cs['count citizen status unknown'] = pd.to_numeric(nycdem_cs['count citizen status unknown'])

# now let us do the summary statistics again on our dataframe of demographic citizenship status in new york city
print(nycdem_cs.describe())
# awesome now we can see the summary statistics for our values in the count columns for all citizens
# There are some useful insights we can garner here. The mean of us citizens amongst all zip codes is 17.16 and the maximum 
# us citizens living in a zipcode are 271. The maximum other citizens living in a zip code are 2.

# we are printing a new line for readability sake
print('\n')

# its not a good python practice to have spaces in column names so let us replace the spaces with underscores
nycdem_cs.columns = ['jurisdiction_name', 'count_permanent_resident_alien', 'count_us_citizen', 'count_other_citizen_status',
'count_citizen_status_unknown']

# now let us print our dataframe with our new column names
print(nycdem_cs)
# awesome. we can see the data frame with the new column names

# we are printing a new line for readability sake
print('\n')

# now let us look at the unique values of one of our columns in our data frame 
print(nycdem_cs.count_citizen_status_unknown.unique())
# there is only one unique value which gets printed on the console. That is 0. This value is not of much insight to us here
# in this context. Hence I am going to delete citizen_status_unknown column from my dataframe.

nycdem_cs.drop(['count_citizen_status_unknown'], axis = 1, inplace=True)

# we are printing a new line for readability sake
print('\n')

# now lets do some querying and produce some output files
# first we are going to look at all zipcodes where the count of us citizens is greater than 200
nycdem_usc = nycdem_cs.query('count_us_citizen > 200.0')

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of us citizens
# is greater than 200. These also can be presumed to be the most populous zipcodes of NYC as very few other citizens live
# in NYC, looking at our dataset. And it is also going to give us the counts of all citizen statuses in those zipcodes too.
print(nycdem_usc)

# we are printing a new line for readability sake
print('\n')

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_usc.plot(x = 'jurisdiction_name', y = ['count_us_citizen'])
plt.show()

# now let us produce an output excel file of our data frame that we queried
nycdem_usc.to_excel('output5.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# now we are going to look at all zipcodes where us permanent resident is greater than 3. 
nycdem_prgrthfi = nycdem_cs.query('count_permanent_resident_alien > 3.0')
# now from the dataframe that gets returned I am going to look for other citizens less than 2.
nycdem_pranoc = nycdem_prgrthfi.query('count_other_citizen_status < 2.0')

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where us permanent
# resident is greater than 3 and other citizen number is less than 2. And it is also going to give us the counts of
# all citizen statuses in those zipcodes too.
print(nycdem_pranoc)

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_pranoc.plot(x = 'jurisdiction_name', y = ['count_permanent_resident_alien', 'count_other_citizen_status'])
plt.show()

# now let us produce an output excel file of our data frame that we queried
nycdem_pranoc.to_excel('output6.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# Similarly we can use the query function to pass any expression we want and view the dataframe that gets produced based
# on the result we want and then visualize/analyze the results.

# sub-dividing the dataframe based on public assistance
nycdem_pa = nycdem_df1[['jurisdiction name', 'count receives public assistance', 'count nreceives public assistance', 
'count public assistance unknown']]
#let us print the new subdivided dataframe on the console
print(nycdem_pa)

# we are printing a new line for readability sake
print('\n')

# now let us perform a summary statistic on our subset dataframe and explore it further
print(nycdem_pa.describe())
# looking at the console, I can say that the results produced for each column are count, unique, top and freq
# these results correspond to values of strings. That is if the data type of column values is string
# the first column is zip code and we will leave it as is, whereas the other columns are counts and hence it 
# makes more analytical sense to convert them as integers

# we are printing a new line for readability sake
print('\n')

# we are using the to_numeric function to do the conversion
nycdem_pa['count receives public assistance'] = pd.to_numeric(nycdem_pa['count receives public assistance'])
nycdem_pa['count nreceives public assistance'] = pd.to_numeric(nycdem_pa['count nreceives public assistance'])
nycdem_pa['count public assistance unknown'] = pd.to_numeric(nycdem_pa['count public assistance unknown'])

# now let us do the summary statistics again on our dataframe of public assistance status in new york city
print(nycdem_pa.describe())
# awesome now we can see the summary statistics for our values in the count columns for all public assistance.
# There are some useful insights we can garner here. The mean of people who do not receive public assistance is greater
# than people who do not. This shows that people living in NYC are well off in general. The maximum people who receive
# public assistance is 155. The maximum people who do not receive public assistance is 206.

# we are printing a new line for readability sake
print('\n')

# its not a good python practice to have spaces in column names so let us replace the spaces with underscores
nycdem_pa.columns = ['jurisdiction_name', 'count_receives_public_assistance', 'count_nreceives_public_assistance', 
'count_public_assistance_unknown']

# now let us print our dataframe with our new column names
print(nycdem_pa)
# awesome. we can see the data frame with the new column names

# we are printing a new line for readability sake
print('\n')

# now let us look at the unique values of one of our columns in our data frame 
print(nycdem_pa.count_public_assistance_unknown.unique())
# there is only one unique value which gets printed on the console. That is 0. This value is not of much insight to us here
# in this context. Hence I am going to delete count_public_assistance__unknown column from my dataframe.

nycdem_pa.drop(['count_public_assistance_unknown'], axis = 1, inplace=True)

# we are printing a new line for readability sake
print('\n')

# now lets do some querying and produce some output files
# first we are going to look at all zipcodes where public assistance is less than 50.0
nycdem_paltfi = nycdem_pa.query('count_receives_public_assistance < 50.0')
# now we are going to look at the count of people who do not receive public assistance more than 100.0 from the zip codes
# which we got just now where public assistance is less than 50.0
nycdem_paannpa = nycdem_paltfi.query('count_nreceives_public_assistance > 100.0')

# now when I print this variable on the console. We get our dataframe consisting of all zipcodes where count of people who
# receive public assistance is less than 50.0 and count of people who do not receive public assistance greater than 100.0
# And it is also going to give us the counts of all citizen statuses in those zipcodes too.
print(nycdem_paannpa)

# we are printing a new line for readability sake
print('\n')

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_paannpa.plot(x = 'jurisdiction_name', y = ['count_receives_public_assistance', 'count_nreceives_public_assistance'])
plt.show()

# now let us produce an output excel file of our data frame that we queried
nycdem_paannpa.to_excel('output7.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# now we are going to look at all zip codes where people receiving public assistance is greater than 100.0 
nycdem_pagrthhu = nycdem_pa.query('count_receives_public_assistance > 100.0')
# now from the dataframe that gets returned I am going to look for people who do not receive public assistance less than 150.0
nycdem_pandnpa = nycdem_pagrthhu.query('count_nreceives_public_assistance < 150.0')

# now when I print this variable on the console. We get our dataframe consisting of all people who do receive public assistance
# greater than 100.0 and all people who do not receive public assistance less than 150.0.
print(nycdem_pandnpa)

# let us produce a visualization of a plot that contains patterns of our values from our newly queried data frame
nycdem_pandnpa.plot(x = 'jurisdiction_name', y = ['count_receives_public_assistance', 'count_nreceives_public_assistance'])
plt.show()

# now let us produce an output excel file of our data frame that we queried
nycdem_pandnpa.to_excel('output8.xlsx', index = False)
# an excel file gets saved in the same directiry as you are running this python file. And I have given the value False to
# index method in the function so that the index of the dataframe does not be part of the excel file. If you open the 
# excel file, you can view the dataframe with the columns being the header row.

# Similarly we can use the query function to pass any expression we want and view the dataframe that gets produced based
# on the result we want and then visualize/analyze the results.

# The code for the mini project ends here. Thank you.