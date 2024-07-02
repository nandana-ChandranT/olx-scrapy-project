# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy

class OlxPropertyItem(scrapy.Item):
    property_name = scrapy.Field()
    property_id = scrapy.Field()
    breadcrumbs = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    seller_name = scrapy.Field()
    location = scrapy.Field()
    property_type = scrapy.Field()
    bathrooms = scrapy.Field()
    bedrooms = scrapy.Field()

