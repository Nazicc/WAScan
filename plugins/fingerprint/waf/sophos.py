#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I 

def sophos(headers,content):
	_ = False
	_ |= search(r"Powered by UTM Web Protection",content) is not None
	if _ : 
		return "UTM Web Protection (Sophos)"