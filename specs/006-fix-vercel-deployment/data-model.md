# Data Model: Fix Vercel Deployment CSS and Links

## Entities

### Deployment Configuration
- **baseUrl**: String (required) - Base URL for the deployed site (e.g., '/', '/robotic-learning-book')
- **url**: String (required) - Full URL of the deployment site
- **assetPath**: String (required) - Path prefix for static assets
- **environment**: String (required) - Deployment environment (local, vercel, github-pages)

### Asset Reference
- **type**: String (required) - Asset type (css, js, image, font)
- **path**: String (required) - Path to the asset file
- **resolvedPath**: String (computed) - Path after base URL resolution
- **status**: String (required) - Loading status (pending, loaded, error)

### Navigation Link
- **source**: String (required) - Source page path
- **destination**: String (required) - Destination page path
- **resolvedDestination**: String (computed) - Path after base URL resolution
- **status**: String (required) - Link functionality status (working, broken)

## Relationships
- Deployment Configuration contains multiple Asset References
- Deployment Configuration contains multiple Navigation Links

## Validation Rules
- baseUrl must be a valid URL path format
- All Asset References must resolve to existing files
- All Navigation Links must point to valid destinations
- Asset paths must be relative to the static directory or use proper absolute paths

## State Transitions
- Asset Reference: pending → loaded (when asset loads successfully)
- Asset Reference: pending → error (when asset fails to load)
- Navigation Link: unknown → working (when link functions properly)
- Navigation Link: unknown → broken (when link fails to navigate)