# Configuration Contracts: Vercel Deployment Fix

## Docusaurus Configuration Requirements

### Required Settings
- **baseUrl**: Must be set to '/' for Vercel deployment to ensure proper asset resolution
- **url**: Must match the Vercel deployment URL
- **onBrokenLinks**: Should be set to 'warn' or 'ignore' during fixes to allow deployment
- **onBrokenMarkdownLinks**: Should be set to 'warn' or 'ignore' during fixes to allow deployment

### Asset Handling
- All CSS files must be properly referenced in the `stylesheets` configuration
- Static assets must be placed in the `/static` directory
- Image paths in MDX files must be relative to the static directory

## Environment Consistency Contract

### Path Resolution
- All internal links must use relative paths or Docusaurus `Link` component
- Asset paths must resolve correctly both locally and in deployment
- Base URL must be handled consistently across all pages

### Validation Criteria
- CSS files load without 404 errors
- Images load correctly on all pages
- Navigation links direct to valid destinations
- Site maintains responsive design behavior