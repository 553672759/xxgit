#单元测试，用于对一个模块，一个韩式，或者一个类来测试正确性的工作

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest

class TestDict(unittest,TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)#断言函数返回的结果等于1
		self.assertEqual(d.b,'test')
		self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty