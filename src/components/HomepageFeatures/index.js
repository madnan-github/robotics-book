import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';

const FeatureList = [
  {
    title: 'Module 1: ROS 2 Fundamentals',
    description: 'Learn the basics of Robot Operating System 2, including nodes, topics, services, and the rclpy Python client library. Build your first ROS 2 applications and understand the core concepts that power modern robotics.',
    imageUrl: '/img/module1.jpg',
    link: '/docs/module1/intro',
    id: 'module1',
  },
  {
    title: 'Module 2: Digital Twin (Gazebo & Unity)',
    description: 'Explore digital twin technologies using Gazebo physics simulation and Unity for human-robot interaction. Create realistic simulation environments and test robotics algorithms in a safe, virtual space.',
    imageUrl: '/img/module2.jpg',
    link: '/docs/module2/intro',
    id: 'module2',
  },
  {
    title: 'Module 3: AI-Robot Brain (Isaac)',
    description: 'Dive into NVIDIA Isaac technologies including Isaac ROS visual SLAM, Isaac Sim for robotics simulation, and Nav2 for humanoid navigation. Build intelligent robot brains with advanced perception and navigation capabilities.',
    imageUrl: '/img/module3.jpg',
    link: '/docs/module3/intro',
    id: 'module3',
  },
  {
    title: 'Module 4: Vision-Language-Action',
    description: 'Implement Vision-Language-Action models for advanced robot interaction. Learn how robots can perceive, understand, and interact with the world using multimodal AI approaches.',
    imageUrl: '/img/module4.jpg',
    link: '/docs/module4/intro',
    id: 'module4',
  },
];

function Feature({ title, description, imageUrl, link, id }) {
  return (
    <div className={clsx('col col--3', styles.featureCard)}>
      <div className={styles.cardInner}>
        <Link to={link}>
          <h3 className={styles.cardTitle}>{title}</h3>
          <p className={styles.cardDescription}>{description}</p>
        </Link>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}