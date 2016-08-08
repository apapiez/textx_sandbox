from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export
from textx.export import model_export
hello_meta = metamodel_from_file('hello.tx')
metamodel_export(hello_meta, 'hello_meta.dot')

example_hello_model = hello_meta.model_from_file('example.hello')
model_export(example_hello_model, 'example.dot')
