# **Getting started**

create virtualenv: `virtualenv -p python3 venv`

activate the virtualenv: `source venv/bin/activate`


# **Threading**

* Write a Python program to download multiple files concurrently using threads.
> * Use the following urls
>> *  https://www.northwestknowledge.net/metdata/data/pr_1979.nc
>> *  https://www.northwestknowledge.net/metdata/data/pr_1980.nc
>> *  https://www.northwestknowledge.net/metdata/data/pr_1981.nc
>> *  https://www.northwestknowledge.net/metdata/data/pr_1982.nc 
> * Output should be: 
>> * url: https://www.northwestknowledge.net/metdata/data/pr_1979.nc time: 16.381176710128784
     url: https://www.northwestknowledge.net/metdata/data/pr_1980.nc time: 11.475878953933716
     url: https://www.northwestknowledge.net/metdata/data/pr_1981.nc time: 13.059367179870605
     url: https://www.northwestknowledge.net/metdata/data/pr_1982.nc time: 12.232381582260132
     Total time: 53.15849542617798 

# **Processing**

* Write a Python program to find squares of numbers in a given list (list generated from 1 to an input number)
> * input: max value for generating a list of numbers (i.e.: 5) 
> * output: list of squares numbers (i.e.: 1, 4, 9, 16)
> * HINT! use pool