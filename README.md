# python-web-scrapper

## Prerequisites
- `python 3.10`
- `requests 2.25.1`
- `beautifulsoup4 4.11.2`
- Install requirements: `pip install -r requirements.txt`
- Suggestion: Install these extensions to see the results more clearly
  -  [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one). Press `ctrl+k v` to preview markdown.
  -  [json](https://marketplace.visualstudio.com/items?itemName=ZainChen.json)

## Run program
```
    usage: app.py [-h] [-c CATEGORY]

    Python web scrapper.

    options:
    -h, --help            show this help message and exit
    -c CATEGORY, --category CATEGORY
                            Category to scrape.
```
- Example: `python3 NguyenSyPhiLong.py -c khoa-hoc`
- List of categories: `the-gioi`, `xa-hoi`, `van-hoa`, `kinh-te`, `giao-duc`, `the-thao`, `giai-tri`, `phap-luat`, `khoa-hoc-cong-nghe`, `khoa-hoc`, `doi-song`, `xe-co`, `nha-dat`

## Further development
- Folder: `./multiprocessing/`
- Run in parallel using python `multiprocessing` module.
- Run `python3 cores.py` to see how many cpus your system has. Example output: `Number of cpu: 8`
- Run `python3 app-parallel.py` to get the output.
- Idea: The code defines a `scrape_category` function that takes a category as input and performs the web scraping process. The main function creates a list of categories, creates a process pool with 6 workers, and maps the `scrape_category` function to each category in parallel using the `multiprocessing.Pool.map` method. The `Pool.close` and `Pool.join` methods are used to free up resources after the scraping is complete.