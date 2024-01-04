Given the keyword , provide precise and detailed information about it in the context. Extract all relevant details, key attributes, and any associated information.Do not take information form example,if data not found give NA.

The output should look like a JSON format. Just extract information from the context and be precise not from example.
The context and question are separated by delimiters *

for example:-
*
   "red-color-name": ["Iphone\t14", "Samsung S21"],
    "a46768b24f1b318283de164b5da6f3c0": ["Excellent smartphone with 13mp camera and A13 Processor", "Powerful smartphone with a 64MP camera and Exynos 2100 Processor"],
    "cost-abc": ["36000", "45000"],
    "number": ["46223", "1200"],
    "345soTi": ["\n \n", "\n\n \t"] 


query:-[ name price description]
expected result:-
  Divide each product or item seperate as json do not take as list.
    "name": "Iphone 14",
    "price": price of corresponding name in a context if missing give na in that position,
    "description": "description of the corresponding item in a context if not present give na in that position".

    "name": "Samsung S21",
     "price": price of corresponding name in a context if missing give na in that position,
    "description": "description of the corresponding item in a context if not present give na in that position".

     

    
    *
Don't use example information to answer the question only take from context
*{context}*
keyword: *{question}*
Helpful Answer: