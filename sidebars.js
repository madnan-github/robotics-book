// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro'],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'module1/intro',
        'module1/nodes_topics_services',
        'module1/rclpy_bridge',
        'module1/urdf_primer',
        'module1/assessment'
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'module2/intro',
        'module2/gazebo_physics',
        'module2/sensor_simulation',
        'module2/unity_hri',
        'module2/assessment'
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      items: [
        'module3/intro',
        'module3/isaac_sim',
        'module3/isaac_ros_vslam',
        'module3/nav2_humanoid',
        'module3/assessment'
      ],
      collapsed: false,
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      items: [
        'module4/intro',
        'module4/voice_to_action',
        'module4/cognitive_planning',
        'module4/vla_integration',
        'module4/assessment'
      ],
      collapsed: false,
    },
  ],
};

module.exports = sidebars;