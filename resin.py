from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export
from textx.export import model_export

class SimpleType(object):
	def __init__(self, parent, name):
		self.parent = parent
		self.name = name
		
myobjs = {'integer':SimpleType(None, 'integer'),
		  'string':SimpleType(None, 'string')
		  }

meta = metamodel_from_file('test.resin',
						    classes=[SimpleType],
							builtins=myobjs)