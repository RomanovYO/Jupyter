@echo off

set https_proxy=http://172.16.1.30:3128
set http_proxy=http://172.16.1.30:3128
set ftp_proxy=http://172.16.1.30:3128

c:
cd C:\Work\DataAnalyst\Jupyter\
jupyter notebook
