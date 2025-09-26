# Recipe Suggestion Microservice - Project Documentation

## Project Overview

A Flask microservice that accepts ingredient lists and returns ranked recipe suggestions with substitution recommendations. Built as a learning project for backend development, API design, and microservice architecture.

**Student**: Final-year Software Engineering student  
**Purpose**: Learn Flask, microservices, API design, backend fundamentals  
**End Goal**: Backend for mobile app (Flutter/React Native)  

## Core Functionality

### Current Scope (Console Application)
- Accept list of user ingredients (comma-separated input)
- Match ingredients against recipe database
- Rank recipes by number of matching ingredients
- Tie-breaking: prefer recipes with fewer total ingredients (easier to make)
- Display results with recipe details (time, difficulty, matched ingredients)

### Planned Features (Flask Microservice)
- RESTful API endpoints for ingredient matching
- Recipe substitution suggestions (e.g., cheese â†’ nutritional yeast)
- Detailed recipe retrieval by ID
- Recipe scoring algorithm considering:
  - Ingredient overlap percentage
  - Difficulty level
  - Preparation time
  - Available substitutions

## Current Implementation Status

### What's Working (Flask API + Console Version)
```python
# Enhanced data structure (40+ recipes)
recipes = {
    "Classic Pancakes": {
        "ingredients": ["Flour", "Egg", "Milk", "Sugar", "Baking powder", "Salt", "Butter"],
        "time": "20 min",
        "difficulty": "easy",
        "cuisine": "American",
        "meal_type": "breakfast"
    },
    # ... 40+ recipes covering various cuisines
}

# Optimized algorithm (Phase 1 Complete)
- Uses set intersection operations for O(R Ã— (I + U)) performance
- Handles case-insensitive matching with normalized string processing
- Implements tie-breaking: primary by match count, secondary by total ingredients
- Returns structured data suitable for JSON API responses
- Tracks both match count and specific matched ingredients
```

### Flask Implementation (Phase 2 In Progress)
```python
# Working Flask endpoint
@app.route('/find_recipe/<string:ingredients>')
def find_recipe(ingredients):
    # URL parameter approach: /find_recipe/egg,cheese,milk
    # Returns JSON with recipe rankings and match details
```

### Recent Achievements
1. **âœ… Algorithm Optimization**: Migrated from O(R Ã— I Ã— U) nested loops to O(R Ã— (I + U)) set operations
2. **âœ… Tie-breaking Logic**: Implemented secondary sorting by ingredient count (fewer = easier recipes)
3. **âœ… Flask Migration**: Successfully converted console app to web API with JSON responses
4. **âœ… Enhanced Dataset**: Expanded to 40+ recipes with cuisine, meal type, and difficulty metadata
5. **âœ… Professional Structure**: Organized codebase with proper Flask project architecture
6. **âœ… URL Parameter Handling**: Implemented ingredient input via URL parameters for easy testing

### Current Limitations
1. **Hybrid API Integration**: Spoonacular API service layer created but not yet integrated with main endpoint
2. **Response Format**: Current tuple-based JSON could be more user-friendly for mobile clients
3. **Network Configuration**: Not yet configured for phone-to-PC communication
4. **Error Handling**: Basic implementation without comprehensive API error management
5. **Mobile Client**: Test client for phone-to-PC communication not yet implemented

## Technical Architecture Plan

### Phase 1: Console Application âœ… COMPLETED
**Status**: Complete  
**Achievements**: 
- âœ… Set-based ingredient matching algorithm (optimized performance)
- âœ… Tie-breaking logic implemented (match count â†’ ingredient count)
- âœ… Business logic separated from display logic
- âœ… Matched ingredients tracking and display
- âœ… Comprehensive test coverage with enhanced dataset

### Phase 2: Flask Microservice Migration ðŸ”„ IN PROGRESS
**Status**: Core functionality implemented, API integration in development

**Current Flask Implementation:**
```
recipe-microservice/
├── main.py
├── services/
│   └── spoonacular_service.py
├── data/
│   └── recipes.py  - local recipes
├── config.py
├── .env
└── requirements.txt
    .gitignore
    recipe_finder.ipynb - different versions was tested here
```

**Completed:**
- âœ… Basic Flask app with working endpoints
- âœ… URL parameter ingredient input (/find_recipe/egg,cheese,milk)
- âœ… JSON response formatting with recipe rankings
- âœ… Professional project structure setup

**In Development:**
- ðŸ”„ Spoonacular API integration (hybrid local + external approach)
- ðŸ”„ Enhanced response format for mobile client consumption
- ðŸ”„ Error handling and API resilience
- ðŸ”„ Phone-to-PC network configuration

### Phase 3: Mobile Integration & Advanced Features ðŸ“‹ PLANNED
- Phone-to-PC networking setup (Flask host configuration)
- Mobile client application (test scripts â†’ basic mobile app)
- Hybrid API integration (local recipes + Spoonacular API)
- Enhanced response formatting for mobile consumption
- Redis caching for frequent queries
- Fuzzy ingredient matching
- Recipe substitution suggestions
- SQLite/PostgreSQL database migration
- Docker containerization
- API documentation (Swagger/OpenAPI)

## API Design (Planned)

