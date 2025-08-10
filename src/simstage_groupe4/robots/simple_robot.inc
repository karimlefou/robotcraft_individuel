define laser ranger(
	sensor(
		range [0.0 5.6]
		fov 240.0
		samples 240
	)

	color "turquoise"
	size [0.08 0.08 0.2]

	block(
		points 4
		point[0] [0 0]
		point[1] [0 1]
		point[2] [1 1]
		point[3] [1 0]
		z [0 1]
	)
)

define simple_robot position(
	odom_error [0.03 0.03 0.00 0.05]
	localization "odom"
	size [0.5 0.5 0.15]
	gui_nose 1
	drive "diff"
	color "purple"
	block(
		points 8
		point[0] [0 1]       # pointe avant (flèche)
		point[1] [0.5 0.6]    # coin avant droit
		point[2] [0.6 0.2]    # milieu droit
		point[3] [0.4 -0.5]   # arrière droit
		point[4] [0 -0.3]     # centre arrière
		point[5] [-0.4 -0.5]  # arrière gauche
		point[6] [-0.6 0.2]   # milieu gauche
		point[7] [-0.5 0.6]   # coin avant gauche
		z [0 0.2] 
)

	laser(pose [0.23 0.0 -0.15 0.0])
)



