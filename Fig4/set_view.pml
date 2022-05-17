set_view (\
    -0.991248369,   -0.060990244,   -0.117093273,\
    -0.129119098,    0.632885993,    0.763403594,\
     0.027546577,    0.771840334,   -0.635220706,\
    -0.000052676,    0.000022725, -135.870208740,\
    14.249032974,    8.542002678,   12.588933945,\
    76.360839844,  195.377532959,  -21.000000000 )
color gray90, all
color red, lid
color blue, nmp
set cartoon_transparency, 0.8
set cartoon_transparency, 0.8, lid
set cartoon_transparency, 0.8, nmp
select atp, resn ATP
show sticks, atp
color wheat, atp
select adp, resn ADP
show sticks, adp
color wheat, adp
select amp, resn AMP
show sticks, amp
color wheat, amp

set antialias, 2
set ray_opaque_background, on
bg_color white
ray 512, 512
