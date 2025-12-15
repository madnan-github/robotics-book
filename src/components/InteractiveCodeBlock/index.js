import React, { useState } from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

/**
 * InteractiveCodeBlock Component
 *
 * A component for displaying executable code examples in the ROS2 learning module.
 * Provides syntax highlighting and an option to run the code in a simulated environment.
 */
const InteractiveCodeBlock = ({ children, language, title }) => {
  const [isRunning, setIsRunning] = useState(false);
  const [output, setOutput] = useState('');

  const handleRunCode = () => {
    setIsRunning(true);
    // In a real implementation, this would connect to a backend service
    // to execute the code in a safe environment
    setTimeout(() => {
      setOutput(`Simulated output for ${language || 'code'} execution\nExecution completed.`);
      setIsRunning(false);
    }, 1000);
  };

  return (
    <div className={clsx('code-block-wrapper', styles.wrapper)}>
      {title && <div className={clsx('code-block-title', styles.title)}>{title}</div>}
      <div className="code-block">
        <pre>
          <code className={language ? `language-${language}` : ''}>
            {children}
          </code>
        </pre>
      </div>
      <div className="code-block-controls">
        <button
          className={clsx('button button--secondary button--sm', styles.runButton)}
          onClick={handleRunCode}
          disabled={isRunning}
        >
          {isRunning ? 'Running...' : 'Run Code'}
        </button>
      </div>
      {output && (
        <div className={clsx('code-block-output', styles.output)}>
          <h6>Output:</h6>
          <pre><code>{output}</code></pre>
        </div>
      )}
    </div>
  );
};

export default InteractiveCodeBlock;