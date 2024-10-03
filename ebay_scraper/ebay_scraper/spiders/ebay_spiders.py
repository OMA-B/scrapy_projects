import json, os, pandas as pd, time
from scrapy import Spider
from scrapy.utils.project import get_project_settings



def gather_urls_from_input_file():
    with open(file=os.path.join(os.path.dirname(__file__), 'input.json'), mode='r') as file:
        input_data = json.load(fp=file)

    links_in_input_data = []
    for data in input_data:
        for link in data['links']: links_in_input_data.append(link)

    return links_in_input_data


class EbaySpider1(Spider):

    name = 'ebay_spider_1'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[:urls_portion]
        self.start_time = time.time()
        self.items = []
        print('spider 1 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_1'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_1 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider2(Spider):

    name = 'ebay_spider_2'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion:urls_portion*2]
        self.start_time = time.time()
        self.items = []
        print('spider 2 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_2'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_2 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider3(Spider):

    name = 'ebay_spider_3'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*2:urls_portion*3]
        self.start_time = time.time()
        self.items = []
        print('spider 3 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_3'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_3 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider4(Spider):

    name = 'ebay_spider_4'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*3:urls_portion*4]
        self.start_time = time.time()
        self.items = []
        print('spider 4 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_4'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_4 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider5(Spider):

    name = 'ebay_spider_5'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*4:urls_portion*5]
        self.start_time = time.time()
        self.items = []
        print('spider 5 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_5'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_5 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider6(Spider):

    name = 'ebay_spider_6'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*5:urls_portion*6]
        self.start_time = time.time()
        self.items = []
        print('spider 6 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_6'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_6 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider7(Spider):

    name = 'ebay_spider_7'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*6:urls_portion*7]
        self.start_time = time.time()
        self.items = []
        print('spider 7 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_7'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_7 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider8(Spider):

    name = 'ebay_spider_8'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*7:urls_portion*8]
        self.start_time = time.time()
        self.items = []
        print('spider 8 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_8'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_8 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider9(Spider):

    name = 'ebay_spider_9'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*8:urls_portion*9]
        self.start_time = time.time()
        self.items = []
        print('spider 9 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_9'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_9 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()

    
class EbaySpider10(Spider):

    name = 'ebay_spider_10'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 100)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*9:urls_portion*10]
        self.start_time = time.time()
        self.items = []
        print('spider 10 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_10'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_10 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider11(Spider):

    name = 'ebay_spider_11'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 110)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*10:urls_portion*11]
        self.start_time = time.time()
        self.items = []
        print('spider 11 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_11'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_11 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider12(Spider):

    name = 'ebay_spider_12'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 120)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*11:urls_portion*12]
        self.start_time = time.time()
        self.items = []
        print('spider 12 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_12'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_12 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider13(Spider):

    name = 'ebay_spider_13'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 130)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*12:urls_portion*13]
        self.start_time = time.time()
        self.items = []
        print('spider 13 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_13'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_13 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider14(Spider):

    name = 'ebay_spider_14'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 140)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*13:urls_portion*14]
        self.start_time = time.time()
        self.items = []
        print('spider 14 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_14'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_14 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider15(Spider):

    name = 'ebay_spider_15'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 150)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*14:urls_portion*15]
        self.start_time = time.time()
        self.items = []
        print('spider 15 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_15'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_15 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider16(Spider):

    name = 'ebay_spider_16'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 160)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*15:urls_portion*16]
        self.start_time = time.time()
        self.items = []
        print('spider 16 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_16'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_16 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider17(Spider):

    name = 'ebay_spider_17'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 170)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*16:urls_portion*17]
        self.start_time = time.time()
        self.items = []
        print('spider 17 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_17'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_17 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider18(Spider):

    name = 'ebay_spider_18'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 180)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*17:urls_portion*18]
        self.start_time = time.time()
        self.items = []
        print('spider 18 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_18'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_18 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider19(Spider):

    name = 'ebay_spider_19'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 190)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*18:urls_portion*19]
        self.start_time = time.time()
        self.items = []
        print('spider 19 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_19'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_19 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider20(Spider):

    name = 'ebay_spider_20'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 200)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*19:urls_portion*20]
        self.start_time = time.time()
        self.items = []
        print('spider 20 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_20'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_20 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider21(Spider):

    name = 'ebay_spider_21'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 210)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*20:urls_portion*21]
        self.start_time = time.time()
        self.items = []
        print('spider 21 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_21'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_21 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider22(Spider):

    name = 'ebay_spider_22'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 220)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*21:urls_portion*22]
        self.start_time = time.time()
        self.items = []
        print('spider 22 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_22'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_22 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider23(Spider):

    name = 'ebay_spider_23'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 230)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*22:urls_portion*23]
        self.start_time = time.time()
        self.items = []
        print('spider 23 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_23'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_23 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider24(Spider):

    name = 'ebay_spider_24'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 240)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*23:urls_portion*24]
        self.start_time = time.time()
        self.items = []
        print('spider 24 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_24'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_24 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider25(Spider):

    name = 'ebay_spider_25'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 250)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*24:urls_portion*25]
        self.start_time = time.time()
        self.items = []
        print('spider 25 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_25'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_25 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider26(Spider):

    name = 'ebay_spider_26'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 260)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*25:urls_portion*26]
        self.start_time = time.time()
        self.items = []
        print('spider 26 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_26'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_26 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider27(Spider):

    name = 'ebay_spider_27'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 270)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*26:urls_portion*27]
        self.start_time = time.time()
        self.items = []
        print('spider 27 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_27'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_27 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider28(Spider):

    name = 'ebay_spider_28'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 280)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*27:urls_portion*28]
        self.start_time = time.time()
        self.items = []
        print('spider 28 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_28'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_28 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider29(Spider):

    name = 'ebay_spider_29'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 290)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*28:urls_portion*29]
        self.start_time = time.time()
        self.items = []
        print('spider 29 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_29'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_29 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider30(Spider):

    name = 'ebay_spider_30'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 300)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*29:urls_portion*30]
        self.start_time = time.time()
        self.items = []
        print('spider 30 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_30'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_30 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider31(Spider):

    name = 'ebay_spider_31'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 310)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*30:urls_portion*31]
        self.start_time = time.time()
        self.items = []
        print('spider 31 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_31'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_31 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider32(Spider):

    name = 'ebay_spider_32'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 320)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*31:urls_portion*32]
        self.start_time = time.time()
        self.items = []
        print('spider 32 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_32'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_32 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider33(Spider):

    name = 'ebay_spider_33'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 330)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*32:urls_portion*33]
        self.start_time = time.time()
        self.items = []
        print('spider 33 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_33'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_33 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider34(Spider):

    name = 'ebay_spider_34'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 340)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*33:urls_portion*34]
        self.start_time = time.time()
        self.items = []
        print('spider 34 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_34'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_34 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider35(Spider):

    name = 'ebay_spider_35'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 350)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*34:urls_portion*35]
        self.start_time = time.time()
        self.items = []
        print('spider 35 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_35'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_35 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider36(Spider):

    name = 'ebay_spider_36'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 360)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*35:urls_portion*36]
        self.start_time = time.time()
        self.items = []
        print('spider 36 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_36'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_36 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider37(Spider):

    name = 'ebay_spider_37'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 370)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*36:urls_portion*37]
        self.start_time = time.time()
        self.items = []
        print('spider 37 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_37'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_37 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider38(Spider):

    name = 'ebay_spider_38'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 380)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*37:urls_portion*38]
        self.start_time = time.time()
        self.items = []
        print('spider 38 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_38'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_38 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider39(Spider):

    name = 'ebay_spider_39'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 390)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*38:urls_portion*39]
        self.start_time = time.time()
        self.items = []
        print('spider 39 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_39'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_39 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider40(Spider):

    name = 'ebay_spider_40'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 400)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*39:urls_portion*40]
        self.start_time = time.time()
        self.items = []
        print('spider 40 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_40'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_40 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider41(Spider):

    name = 'ebay_spider_41'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 410)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*40:urls_portion*41]
        self.start_time = time.time()
        self.items = []
        print('spider 41 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_41'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_41 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider42(Spider):

    name = 'ebay_spider_42'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 420)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*41:urls_portion*42]
        self.start_time = time.time()
        self.items = []
        print('spider 42 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_42'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_42 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider43(Spider):

    name = 'ebay_spider_43'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 430)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*42:urls_portion*43]
        self.start_time = time.time()
        self.items = []
        print('spider 43 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_43'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_43 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider44(Spider):

    name = 'ebay_spider_44'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 440)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*43:urls_portion*44]
        self.start_time = time.time()
        self.items = []
        print('spider 44 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_44'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_44 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider45(Spider):

    name = 'ebay_spider_45'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 450)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*44:urls_portion*45]
        self.start_time = time.time()
        self.items = []
        print('spider 45 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_45'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_45 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider46(Spider):

    name = 'ebay_spider_46'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 460)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*45:urls_portion*46]
        self.start_time = time.time()
        self.items = []
        print('spider 46 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_46'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_46 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider47(Spider):

    name = 'ebay_spider_47'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 470)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*46:urls_portion*47]
        self.start_time = time.time()
        self.items = []
        print('spider 47 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_47'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_47 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider48(Spider):

    name = 'ebay_spider_48'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 480)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*47:urls_portion*48]
        self.start_time = time.time()
        self.items = []
        print('spider 48 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_48'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_48 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider49(Spider):

    name = 'ebay_spider_49'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 490)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*48:urls_portion*49]
        self.start_time = time.time()
        self.items = []
        print('spider 49 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_49'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_49 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()


class EbaySpider50(Spider):

    name = 'ebay_spider_50'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.batch_size = settings.getint('BATCH_SIZE', 500)
        self.output_format = settings.get('OUTPUT_FORMAT', 'json')
        urls_portion = settings.getint('EACH_SPIDER_URLS_PORTION')
        self.start_urls = gather_urls_from_input_file()[urls_portion*49:urls_portion*50]
        self.start_time = time.time()
        self.items = []
        print('spider 50 done...')

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'html': response.css('html').get(),
        }
        self.items.append(item)

    def save_batch(self):
        filename = f'outputs/spider_output_50'
        if self.output_format == 'json':
            filename += '.json'
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        elif self.output_format == 'jsonlines':
            filename += '.jl'
            with open(filename, 'w') as f:
                for item in self.items:
                    f.write(json.dumps(item) + "\n")
        elif self.output_format == 'parquet':
            filename += '.parquet'
            df = pd.DataFrame(self.items)
            df.to_parquet(filename)

    def closed(self, reason):
        end_time = time.time()
        duration = (end_time - self.start_time) / 60
        with open(file='log.txt', mode='a+') as file:
            file.write(f"\nSpider_50 closed: {reason}. Duration: {duration} minutes")
        
        self.save_batch()