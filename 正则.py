# -*- coding: utf-8 -*-

# 导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
p = re.compile(r'hell[123]o\d\D\w{1,5}(e|d)')

result = re.match(p, 'hell1o9dBe')
if result:
    print result.group()
else:
    print '匹配失败'

