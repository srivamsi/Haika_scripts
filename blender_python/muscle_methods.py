import bpy

def relink_muscleSystems(*args,**kwargs):
    target_rig_type = 'rigify'
    prefix = args[0]
    target_rig = None
    if args:
        target_rig = bpy.data.objects[args[1]]
    else:
        target_rig = kwargs.get('target_rig',bpy.context.active_object)

    left_muscles = ['pectoralis_major']

    for a_side in ['L','R']:
        for a_muscle_name in left_muscles:
            bpy.data.objects[f"{prefix}__{a_muscle_name} System__{a_side}"].parent = target_rig


relink_muscleSystems('kingB')
