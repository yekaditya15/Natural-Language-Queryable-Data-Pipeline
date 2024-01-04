import scrapy
import json
import re

class MainSpider(scrapy.Spider):
    name = 'main'
    start_urls = None

    def __init__(self, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)

        # Load settings from JSON file
        with open('config.json', 'r') as file:
            settings = json.load(file)

        # Set spider attributes from the loaded settings
        self.start_urls = settings.get('start_urls', [])

    regex_rules = {
        r'\n\s*\n': r'\n',
        r'^\s*$': r'',
         r'^\s+|\s+$': r'',
        r'\n\s*\n': r'\n' 
    }

    def parse(self, response):
        span_elements = response.css('span')
        data_dict = {}

        for span in span_elements:
            class_identifier = span.css('::attr(class)').get()
            text_content = span.css('::text').get()

            # Check if text_content is not None before applying regex
            if text_content is not None:
                for pattern, replacement in self.regex_rules.items():
                    text_content = re.sub(pattern, replacement, text_content)

                if class_identifier and text_content:
                    if class_identifier in data_dict:
                        data_dict[class_identifier].append(text_content)
                    else:
                        data_dict[class_identifier] = [text_content]

        self.log(f'Data: {data_dict}')
        self.save_as_json(data_dict)

    def save_as_json(self, data):
        file_path = 'output.json'

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        self.log(f'Data saved as JSON in {file_path}')
