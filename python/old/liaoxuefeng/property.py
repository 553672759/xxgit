#防止参数暴露而被随意更改
#使用@property

class Student(object):

	def get_score(slef):
		return self._score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score musst be integer')
		if value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score=value

s=Student()
print(s.set_score(1000))
print(s.get_score())

class School(object):

	@property
	def ban(self):
		return self._ban

	@ban.setter
	def ban(self,value):
		if not isinstance(value, int):
            raise ValueError('ban must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('ban must between 0 ~ 100!')
        self._score = value