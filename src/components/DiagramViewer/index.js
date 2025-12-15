import React from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { useColorMode } from '@docusaurus/theme-common';

/**
 * DiagramViewer Component
 *
 * A component for displaying Mermaid.js diagrams in the ROS2 learning module.
 * Handles client-side rendering for dynamic diagram generation.
 */
const DiagramViewer = ({ chart, caption }) => {
  const { colorMode } = useColorMode();

  const renderDiagram = () => {
    // Dynamic import for client-side only
    return (
      <BrowserOnly fallback={<div>Loading diagram...</div>}>
        {() => {
          const { default: mermaid } = require('mermaid');

          // Setup mermaid configuration based on color mode
          mermaid.initialize({
            startOnLoad: true,
            theme: colorMode === 'dark' ? 'dark' : 'default',
            securityLevel: 'loose',
            fontFamily: 'inherit',
          });

          // Create a unique ID for the diagram container
          const diagramId = `mermaid-${Math.random().toString(36).substr(2, 9)}`;

          // Render the diagram after component mounts
          setTimeout(() => {
            try {
              mermaid.render(diagramId, chart, (svgCode) => {
                document.getElementById(diagramId).innerHTML = svgCode;
              });
            } catch (error) {
              console.error('Error rendering mermaid diagram:', error);
              document.getElementById(diagramId).innerHTML = '<div>Error rendering diagram</div>';
            }
          }, 100);

          return (
            <div className="mermaid-diagram-container">
              <div id={diagramId}></div>
              {caption && <div className="mermaid-caption">{caption}</div>}
            </div>
          );
        }}
      </BrowserOnly>
    );
  };

  return renderDiagram();
};

export default DiagramViewer;