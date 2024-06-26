Viewers
=======


Examples
========

You can easily try out visualization programs using the examples found in `scikit-robot/examples <https://github.com/iory/scikit-robot/tree/main/examples>`_

.. code-block:: bash

    python robot_models.py --viewer trimesh


.. figure:: ../../image/robot_models.jpg
    :scale: 100%
    :align: center



CommandLine Tools
=================


You can easily visualize a URDF by providing it as an argument to the visualize-urdf command.


.. code-block:: bash

    visualize-urdf ~/.skrobot/pr2_description/pr2.urdf


.. figure:: ../../image/pr2.png
    :scale: 20%
    :align: center


Viewer classes
==============

TrimeshSceneViewer
------------------

**Description:**
  The ``TrimeshSceneViewer`` is an extension of the ``trimesh.viewer.SceneViewer`` tailored for visualizing 3D scenes using the Trimesh library. It is specifically designed for 3D triangle meshes visualization and manipulation in robotic applications.

**Key Functionalities:**

- **Initialization and Configuration:**
  Initializes with options for screen resolution and an update interval. It sets up a scene using Trimesh to manage various geometrical entities.

- **Rendering Control:**
  Manages redraws upon user interactions such as mouse clicks, drags, scrolls, and key presses. It also handles window resizing events to ensure the scene is accurately rendered.

- **Scene Management:**
  Supports dynamic addition and deletion of geometrical entities. It allows management of links and their associated meshes, enabling real-time updates based on robotic movements.

- **Camera Management:**
  Facilitates camera positioning and orientation, allowing for customizable views based on specified angles and transformations reflective of the robotic link configurations.

PyrenderViewer
--------------

**Description:**
  The ``PyrenderViewer`` utilizes the Pyrender library for advanced 3D rendering, ideal for creating realistic visual simulations. This viewer is particularly suited for complex rendering tasks in robotics, including detailed lighting and shading effects.

**Key Functionalities:**

- **Initialization and Configuration:**
  The viewer is initialized with specified resolution and rendering flags, creating a scene managed by Pyrender. It supports high-quality rendering features like raymond lighting.

- **Rendering Control:**
  Handles real-time scene updates triggered by user interactions such as mouse events and keyboard inputs, ensuring the scene remains interactive and up-to-date.

- **Scene Management:**
  Similar to ``TrimeshSceneViewer``, it allows for the addition and removal of visual meshes linked to robotic models, supporting dynamic updates to the scene as robotic configurations change.

- **Camera Management:**
  Offers detailed camera setup options, including angle adjustments, distance settings, center positioning, and field of view configuration, providing flexibility in viewing angles for complex scenes.


.. caution::

  To speed up the rendering cycle in **TrimeshSceneViewer** and **PyrenderViewer**, adjust the ``update_interval`` to the reciprocal of the desired frequency. For example, to achieve updates at 30 Hz, set the ``update_interval`` to 1/30. This change will increase the frequency at which the ``redraw()`` function is called, making the rendering process faster.

  Example usage:

  .. code-block:: python

    viewer = skrobot.viewers.TrimeshSceneViewer(resolution=(640, 480), update_interval=1.0/30)   # Set update interval for 30 Hz


Color Management
----------------

**Changing Colors:**

To enhance the visibility and distinction of different components in a robot model, users can change the colors of individual links or the entire robot. This can be done using the ``set_color`` method, which applies a specified RGBA color to the link. The ``reset_color`` method restores the original color of the link, allowing for easy toggling between custom and default visualizations.


.. code-block:: python

    import time
    from skrobot.viewers import TrimeshSceneViewer
    from skrobot.models import PR2
    import numpy as np

    viewer = TrimeshSceneViewer()
    robot_model = PR2()
    viewer.add(robot_model)
    viewer.show()

    # Setting the color to red with some transparency
    color = [255, 0, 0, 200]
    for link in robot_model.find_link_path(robot_model.rarm_root_link, robot_model.r_gripper_l_finger_tip_link) + robot_model.find_link_path(robot_model.rarm_root_link, robot_model.r_gripper_r_finger_tip_link):
        link.set_color(color)


.. figure:: ../../image/change-link-color.jpg
    :scale: 100%
    :align: center


.. code-block:: python

    # Resetting the color to default
    for link in robot_model.find_link_path(robot_model.rarm_root_link, robot_model.r_gripper_l_finger_tip_link) + robot_model.find_link_path(robot_model.rarm_root_link, robot_model.r_gripper_r_finger_tip_link):
        link.reset_color()


.. figure:: ../../image/reset-link-color.jpg
    :scale: 100%
    :align: center
