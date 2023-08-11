import bpy


def biped_defaults(*args, **kwargs):
    target_rig = None
    target_rig_data = None

    if args:
        target_rig = args[0]
    else:
        target_rig = kwargs.get('target_rig', bpy.context.active_object)

    target_rig_data = target_rig.data
    current_val = target_rig_data.layers[1]
    UI_hand_bones = ["upper_arm_parent.L", "upper_arm_parent.R"]
    UI_leg_bones = ["thigh_parent.L", "thigh_parent.R"]
    UI_bones = UI_hand_bones + UI_leg_bones

    # layer vis
    for a_layer_id in [1, 2, 4, 7,
                       9, 10, 12, 14, 15, 17, 18]:
        target_rig_data.layers[a_layer_id] = False

    # pole target vis
    for a_bone in UI_bones:
        if a_bone in target_rig.pose.bones.keys():
            target_rig.pose.bones[a_bone]["pole_vector"] = 1

    # IK - FK switch
    bpy.data.objects["rig"].pose.bones["upper_arm_parent.L"]["IK_FK"]
    for a_bone in UI_hand_bones:
        target_rig.pose.bones[a_bone]["IK_FK"] = 1.0
        target_rig.pose.bones[a_bone]["IK_Stretch"] = 0.0

    for a_bone in UI_leg_bones:
        target_rig.pose.bones[a_bone]["pole_parent"] = 6
        target_rig.pose.bones[a_bone]["IK_parent"] = 2
        target_rig.pose.bones[a_bone]["IK_Stretch"] = 0.0


biped_defaults()
