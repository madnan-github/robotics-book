import React from 'react';
import Layout from '@theme/Layout';
import HomepageHeader from '@site/src/components/HomepageHeader';
import GetStartedButton from '@site/src/components/GetStartedButton';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

export default function Home() {
  return (
    <Layout
      title={`Home`}
      description="Physical AI & Humanoid Robotics Learning Platform">
      <HomepageHeader />
      <main>
        <GetStartedButton />
        <HomepageFeatures />
      </main>
    </Layout>
  );
}