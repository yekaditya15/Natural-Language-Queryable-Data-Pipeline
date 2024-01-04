# Introduction


## Data Pipeline

A data pipeline is a set of processes that collects, transforms and delivers data from one or multiple sources to a destination for storage, processing, and analysis. In a data pipeline, multiple data processing elements are connected in series where the output of one element is connected in series, where output of one element is the input of another element.

A data pipeline represents a structured and automated approach to the movement, transformation, and storage of data from diverse sources to designated destinations

# Data Ingestion



## Scraping

Web scraping is the process of automatically extracting information from websites by systematically mapping websites, sending HTTP requests to download web pages.

### HTTP Requests

## Parsing

Parsing is the breaking down of the HTML document to a structured format according to the context so that data can be readily processed. In the implementation of this project, 

### HTML

#### Tag metadata

### Document Object Model (DOM)

## DOM destructuring

As in the project implementation, only the text data are supposed to be extracted. However, the derived DOM tree contains a lot of unnecessary data like styles, scripts and their dependencies and unnecessary nesting for the text data extraction point of view. It also contains redundant and repeated data, which also supposed to be removed. 

It is observed that most of the tags (or their parents) that containing text data contains some identifiers that gives idea of content of the data enclosed.

This is an an extract from html code of a product from an ecommerce site showing the price of the product:

<span class="a-price" data-a-size="xl" data-a-color="base">
    <span class="a-offscreen">
        ₹26,990
    </span>
    <span aria-hidden="true">
        <span class="a-price-symbol">
            ₹
        </span>
        <span class="a-price-whole">
            26,990
        </span>
    </span>
</span>

Here the only relevant information in the point of view of text data is the price: `26990₹`, which could just be represented in a key value pair:

"price" : "26990₹"

The multiple levels of complex nesting and unnecessary redundencies can be observed from this snippet. The goal of DOM destructuring is to remove redundancies and reduce nesting to maximise information entropy. Here it is also observed that the tags and even their parent tags contains some idea of what data is enclosed in it. However there exists some websites or some parts of the same webpage of which the metadata of tags gives no idea of their content as in the following snippet from another ecommerce site:

<div class="_6jPmlQ">
    <div class="_3pLy-c row">
        <div class="col col-7-12">
            <div class="_4rR01T">
                ASUS Vivobook S 14 Flip TN3402QA-LZ540WS...
            </div>
            <div class="fMghEO">
                <ul class="_1xgFaf">
                    <li class="rgWa7D">AMD Ryzen 5 Hexa Core Processor</li>
                    <li class="rgWa7D">16 GB DDR4 RAM</li>
                    <li class="rgWa7D">Windows 11 Operating System</li>
                    <li class="rgWa7D">512 GB SSD</li>
                    <li class="rgWa7D">35.56 cm (14 Inch) Touchscreen Display</li>
                    <li class="rgWa7D">1 Year Onsite Warranty</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="_3pLy-c row">
        <div class="col col-7-12">
            <div class="_4rR01T">
                ASUS Vivobook 16X M1603QA-MB712WS...
            </div>
            <div class="gUuXy-">
                <ul class="_1xgFaf">
                    <li class="rgWa7D">AMD Ryzen 7 Octa Core Processor</li>
                    <li class="rgWa7D">16 GB DDR4 RAM</li>
                    <li class="rgWa7D">64 bit Windows 11 Operating System</li>
                    <li class="rgWa7D">512 GB SSD</li>
                    <li class="rgWa7D">40.64 cm (16 inch) Display</li>
                    <li class="rgWa7D">Windows 11, Microsoft Office HS 2021, 1 Year McAfee</li>
                    <li class="rgWa7D">1 Year Onsite Warranty</li>
                </ul>
            </div>
        </div>
    </div>
</div>

Here even though the tag metadata contains no relevant information, the text content gives a view to what type of information it conveys about, By the statement "AMD Ryzen 5 Hexa Core Processor", it can be assumed that it is mentioning about the Processor and similarily by understanding the words and comparing with world knowledge will provide us with some insight.

Also the DOM structure also provide some insights about the relation between the data in the neighboring tag. From the above snippet it can easily be understood that the product "ASUS Vivobook S 14 Flip Ryzen 5" is the one having "14 Inch Touchscreen Display" not "ASUS Vivobook 16X".

Sometimes not only the DOM structure, text content or tag metadata the geometric alignment (or computed styles) of the product may give some insight of the data type content.

<image>

The aim of the DOM destructuring is to convert these complicated DOM structures to simpler context dependent structures that can be easily read and processed by machines.

For the snippet 2, an expected JSON extraction is:

[
    {
        "unknown-key-0": "ASUS Vivobook S 14 Flip TN3402QA-LZ540WS...",
        "unknown-key-1": "AMD Ryzen 5 Hexa Core Processor",
        "unknown-key-2": "16 GB DDR4 RAM",
        "unknown-key-3": "Windows 11 Operating System",
        "unknown-key-4": "512 GB SSD",
        "unknown-key-5": "35.56 cm (14 Inch) Touchscreen Display",
        "unknown-key-6": "1 Year Onsite Warranty"
    },
    {
        "unknown-key-0": "ASUS Vivobook 16X M1603QA-MB712WS...",
        "unknown-key-1": "AMD Ryzen 7 Octa Core Processor",
        "unknown-key-2": "16 GB DDR4 RAM",
        "unknown-key-3": "64 bit Windows 11 Operating System",
        "unknown-key-4": "512 GB SSD",
        "unknown-key-5": "40.64 cm (16 inch) Display",
        "unknown-key-6": "Windows 11, Microsoft Office HS 2021, 1 Year McAfee",
        "unknown-key-7": "1 Year Onsite Warranty"
    }
]



### Data Serialization