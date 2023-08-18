import bpy


def add_properties(*args, **kwargs):
    '''adds properties
    exec example:
    pd.add_properties([bpy.context.active_object],
                        properties = {"one":{"default_value":True,
                        'min':-10.0,
                        'max':10.0,
                        'soft_min':-5,
                        'soft_max':5})

    '''

    if not args:
        raise Exception("target object; args[0] is missing")
    target_objects = kwargs.get('target_objects', args[0])
    user_dictionary = kwargs.get('properties', {})

    if not isinstance(target_objects, list):
        raise Exception('target_objects has to be of type list')

    for a_target_object in target_objects:
        for a_property in user_dictionary:
            print(a_property)
            a_target_object[a_property] = user_dictionary[a_property]['default_value']
            a_target_object.id_properties_ensure()
            property_manager = a_target_object.id_properties_ui(a_property)
            prop = user_dictionary[a_property]

            vars = [None, None, None, None]
            for ID, a_var in enumerate(['min', 'max', 'soft_min', 'soft_max']):
                if a_var in prop.keys():
                    vars[ID] = user_dictionary[a_property][a_var]

            for a_type in [float]:
                if isinstance(prop['default_value'], a_type):
                    property_manager.update(min=vars[0], max=vars[1], soft_min=vars[2], soft_max=vars[3])
