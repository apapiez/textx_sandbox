from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export
from textx.export import model_export
coshh_meta = metamodel_from_file('coshh.tx')
metamodel_export(coshh_meta, 'coshh.dot')
example_coshh_model = coshh_meta.model_from_file('test.coshh')
model_export(example_coshh_model, 'coshh_example.dot')