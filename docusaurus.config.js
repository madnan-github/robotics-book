// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Robotic Learning Book',
  tagline: 'Physical AI & Humanoid Robotics Learning Platform',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://robotics-learning-book79.vercel.app',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For Vercel deployment, use '/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'madnan-github', // Usually your GitHub org/user name.
  projectName: 'robotics-learning-book', // Usually your repo name.

  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'ignore',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/madnan-github/robotics-learning-book/tree/main/',
        },
        blog: false, // Disable blog plugin
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/robotics-social-card.jpg',
      navbar: {
        title: 'Robotic Learning Book',
        logo: {
          alt: 'Robotic Learning Book Logo',
          src: 'img/robotics-logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Modules',
          },
          {
            href: 'https://github.com/madnan-github/robotics-learning-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Learning Modules',
            items: [
              {
                label: 'Module 1: ROS 2 Fundamentals',
                to: '/docs/module1/intro',
              },
              {
                label: 'Module 2: Digital Twin (Gazebo & Unity)',
                to: '/docs/module2/intro',
              },
              {
                label: 'Module 3: AI-Robot Brain (Isaac)',
                to: '/docs/module3/intro',
              },
              {
                label: 'Module 4: Vision-Language-Action',
                to: '/docs/module4/intro',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'ROS 2 Documentation',
                href: 'https://docs.ros.org/',
              },
              {
                label: 'NVIDIA Isaac',
                href: 'https://developer.nvidia.com/isaac',
              },
              {
                label: 'Gazebo Simulation',
                href: 'https://gazebosim.org/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Robotics Stack Exchange',
                href: 'https://robotics.stackexchange.com/',
              },
              {
                label: 'ROS Discourse',
                href: 'https://discourse.ros.org/',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/madnan-github/robotics-learning-book',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Robotic Learning Book. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;