### Core Endpoints
```
POST /api/v1/recipes/suggest
Body: {
    "ingredients": ["egg", "flour", "milk"],
    "dietary_restrictions": ["vegetarian"], // optional
    "max_difficulty": "medium"              // optional
}
Response: {
    "matches": [
        {
            "recipe_id": "pancakes_001",
            "name": "Simple Pancakes", 
            "match_score": 0.85,
            "matched_ingredients": ["egg", "flour", "milk"],
            "missing_ingredients": ["sugar"],
            "substitutions": [],
            "time": "20 min",
            "difficulty": "easy"
        }
    ],
    "suggestions": [
        {
            "recipe_id": "cake_001",
            "name": "Basic Cake",
            "match_score": 0.60,
            "substitutions": [
                {
                    "missing": "butter",
                    "substitute": "oil",
                    "confidence": 0.9
                }
            ]
        }
    ]
}

GET /api/v1/recipes/{recipe_id}
Response: {
    "recipe_id": "pancakes_001",
    "name": "Simple Pancakes",
    "ingredients": [
        {"name": "egg", "amount": "2", "unit": "pieces"},
        {"name": "flour", "amount": "200", "unit": "g"}
    ],
    "instructions": ["Step 1...", "Step 2..."],
    "prep_time": "5 min",
    "cook_time": "15 min",
    "difficulty": "easy",
    "servings": 4
}

GET /api/v1/recipes/search?q={query}&difficulty={level}
# Optional: Search recipes by name/cuisine
```

## Matching Algorithm Evolution

### Current (Phase 1)
- Count exact ingredient matches
- Sort by match count
- Basic tie-breaking by total ingredient count

### Planned (Phase 2)
- Percentage-based scoring (matches/total_required)
- Weighted scoring (common ingredients vs specialty items)
- Substitution factor in scoring
- Difficulty and time preferences

### Advanced (Phase 3)
- Fuzzy string matching for ingredient names
- Nutritional similarity for substitutions
- User preference learning
- Seasonal/availability factors

## Technology Decisions

### Current Stack
- **Language**: Python 3.x
- **Framework**: Console application â†’ Flask
- **Data Storage**: In-memory dict â†’ JSON â†’ SQLite/PostgreSQL
- **Testing**: unittest
- **Dependencies**: collections.Counter

### Planned Additions
- **Caching**: Redis (for frequent ingredient/recipe queries)
- **API Documentation**: Flask-RESTX or Swagger
- **Validation**: Marshmallow or Pydantic
- **Database**: SQLAlchemy ORM
- **External APIs**: Spoonacular API
- **Containerization**: Docker

## Learning Objectives

### Backend Development
- Flask application structure and best practices
- RESTful API design principles
- Microservice architecture patterns
- Database design and ORM usage
- Caching strategies with Redis

### Software Engineering
- Test-driven development
- Code organization and separation of concerns
- Error handling and validation
- API documentation
- Deployment considerations

### Data & Algorithms
- Recipe matching algorithms
- Ingredient substitution logic
- Performance optimization
- Data modeling for recipes and ingredients

## Portfolio Value

### Technical Skills Demonstrated
- Python backend development
- Flask microservice architecture
- API design and implementation
- Database integration
- Caching with Redis
- External API integration
- Testing and documentation

### Project Complexity Progression
1. **Console app** â†’ Basic algorithm development
2. **Flask API** â†’ Web service architecture
3. **Database integration** â†’ Data persistence
4. **Caching layer** â†’ Performance optimization
5. **External APIs** â†’ Service integration
6. **Mobile backend** â†’ Production-ready service

## Current Development Priorities

### Immediate (Phase 2 Completion)
1. **Complete Spoonacular API integration** with hybrid local + external approach
2. **Enhance response format** for mobile client compatibility  
3. **Configure networking** for phone-to-PC communication (Flask host settings)
4. **Implement error handling** for API failures and network issues
5. **Create mobile test client** for end-to-end validation

### Near-term (Phase 3 Planning) 
1. **Mobile app development** strategy (Flutter/React Native vs web app)
2. **Caching implementation** using Redis for frequent ingredient queries
3. **Database migration** from in-memory dict to SQLite/PostgreSQL
4. **Recipe substitution logic** development and testing
5. **Performance optimization** for production deployment

### Long-term Considerations
1. **Advanced matching algorithms** (fuzzy string matching, weighted scoring)
2. **User preference learning** and personalization features
3. **Nutritional information integration** and dietary restriction handling
4. **Deployment strategy** (Docker, cloud hosting, mobile app stores)
5. **API documentation and testing** for production readiness

## Success Metrics & Current Progress

### MVP (Minimum Viable Product)
- [x] **Console app with working ingredient matching** - Completed with optimized set operations
- [x] **Flask API with basic endpoints** - Working Flask server with URL parameter handling
- [x] **Simple recipe database** - Enhanced 40+ recipe dataset with metadata
- [ ] **Spoonacular API integration** - Service layer created, integration in progress
- [ ] **Mobile client connectivity** - Phone-to-PC networking configuration pending
- [x] **Basic test coverage** - Test suite updated for current implementation
- [x] **Documentation and README** - Comprehensive project documentation maintained

### Portfolio Ready (In Progress)
- [ ] **Production-ready Flask microservice** - Core functionality complete, error handling needed
- [ ] **Hybrid API integration** - Local + Spoonacular combination approach planned
- [ ] **Mobile client application** - Test client and mobile app development planned
- [ ] **Comprehensive test suite** - Basic tests complete, API integration tests needed
- [ ] **Enhanced response formatting** - JSON structure optimized for mobile consumption
- [ ] **Network configuration** - Phone-to-PC communication setup pending
- [ ] **GitHub repository documentation** - Project structure and setup instructions needed

### Advanced Features (Future)
- [ ] **Redis caching implementation**
- [ ] **Database integration** (SQLite â†’ PostgreSQL migration path)
- [ ] **Recipe substitution algorithms**
- [ ] **Docker containerization**
- [ ] **API documentation** (Swagger/OpenAPI)
- [ ] **Performance optimization and monitoring**