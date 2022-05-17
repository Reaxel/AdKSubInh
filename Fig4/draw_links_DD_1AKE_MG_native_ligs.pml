reinitialize
load 1ake.pdb
load DD_1AKE_MG_native.pdb
align DD_1AKE_MG_native, 1ake
delete  1ake
hide all
unset dynamic_measures
show cartoon, all
color grey90, all
run draw_links.py
draw_links ///A/215/C1*, ///A/10/CA, color=red, color2=red, radius=0.18, object_name=215:10_redAA
draw_links ///A/215/C1*, ///A/14/CA, color=red, color2=red, radius=0.18, object_name=215:14_redAA
draw_links ///A/215/C1*, ///A/84/CA, color=green, color2=green, radius=0.18, object_name=215:84_greenAA
draw_links ///A/215/C1*, ///A/133/CA, color=green, color2=green, radius=0.18, object_name=215:133_greenAA
draw_links ///A/216/C1*, ///A/31/CA, color=green, color2=green, radius=0.18, object_name=216:31_greenAA
draw_links ///A/216/C1*, ///A/33/CA, color=green, color2=green, radius=0.18, object_name=216:33_greenAA
draw_links ///A/216/C1*, ///A/35/CA, color=green, color2=green, radius=0.18, object_name=216:35_greenAA
draw_links ///A/216/C1*, ///A/36/CA, color=green, color2=green, radius=0.18, object_name=216:36_greenAA
draw_links ///A/216/C1*, ///A/49/CA, color=green, color2=green, radius=0.18, object_name=216:49_greenAA
draw_links ///A/216/C1*, ///A/52/CA, color=green, color2=green, radius=0.18, object_name=216:52_greenAA
draw_links ///A/216/C1*, ///A/53/CA, color=green, color2=green, radius=0.18, object_name=216:53_greenAA
draw_links ///A/216/C1*, ///A/57/CA, color=green, color2=green, radius=0.18, object_name=216:57_greenAA
draw_links ///A/216/C1*, ///A/58/CA, color=green, color2=green, radius=0.18, object_name=216:58_greenAA
draw_links ///A/216/C1*, ///A/59/CA, color=green, color2=green, radius=0.18, object_name=216:59_greenAA
draw_links ///A/216/C1*, ///A/61/CA, color=green, color2=green, radius=0.18, object_name=216:61_greenAA
draw_links ///A/216/C1*, ///A/64/CA, color=green, color2=green, radius=0.18, object_name=216:64_greenAA
draw_links ///A/216/C1*, ///A/68/CA, color=green, color2=green, radius=0.18, object_name=216:68_greenAA
draw_links ///A/216/C1*, ///A/84/CA, color=green, color2=green, radius=0.18, object_name=216:84_greenAA
draw_links ///A/216/C1*, ///A/86/CA, color=green, color2=green, radius=0.18, object_name=216:86_greenAA
draw_links ///A/216/C1*, ///A/87/CA, color=green, color2=green, radius=0.18, object_name=216:87_greenAA
draw_links ///A/216/C1*, ///A/88/CA, color=green, color2=green, radius=0.18, object_name=216:88_greenAA
draw_links ///A/216/C1*, ///A/89/CA, color=green, color2=green, radius=0.18, object_name=216:89_greenAA
draw_links ///A/216/C1*, ///A/92/CA, color=green, color2=green, radius=0.18, object_name=216:92_greenAA
draw_links ///A/216/C1*, ///A/120/CA, color=green, color2=green, radius=0.18, object_name=216:120_greenAA
draw_links ///A/216/C1*, ///A/123/CA, color=green, color2=green, radius=0.18, object_name=216:123_greenAA
draw_links ///A/216/C1*, ///A/159/CA, color=green, color2=green, radius=0.18, object_name=216:159_greenAA
draw_links ///A/216/C1*, ///A/164/CA, color=green, color2=green, radius=0.18, object_name=216:164_greenAA
draw_links ///A/216/C1*, ///A/167/CA, color=green, color2=green, radius=0.18, object_name=216:167_greenAA
zoom all
hide labels
sel lid, resi 122-160
sel nmp, resi 30-75
color red, lid
color blue, nmp
@set_view.pml
save draw_links_DD_1AKE_MG_native_ligs.png
