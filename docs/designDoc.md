# Scrape-Crawler Design Doc



### Objects


#### ScrapeObject
ScrapeObject defines an input ie. target to scrape and the output. It also
specifies the parts of the target that need to be scraped and the means to
scrape them. It can be defined as part of a scrape job.

##### Spec
_Input_: url (to scrape) string  
_Output_: JSON-style object

###### xml format (_experimental_):
```
<scrape name="ScrapeObjectName">
  <input attr="attribute_variable_name" type="datatype" />
  <input attr="attribute_variable_name" type="datatype" />
  <output ...>
</scrape>
```

#### ScrapeJob
ScrapeJob defines a scraping job to be executed. It optionally defines
scraping objects (or can refer to objects defines elsewhere) and how to
connect them together.
