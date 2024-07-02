import scrapy
from olx.items import OlxPropertyItem

class OlxRentalsSpider(scrapy.Spider):
    name = 'olx_spider'
    allowed_domains = ["olx.in"]
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self, response):
        # Parse listings on the first page
        property_links = response.css('li._1DNjI::attr(href)').getall()  # Adjust selector based on OLX structure
        for link in property_links:
            yield response.follow(link, callback=self.parse_property)

        # Check for "Load More" button and follow it if present
        next_page = response.css('li.TA_b7::attr(href)').get()  # Example selector for "Load More" button
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_property(self, response):
        property_name = response.css('h1._1hJph::text').get()
        property_id = response.url.split('div._1-os0')[-1]  # Extracting ID from URL
        breadcrumbs = response.css('ol.rui-2Pidb::text').getall()
        price_amount = response.css('span.T8y-Z::text').get()  # Adjust selector for price amount
        
        image_url = response.css('div._23Jeb::attr(src)').get()  # Adjust selector for image URL
        description = response.css('h3._30eN9::text').get()  # Adjust selector for description
        seller_name = response.css('div.rui-oN78c::text').get()  # Adjust selector for seller name
        location = response.css('div.place-card place-card-medium::text').get()  # Adjust selector for location
        property_type = response.css('span.B6X7c::text').get()  # Adjust selector for property type
        bathrooms = int(response.css('span._3V4pD::text').get())  # Adjust selector for bathrooms
        bedrooms = int(response.css('span._3V4pD::text').get())  # Adjust selector for bedrooms

        yield {
            'property_name': property_name,
            'property_id': property_id,
            'breadcrumbs': breadcrumbs,
            'price': {
                'amount': price_amount,
                'currency': price_currency,
            },
            'image_url': image_url,
            'description': description,
            'seller_name': seller_name,
            'location': location,
            'property_type': property_type,
            'bathrooms': bathrooms,
            'bedrooms': bedrooms,
        }




    
