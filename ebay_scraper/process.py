import asyncio, subprocess, time, json, os, pandas as pd


async def run_spider(spider):
    process = await asyncio.create_subprocess_exec(
        'scrapy', 'crawl', spider,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        print(f"Spider {spider} finished successfully:\n{stdout.decode()}")
    else:
        print(f"Spider {spider} encountered an error:\n{stderr.decode()}")

async def run_spiders():
    start_time = time.time()
    
    spiders = [f'ebay_spider_{i+1}' for i in range(50)]

    tasks = [run_spider(spider) for spider in spiders]
    await asyncio.gather(*tasks)

    end_time = time.time()
    duration = (end_time - start_time) / 60
    print(f"Total duration: {duration:.2f} minutes")
    with open(file='log.txt', mode='a+') as file:
        file.write(f"\nTotal duration: {duration:.2f} minutes")


def merge_all_the_output_files_into_one():
    with open(file='ebay_scraper/config.json', mode='r') as file:
        output_format = json.load(fp=file)['OUTPUT_FILE_TYPE']

    if output_format == 'json':
        merged_data = []
        for file in os.listdir(path='outputs'):
            with open(f'outputs/{file}', 'r') as f:
                data = json.load(f)
                merged_data.extend(data)
            os.remove(path=f'outputs/{file}')
        
        with open('outputs.json', 'w') as file:
            json.dump(merged_data, file, indent=4)

    elif output_format == 'jsonlines':
        with open('outputs.jl', 'w') as outfile:
            for file in os.listdir(path='outputs'):
                with open(f'outputs/{file}', 'r') as infile:
                    for line in infile:
                        outfile.write(line)
                os.remove(path=f'outputs/{file}')

    elif output_format == 'parquet':
        dataframes = []
        for file in os.listdir(path='outputs'):
            dataframes.append(pd.read_parquet(f'outputs/{file}'))
            os.remove(path=f'outputs/{file}')
        merged_df = pd.concat(dataframes, ignore_index=True)
        merged_df.to_parquet('outputs.parquet')

if __name__ == "__main__":
    asyncio.run(run_spiders())
    # merge_all_the_output_files_into_one()