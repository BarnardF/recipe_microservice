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
- Recipe substitution suggestions (e.g., cheese → nutritional yeast)
- Detailed recipe retrieval by ID
- Recipe scoring algorithm considering:
  - Ingredient overlap percentage
  - Difficulty level
  - Preparation time
  - Available substitutions

## Current Implementation Status

### What's Working (Console Version)
```python
# Current data structure
recipes = {
    "Apple Pie": {
        "ingredients": ["Flour", "Egg", "Milk", "Sugar", "Apple"],
        "time": "1 hour",
        "difficulty": "medium"
    },
    # ... more recipes
}

# Current algorithm
- Uses Python Counter to count ingredient matches
- Handles case-insensitive matching
- Processes comma-separated input with whitespace handling
- Ranks by match count using Counter.most_common()
```

### Current Limitations
1. **No tie-breaking**: When recipes have same match count, no secondary sorting
2. **No substitution logic**: Only exact ingredient matching
3. **Print-only output**: Functions print results instead of returning data (makes testing difficult)
4. **No ingredient display**: Shows match count but not which ingredients matched
5. **Basic test coverage**: Test file needs updating for current implementation

## Technical Architecture Plan

### Phase 1: Console Application (Current)
**Status**: In progress  
**Focus**: Core matching algorithm, data structures, basic functionality  

**Next Steps**:
- Implement tie-breaking (prefer fewer total ingredients)
- Separate display logic from business logic (for testability)
- Show which ingredients matched in output
- Update test suite

### Phase 2: Flask Microservice Migration
**Planned Structure**:
```
recipe-microservice/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models/
│   │   ├── __init__.py
│   │   └── recipe.py        # Recipe data models
│   ├── services/
│   │   ├── __init__.py
│   │   └── recipe_service.py # Business logic
│   ├── routes/
│   │   ├── __init__.py
│   │   └── recipes.py       # API endpoints
│   └── utils/
│       ├── __init__.py
│       └── helpers.py       # Utility functions
├── data/
│   └── recipes.json         # Initial recipe dataset
├── tests/
│   ├── __init__.py
│   └── test_recipes.py
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

### Phase 3: Advanced Features
- Redis caching for frequent queries
- External API integration (Spoonacular)
- Fuzzy ingredient matching
- AI-powered substitution suggestions
- SQLite/PostgreSQL database
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
- **Framework**: Console application → Flask
- **Data Storage**: In-memory dict → JSON → SQLite/PostgreSQL
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
1. **Console app** → Basic algorithm development
2. **Flask API** → Web service architecture
3. **Database integration** → Data persistence
4. **Caching layer** → Performance optimization
5. **External APIs** → Service integration
6. **Mobile backend** → Production-ready service

## Current Development Questions

### Immediate (Console Phase)
1. Implement tie-breaking for recipes with same match count?
2. Separate business logic from display logic for better testing?
3. Show which specific ingredients matched in output?

### Near-term (Flask Migration)
1. Best practices for Flask project structure?
2. How to design recipe data models?
3. API endpoint design patterns?

### Future Considerations
1. Redis caching strategy for ingredient queries?
2. Spoonacular API integration approach?
3. Substitution algorithm implementation?
4. Database schema design for scalability?

## Success Metrics

### MVP (Minimum Viable Product)
- [ ] Console app with working ingredient matching
- [ ] Flask API with basic endpoints
- [ ] Simple recipe database (JSON/SQLite)
- [ ] Basic test coverage
- [ ] Documentation and README

### Portfolio Ready
- [ ] Production-ready Flask microservice
- [ ] Redis caching implementation
- [ ] External API integration
- [ ] Comprehensive test suite
- [ ] API documentation
- [ ] Docker containerization
- [ ] GitHub repository with proper documentation

### Future Extension
- [ ] Mobile app integration
- [ ] User preference learning
- [ ] Advanced substitution algorithms
- [ ] Nutritional information integration
- [ ] Recipe image recognition