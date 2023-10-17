import numpy as np

def project_points(input_array):
    # extract the plane and projection type from the input
    plane_point = input_array[0, :3]
    plane_normal = input_array[0, 3:6]
    projection_type = 'parallel' if np.count_nonzero(input_array[0, 6:]) == 3 else 'perspective'
    if projection_type == 'parallel':
        projection_dir = input_array[0, 6:]
        # define the projection matrix for parallel projection
        projection_mat = np.identity(3) - np.outer(projection_dir, projection_dir) / np.linalg.norm(projection_dir)**2
    else:
        # define the projection matrix for perspective projection
        projection_mat = np.zeros((3, 4))
        projection_mat[:, :3] = np.identity(3) - np.outer(plane_normal, plane_normal) / np.linalg.norm(plane_normal)**2
        projection_mat[:, 3] = -np.dot(projection_mat[:, :3], plane_point)

    # project all the points
    points = input_array[1:]
    projected_points = np.zeros((points.shape[0], 9))
    for i, point in enumerate(points):
        # reshape point array into a 3x3
        point = point.reshape((3, 3)).T
        if projection_type == 'parallel':
            projected_point = np.dot(projection_mat, point)
        else:
            homogeneous_point = np.hstack((point, np.ones((3, 1))))
            projected_homogeneous_point = np.dot(projection_mat, homogeneous_point.T).T
            projected_point = projected_homogeneous_point[:, :3] / projected_homogeneous_point[:, 3:]

        # reshape projected_point array to (3, 3) and assign to corresponding index in projected_points array
        projected_points[i] = projected_point.reshape((1, 9))

    # return the projected points in the same format as the input
    return np.vstack((plane_point, plane_normal, input_array[0, 6:], projected_points))

input_array = np.loadtxt('class_input_1-2.txt')
print(project_points(input_array))
