#枚举类
from enum import enum

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,menber in Month.__members__.items():
	print(name,'=>',member,',',member.value)

from enum import Enum,unique

#@unique可以检查有没有重复值
@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sta=6