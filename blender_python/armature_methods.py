import bpy


def attach_metarig_to_rigify(*args, **kwargs):
    sel_objs = bpy.context.selected_objects
    if len(sel_objs) > 2:
        raise Exception('selection exceeds limit.\n select only two armatures')

    if not args:
        metarig = bpy.context.active_object
        sel_objs.pop(sel_objs.index(metarig))
        rigify = sel_objs[0]
    else:
        metarig = bpy.data.objects[args[1]]
        rigify = bpy.data.objects[args[0]]
    debug = kwargs.get('debug', 0)

    con_suffix = '__' + (kwargs.get('constraint_suffix', 'MATCH'))

    print(f"rigify:{rigify.name}, meta:{metarig.name}")
    metarig_poseBones_names = [aBone.name for aBone in metarig.pose.bones]
    rigify_poseBones_names = [aBone.name for aBone in rigify.pose.bones]

    con = metarig.constraints.new(type='COPY_SCALE')
    con.target = rigify
    con.subtarget = 'root'
    con.name = f'COPY_SCALE{con_suffix}__CONSTRAINT'
    skipped_bones = []
    for meta_pose_bone_name in metarig_poseBones_names:
        rigify_pose_bone_name = 'DEF-' + meta_pose_bone_name
        if rigify_pose_bone_name in rigify_poseBones_names:
            metarig_bone = metarig.pose.bones[meta_pose_bone_name]
            rigify_bone = rigify.pose.bones[rigify_pose_bone_name]

            if debug:
                print(f"metaBone: {meta_pose_bone_name}; rigifyBone: {rigify_pose_bone_name}")

            for a_con_type in ['COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE']:
                con = metarig_bone.constraints.new(type=a_con_type)
                con.target = rigify
                con.subtarget = rigify_pose_bone_name
                con.name = f"{a_con_type}{con_suffix}__CONSTRAINT"
        else:
            skipped_bones.append(meta_pose_bone_name)

    print(f"cannot find matching bones for {len(skipped_bones)} bones they are:")
    for i in skipped_bones:
        print(i)


attach_metarig_to_rigify('rig', 'metarig')
