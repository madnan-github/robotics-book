# Data Model: Home Page Redesign

## Entities

### Home Page Content
- **Heading**: String (required) - The main heading "Physical AI & Humanoid Robotics Learning"
- **Description**: String (required) - 6-7 line paragraph about the topic
- **CallToAction**: Object
  - text: String (required) - Button text "Getting Start"
  - link: String (required) - Destination URL to textbook getting started section

### Module Card
- **id**: String (required) - Unique identifier for the module
- **title**: String (required) - Module name
- **description**: String (required) - Brief description of the module
- **imageUrl**: String (required) - Path to the relevant image
- **link**: String (required) - Link to the module's detailed page

## Relationships
- Home Page Content contains 4 Module Cards

## Validation Rules
- Home Page Heading must be exactly "Physical AI & Humanoid Robotics Learning"
- Description must be 6-7 lines of text
- Module Card title is required and must be unique
- Module Card description is required
- Module Card imageUrl is required and must point to a valid image asset
- Module Card link is required and must point to a valid internal page

## State Transitions
- Not applicable for static content