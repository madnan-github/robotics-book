/**
 * @file DiagramViewer Component
 * @description A component for displaying diagrams using Mermaid.js in Docusaurus documentation
 */

import React, { useEffect, useRef } from 'react';

/**
 * DiagramViewer Component
 *
 * A React component that renders diagrams using Mermaid.js.
 * This is particularly useful for educational content where readers can visualize
 * system architectures, flowcharts, and other diagrammatic representations.
 *
 * @param {Object} props - Component properties
 * @param {string} props.code - The Mermaid.js diagram definition code
 * @param {string} props.type - The type of diagram (flowchart, sequence, graph, etc.)
 * @param {string} props.title - Optional title for the diagram
 * @returns {JSX.Element} Rendered component
 */
const DiagramViewer = ({ code, type = 'graph', title }) => {
  const diagramRef = useRef(null);
  const containerRef = useRef(null);

  useEffect(() => {
    const renderDiagram = async () => {
      if (!containerRef.current || !code) return;

      // Dynamically import Mermaid
      const mermaid = await import('mermaid');

      // Initialize Mermaid with default configuration
      mermaid.default.initialize({
        startOnLoad: false,
        theme: 'default',
        flowchart: { useMaxWidth: true },
        securityLevel: 'loose', // Allow JavaScript execution in diagrams (use with caution in production)
      });

      try {
        // Clear previous content
        containerRef.current.innerHTML = '';

        // Generate diagram ID
        const diagramId = `mermaid-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;

        // Create the diagram container
        const diagramDiv = document.createElement('div');
        diagramDiv.id = diagramId;
        diagramDiv.className = 'mermaid-diagram';
        containerRef.current.appendChild(diagramDiv);

        // Insert the Mermaid code
        diagramDiv.textContent = `${type} ${code}`;

        // Render the diagram
        await mermaid.default.run({
          nodes: [diagramDiv],
          suppressErrors: true,
        });
      } catch (error) {
        console.error('Error rendering Mermaid diagram:', error);

        // Fallback: display the code as text if rendering fails
        containerRef.current.innerHTML = `
          <div class="mermaid-error">
            <h4>Diagram Preview</h4>
            <pre>${code}</pre>
            <p class="error-message">Note: Diagram could not be rendered. Install mermaid in your Docusaurus site.</p>
          </div>
        `;
      }
    };

    renderDiagram();
  }, [code, type]);

  return (
    <div className="diagram-viewer-container">
      {title && <h3 className="diagram-title">{title}</h3>}
      <div ref={containerRef} className="diagram-container" />
      <style jsx>{`
        .diagram-viewer-container {
          margin: 1.5rem 0;
          padding: 1rem;
          border: 1px solid #ddd;
          border-radius: 8px;
          background-color: #fff;
        }

        .diagram-title {
          margin-top: 0;
          margin-bottom: 1rem;
          color: #24292f;
          font-size: 1.125rem;
        }

        .diagram-container {
          min-height: 200px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .mermaid-diagram {
          width: 100%;
          text-align: center;
        }

        .mermaid-error {
          padding: 1rem;
          background-color: #f6f8fa;
          border-radius: 4px;
        }

        .mermaid-error pre {
          margin: 0.5rem 0;
          padding: 0.5rem;
          background-color: #eaecef;
          border-radius: 4px;
          overflow-x: auto;
        }

        .error-message {
          margin: 0.5rem 0 0 0;
          font-size: 0.875rem;
          color: #d73a49;
        }
      `}</style>
    </div>
  );
};

/**
 * MermaidDiagram Component
 *
 * A convenience wrapper around DiagramViewer specifically for Mermaid diagrams.
 * This component is designed to work with the code blocks found in MDX files.
 *
 * @param {Object} props - Component properties
 * @param {string} props.children - The Mermaid code content
 * @param {string} props.className - CSS class name (used to extract language)
 * @returns {JSX.Element} Rendered component
 */
export const MermaidDiagram = ({ children, className }) => {
  // Extract the code from children
  const code = typeof children === 'string' ? children.trim() : '';

  // Determine diagram type based on the first line of the code
  let diagramType = 'graph'; // default
  if (code.toLowerCase().startsWith('graph')) {
    diagramType = 'graph';
  } else if (code.toLowerCase().startsWith('flowchart')) {
    diagramType = 'flowchart';
  } else if (code.toLowerCase().startsWith('sequenceDiagram')) {
    diagramType = 'sequenceDiagram';
  } else if (code.toLowerCase().startsWith('gantt')) {
    diagramType = 'gantt';
  } else if (code.toLowerCase().startsWith('classDiagram')) {
    diagramType = 'classDiagram';
  } else if (code.toLowerCase().startsWith('stateDiagram')) {
    diagramType = 'stateDiagram';
  } else if (code.toLowerCase().startsWith('pie')) {
    diagramType = 'pie';
  } else if (code.toLowerCase().startsWith('erDiagram')) {
    diagramType = 'erDiagram';
  }

  return (
    <DiagramViewer
      code={code}
      type={diagramType}
      title="Diagram Visualization"
    />
  );
};

export default DiagramViewer;