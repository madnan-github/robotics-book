import React from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import styles from './styles.module.css';

export default function GetStartedButton() {
  return (
    <div className={clsx('container', styles.getStartedSection)}>
      <div className="row">
        <div className="col col--12 text--center">
          <div className={styles.centerButton}>
            <Link
              className={clsx('button button--secondary button--lg', styles.getStartedButton)}
              to="/docs/module1/intro">
              Getting Start
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}