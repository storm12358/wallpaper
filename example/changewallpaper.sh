#!/bin/bash

rm ~/.config/awesome/wallpaper.jpg
cd ~/wallpaper
proxychains scrapy crawl wallpaper
ln -s ~/wallpaper/wallpaper.jpg ~/.config/awesome/wallpaper.jpg
cd ~
