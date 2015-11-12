说明：
    运行方式：scrapy crawl yunvs

    stock_list_20150914.txt是股票名称和代号，如果要添加则按照‘代号\t股票’添加到该文档即可。

    stock_list_result_20151109.txt是输出爬虫www.yuncaijing.com得到的结果，格式'代号\t股票\t主题;主题;...;主题'，如要修改输出文件的名称，在pipelines.py中修改即可。
