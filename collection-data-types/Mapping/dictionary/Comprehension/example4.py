sales={2010:45000, 
       2011:54000, 
       2012:56000, 
       2013:49000, 
       2014:70000, 
       2015:35000}
print(sales)
sales1={year:s for year,s in sales.items() if s<=50000}
sales2={year:s for year,s in sales.items() if s>50000}
print(sales1)
print(sales2)