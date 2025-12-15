/**
 * @file InteractiveCodeBlock Component
 * @description A component for executable code examples in Docusaurus documentation
 */

import React from 'react';

/**
 * InteractiveCodeBlock Component
 *
 * A React component that renders code blocks with the ability to execute them in a simulated environment.
 * This is particularly useful for educational content where readers can experiment with code snippets.
 *
 * @param {Object} props - Component properties
 * @param {string} props.children - The code content to display
 * @param {string} props.className - Optional CSS class name for styling
 * @param {string} props.language - The programming language for syntax highlighting
 * @returns {JSX.Element} Rendered component
 */
const InteractiveCodeBlock = ({ children, className, language }) => {
  const [output, setOutput] = React.useState('');
  const [isLoading, setIsLoading] = React.useState(false);

  /**
   * Executes the provided code in a simulated environment
   * @async
   * @function executeCode
   * @description Simulates code execution for educational purposes
   */
  const executeCode = async () => {
    setIsLoading(true);

    // Simulate code execution delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    // For educational purposes, we'll simulate output based on the code content
    let simulatedOutput = '';

    if (typeof children === 'string') {
      if (children.includes('rclpy')) {
        simulatedOutput = 'Simulated ROS 2 node execution:\n- Node initialized\n- Publisher created\n- Messages published to topic\n- Spinning...\n(Use actual ROS 2 environment to run)';
      } else if (children.includes('print') || children.includes('console.log')) {
        // Extract print statements or console.log outputs
        const printMatches = children.match(/print\(([^)]+)\)/g) || children.match(/console\.log\(([^)]+)\)/g);
        if (printMatches) {
          simulatedOutput = printMatches.map(match => {
            const extracted = match.replace(/^(print|console\.log)\(/, '').replace(/\)$/, '');
            return `Output: ${extracted}`;
          }).join('\n');
        } else {
          simulatedOutput = 'Code executed successfully\n(Actual output would appear in ROS 2 environment)';
        }
      } else {
        simulatedOutput = 'Code structure validated\n(Use actual ROS 2 environment to run)';
      }
    } else {
      simulatedOutput = 'Code executed in simulated environment\n(Actual output would appear in ROS 2 environment)';
    }

    setOutput(simulatedOutput);
    setIsLoading(false);
  };

  // Extract language from className if not provided
  const codeLanguage = language || (className ? className.replace('language-', '') : 'python');

  return (
    <div className="interactive-code-block">
      <div className="code-header">
        <span className="language-indicator">{codeLanguage}</span>
        <button
          className="execute-button"
          onClick={executeCode}
          disabled={isLoading}
        >
          {isLoading ? 'Executing...' : 'Run Code'}
        </button>
      </div>
      <pre className={className}>
        <code>{children}</code>
      </pre>
      {output && (
        <div className="output-panel">
          <div className="output-header">Output:</div>
          <pre className="output-content">
            <code>{output}</code>
          </pre>
        </div>
      )}
      <style jsx>{`
        .interactive-code-block {
          margin: 1rem 0;
          border: 1px solid #ddd;
          border-radius: 8px;
          overflow: hidden;
        }

        .code-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f6f8fa;
          padding: 0.5rem 1rem;
          border-bottom: 1px solid #ddd;
        }

        .language-indicator {
          font-size: 0.875rem;
          font-weight: bold;
          color: #57606a;
        }

        .execute-button {
          background-color: #2ea44f;
          color: white;
          border: none;
          padding: 0.25rem 0.75rem;
          border-radius: 4px;
          cursor: pointer;
          font-size: 0.875rem;
        }

        .execute-button:hover:not(:disabled) {
          background-color: #2c974b;
        }

        .execute-button:disabled {
          background-color: #6e7781;
          cursor: not-allowed;
        }

        .output-panel {
          border-top: 1px solid #ddd;
          background-color: #f6f8fa;
        }

        .output-header {
          padding: 0.25rem 1rem;
          font-size: 0.875rem;
          font-weight: bold;
          color: #57606a;
          background-color: #eaecef;
        }

        .output-content {
          margin: 0;
          padding: 1rem;
          font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
          font-size: 0.875rem;
          line-height: 1.45;
          color: #24292f;
          background-color: transparent;
          overflow: auto;
        }
      `}</style>
    </div>
  );
};

export default InteractiveCodeBlock;