# Quickstart: Home Page Redesign

## Prerequisites
- Node.js 18+ installed
- npm or yarn package manager
- Docusaurus project already set up

## Setup Steps

### 1. Create Custom Home Page
```bash
# Create the pages directory if it doesn't exist
mkdir -p src/pages

# Create the custom home page
touch src/pages/index.js
```

### 2. Create Components Directory
```bash
# Create components directory for custom components
mkdir -p src/components/HomepageHeader src/components/HomepageFeatures
```

### 3. Add Images
```bash
# Create static images directory
mkdir -p static/img

# Add your module images to static/img/
# Examples: module1.jpg, module2.jpg, module3.jpg, module4.jpg
```

### 4. Install Dependencies (if needed)
```bash
# Most dependencies are already part of Docusaurus
npm install
```

### 5. Create the Implementation Files
Create the following files with appropriate content:
- `src/pages/index.js` - Main home page component
- `src/components/HomepageHeader/index.js` - Header with heading and paragraph
- `src/components/HomepageFeatures/index.js` - Module cards component
- Update `src/css/custom.css` with any custom styles

### 6. Run the Development Server
```bash
npm run start
```

## File Structure
```
src/
├── pages/
│   └── index.js
├── components/
│   ├── HomepageHeader/
│   │   └── index.js
│   └── HomepageFeatures/
│       └── index.js
└── css/
    └── custom.css

static/
└── img/
    ├── module1.jpg
    ├── module2.jpg
    ├── module3.jpg
    └── module4.jpg
```

## Verification
1. Visit http://localhost:3000
2. Confirm the heading "Physical AI & Humanoid Robotics Learning" appears
3. Verify the 6-7 line paragraph is displayed
4. Check that the "Getting Start" button is present and functional
5. Ensure 4 module cards are displayed with images and descriptions
6. Test responsive behavior on different screen sizes