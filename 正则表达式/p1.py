'''
. 代表任意0或者1个字符 >= 0
* 代表前面的任意字符
? 非贪婪模式
+ 至少出现一次 >=1
{} 出现多少次
| 或者功能
[] 匹配中括号中任意一个 例如[0-9] [a-z] [A-Z] [.]就是匹配.
\s 匹配空格
\S 匹配不为空格 和\s相反
\w 匹配字母或数字或下划线或汉字 等价于 [A-Za-z0-9_]
\W 和\w相反
[\u4E00-\u9FA5] 代表汉字
\d 数字
'''
import re

# line = 'xxx出生于2001年6月1日'
# line = 'xxx出生于2001/6/1'
# line = 'xxx出生于2001-6-1'
# line = 'xxx出生于2001/06/01'
# line = 'xxx出生于2001-06-01'
line = 'xxx出生于2001-06'
# line = 'xxx出生于2001年06月'
# regex_str = '.*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|\d{1,2}|[月/-]$))'
regex_str = '.*出生于(.*$)'
r = re.match(regex_str, line)

if r:
    print(r.group(1))
else:
    print('none')
