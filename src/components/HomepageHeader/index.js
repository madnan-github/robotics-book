import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const Heading = () => {
  return (
    <div className="text--center">
      <h1 className={clsx('hero__title', styles.mainHeading)}>
        Physical AI & Humanoid Robotics Learning
      </h1>
      <p className={clsx('hero__subtitle', styles.description)}>
        Welcome to the comprehensive learning platform for Physical AI and Humanoid Robotics.
        This educational resource provides in-depth modules covering the fundamentals of ROS 2,
        digital twin technologies, AI robot brains, and vision-language-action models.
        Whether you're a beginner or looking to advance your robotics knowledge,
        this platform offers structured learning paths with practical examples and hands-on exercises.
        Explore the modules below to begin your journey into the future of robotics and AI integration.
      </p>
    </div>
  );
};

export default function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading />
      </div>
    </header>
  );
}