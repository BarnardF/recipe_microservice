# Recipe Suggestion Microservice - Project Documentation

## Project Overview

A Flask microservice that accepts ingredient lists and returns ranked recipe suggestions with substitution recommendations. Built as a learning project for backend development, API design, and microservice architecture.

**Student**: Final-year Software Engineering student  
**Purpose**: Learn Flask, microservices, API design, backend fundamentals  
**End Goal**: Backend for mobile app (Flutter/React Native)  

## Core Functionality

### Current Scope (Flask Microservice)
- Accept list of user ingredients via URL parameters (comma-separated)
- Match ingredients against local recipe database (40+ recipes)
- Integrate with Spoonacular API for extended recipe suggestions
- Rank recipes by number of matching ingredients with tie-breaking logic
- Return hybrid results combining local and external API data
- JSON response format suitable for mobile client consumption

### Planned Features (Enhanced Microservice)
- POST endpoint with request body for complex queries
- Recipe substitution suggestions (e.g., cheese → nutritional yeast)
- Detailed recipe retrieval by ID
- Advanced scoring algorithm considering:
  - Ingredient overlap percentage
  - Difficulty level and preparation time
  - Available substitutions

## Current Implementation Status

### What's Working ✅ (Phase 2 Complete)
```python
# Enhanced data structure (40+ recipes across multiple cuisines)
recipes = {
    "Classic Pancakes": {
        "ingredients": ["Flour", "Egg", "Milk", "Sugar", "Baking powder", "Salt", "Butter"],
        "time": "20 min",
        "difficulty": "easy",
        "cuisine": "American",
        "meal_type": "breakfast"
    },
    # ... 40+ recipes covering breakfast, lunch, dinner, desserts
}

# Hybrid API Integration (Phase 2 Complete + Enhanced)
- Local recipe matching with percentage-based scoring algorithm
- Spoonacular API service layer with optimized ranking (maximum used ingredients)
- Intelligent filtering: Top 5 results for ≤3 ingredients, 40%+ match for more ingredients
- Normalized response format matching local and external API structures
- Combined response format with local + external results
- Error handling for API failures with graceful fallback to local recipes
- Environment-based configuration for API keys
- **NEW**: Web interface for easy testing and demonstration
```

### Flask Implementation ✅ (Phase 2 Complete)
```python
# Working Flask endpoints
@app.route('/')
def hello():
    # Basic server status endpoint

@app.route('/interface')
def interface():
    # Web interface for testing the API

@app.route('/find_recipe/<string:ingredients>')
def find_recipe(ingredients):
    # Hybrid approach with enhanced percentage-based matching
    # Format: /find_recipe/egg,cheese,milk
    # Returns combined JSON with local_recipes and spoonacular_recipes

@app.route('/test_api/<string:ingredients>')
def test_api(ingredients):
    # Testing endpoint for Spoonacular API integration
```

### Recent Achievements
1. **✅ Algorithm Optimization**: Set-based intersection for O(R × (I + U)) performance
2. **✅ Percentage-Based Matching**: **ENHANCED** - Smart filtering with match percentage calculation
3. **✅ Flask Migration**: Complete console-to-web API conversion with JSON responses
4. **✅ Enhanced Dataset**: 40+ recipes with comprehensive cuisine, meal type, and difficulty metadata
5. **✅ Professional Structure**: Organized codebase with proper Flask project architecture
6. **✅ Hybrid API Integration**: Spoonacular API fully integrated with local recipes
7. **✅ Environment Configuration**: Secure API key management with .env files
8. **✅ Error Handling**: Graceful fallback when external API is unavailable
9. **✅ Web Interface**: **NEW** - HTML interface for easy testing and demonstration
10. **✅ Intelligent Filtering**: **NEW** - Adaptive result filtering based on ingredient count

### Current Status & Next Steps
**Phase 2 Status**: ✅ **COMPLETED** - Hybrid API integration working
- ✅ Local recipe matching algorithm optimized
- ✅ Spoonacular API service layer implemented
- ✅ Hybrid response combining local + external results
- ✅ Error handling and graceful API fallback
- ✅ Environment-based configuration

**Ready for Phase 3**: Mobile Integration & Advanced Features

## Technical Architecture

### Phase 1: Console Application ✅ COMPLETED
**Status**: Complete  
**Achievements**: 
- ✅ Set-based ingredient matching algorithm (optimized performance)
- ✅ Tie-breaking logic implemented (match count → ingredient count)
- ✅ Business logic separated from display logic
- ✅ Matched ingredients tracking and display
- ✅ Comprehensive test coverage with enhanced dataset

### Phase 2: Flask Microservice & API Integration ✅ COMPLETED
**Status**: **Complete** - Ready for mobile integration

**Current Flask Implementation:**
```
recipe-microservice/
├── main.py                    # Flask application with hybrid endpoints + web interface
├── services/
│   └── spoonacular_service.py # External API integration service (enhanced)
├── data/
│   └── recipes.py            # Local recipe database (40+ recipes)
├── templates/
│   └── index.html           # Web interface for testing
├── config.py                 # Configuration management
├── .env                      # Environment variables (API keys)
├── requirements.txt          # Dependencies
├── .gitignore               # Version control exclusions
└── README.md                # Project documentation
```

**Completed Features:**
- ✅ Flask app with working hybrid endpoints and web interface
- ✅ URL parameter ingredient input (/find_recipe/egg,cheese,milk)
- ✅ **Spoonacular API integration** - Service layer with optimized ranking
- ✅ **Percentage-based matching** - Smart algorithm with match percentage calculation
- ✅ **Intelligent filtering** - Adaptive results based on ingredient count (≤3: top 5, >3: 40%+ match)
- ✅ **Normalized response format** - Unified structure for local and external results
- ✅ **Web interface** - HTML/CSS/JS frontend for testing and demonstration
- ✅ **Error handling** - Graceful fallback when API unavailable
- ✅ **Environment configuration** - Secure API key management
- ✅ JSON response formatting optimized for mobile client consumption
- ✅ Professional project structure with separation of concerns

### Phase 3: Mobile Integration & Advanced Features 🔄 READY TO START
**Next Priority Tasks:**
1. **Network Configuration** - Configure Flask for phone-to-PC communication
2. **Mobile Test Client** - Create simple mobile app or test scripts
3. **Enhanced Response Format** - Optimize JSON structure for mobile consumption
4. **POST Endpoint Implementation** - Add request body support for complex queries
5. **Recipe Detail Retrieval** - Individual recipe lookup by ID

**Planned Advanced Features:**
- Redis caching for frequent queries
- Fuzzy ingredient matching algorithms
- Recipe substitution suggestion engine
- SQLite/PostgreSQL database migration
- Docker containerization
- Comprehensive API documentation (Swagger/OpenAPI)

## API Endpoints (Current)

### Working Endpoints
```
GET /
# Basic server status check

GET /interface
# Web interface for testing the API (HTML frontend)

GET /find_recipe/<ingredients>
Example: /find_recipe/egg,cheese,milk
Response: {
    "query": "egg,cheese,milk",
    "local_recipes": [
        ["Cheese Omelette", {
            "total_matches": 2,
            "total_ingredients": 5,
            "matched_ingredients": ["egg", "cheese"],
            "match_percentage": 40.0
        }]
    ],
    "spoonacular_recipes": [
        {
            "title": "Perfect Cheese Omelet",
            "total_matches": 2,
            "total_ingredients": 6,
            "matched_ingredients": ["egg", "cheese"],
            "missed_ingredients": ["butter", "salt"],
            "match_percentage": 33.3,
            "spoonacular_id": 12345
        }
    ],
    "total_local": 3,
    "total_api": 5,
    "status": "local + spoonacular"
}

GET /test_api/<ingredients>
# Testing endpoint for raw Spoonacular API data
```

### Planned API Design (Phase 3)
```
POST /api/v1/recipes/suggest
Body: {
    "ingredients": ["egg", "flour", "milk"],
    "dietary_restrictions": ["vegetarian"], // optional
    "max_difficulty": "medium"              // optional
}

GET /api/v1/recipes/{recipe_id}
# Individual recipe details

GET /api/v1/recipes/search?q={query}
# Search recipes by name/cuisine
```

## Matching Algorithm

### Current Implementation (Enhanced Algorithm)
- **Local Matching**: Percentage-based scoring with set intersection operations
- **Intelligent Filtering**: Adaptive results based on ingredient count
  - ≤3 ingredients: Returns top 5 matches regardless of percentage
  - >3 ingredients: Returns only recipes with ≥40% ingredient match
- **Hybrid Results**: Combines local recipe matches with Spoonacular API results
- **Normalized Format**: Both local and external results use consistent structure
- **Ranking**: Primary by match percentage, secondary by total ingredients
- **Fallback**: Graceful degradation when external API unavailable
- **Web Interface**: Built-in HTML interface for testing and demonstration

### Algorithm Flow
```python
def find_recipe(ingredients):
    # 1. Parse and clean ingredient list
    ingredient_list = [ing.strip().lower() for ing in ingredients.split(',')]
    
    # 2. Get local recipe matches with percentage-based scoring
    local_results = get_local_recipes(ingredient_list)
    
    # 3. Query Spoonacular API with normalized response format
    api_results = get_spoonacular_recipes(ingredient_list)
    
    # 4. Apply intelligent filtering:
    #    ≤3 ingredients: top 5 results
    #    >3 ingredients: ≥40% match required
    
    # 5. Return hybrid response with consistent structure
    return combined_json_response
```

### Performance Characteristics
- **Local Search**: O(R × (I + U)) where R=recipes, I=ingredients, U=user_ingredients
- **Percentage Calculation**: Real-time match percentage scoring for precise ranking
- **Intelligent Filtering**: Adaptive result count based on ingredient specificity
- **API Integration**: External calls with normalized response processing
- **Memory Usage**: In-memory recipe storage with efficient set operations
- **Error Resilience**: Continues operation if external API fails
- **Web Interface**: Lightweight HTML/CSS/JS frontend for testing

## Technology Stack

### Current Implementation
- **Language**: Python 3.x
- **Framework**: Flask web framework
- **Data Storage**: In-memory dictionary (local recipes)
- **External APIs**: Spoonacular Recipe API
- **Configuration**: python-dotenv for environment management
- **HTTP Client**: requests library for API calls
- **Dependencies**: Flask, requests, python-dotenv

### Development Tools
- **Testing**: Built-in unittest framework
- **Version Control**: Git with .gitignore for secrets
- **Development Server**: Flask development server
- **API Testing**: URL-based testing via browser/curl

### Planned Additions
- **Caching**: Redis for frequent ingredient/recipe queries
- **Database**: SQLite → PostgreSQL migration
- **API Documentation**: Swagger/OpenAPI specification
- **Validation**: Marshmallow or Pydantic for request validation
- **Containerization**: Docker for deployment
- **Monitoring**: Logging and performance metrics

## Learning Objectives Achieved

### Backend Development ✅
- ✅ Flask application structure and best practices
- ✅ RESTful API design principles
- ✅ Microservice architecture patterns
- ✅ External API integration and error handling
- ✅ Environment-based configuration management

### Software Engineering ✅
- ✅ Code organization and separation of concerns
- ✅ Error handling and graceful degradation
- ✅ Version control with sensitive data protection
- ✅ Algorithm optimization and performance considerations

### Data & Algorithms ✅
- ✅ Recipe matching algorithms with set operations
- ✅ Performance optimization (nested loops → set intersection)
- ✅ Data modeling for recipes and ingredients
- ✅ Hybrid data source integration

## Development Priorities

### Phase 3: Mobile Integration (Immediate)
1. **Network Configuration** - Configure Flask host/port for mobile access
2. **Mobile Test Client** - Create simple client app or test scripts
3. **Enhanced JSON Format** - Optimize response structure for mobile consumption
4. **POST Endpoint** - Add request body support for complex queries
5. **Recipe Details API** - Individual recipe retrieval endpoint

### Performance & Production (Near-term)
1. **Caching Layer** - Redis implementation for frequent queries
2. **Database Migration** - SQLite integration for recipe storage
3. **API Documentation** - Swagger/OpenAPI specification
4. **Error Logging** - Comprehensive error tracking and monitoring
5. **Docker Containerization** - Production deployment preparation

### Advanced Features (Long-term)
1. **Recipe Substitution Engine** - Ingredient substitution suggestions
2. **Fuzzy Matching** - Flexible ingredient name matching
3. **User Preferences** - Dietary restrictions and preference learning
4. **Nutritional Information** - Integration with nutritional databases
5. **Production Deployment** - Cloud hosting and mobile app store deployment

## Success Metrics & Progress

### MVP (Minimum Viable Product) - ✅ ACHIEVED
- [x] **Console app with working ingredient matching** - Completed with optimized algorithms
- [x] **Flask API with basic endpoints** - Working server with URL parameter handling
- [x] **Simple recipe database** - Enhanced 40+ recipe dataset with metadata
- [x] **External API integration** - **NEW** - Spoonacular API fully integrated
- [x] **Hybrid response format** - **NEW** - Combined local + external results
- [x] **Error handling** - **NEW** - Graceful fallback for API failures
- [x] **Environment configuration** - **NEW** - Secure API key management
- [x] **Basic test coverage** - Algorithm and endpoint testing
- [x] **Documentation** - Comprehensive project documentation

### Phase 2 Complete ✅ - Ready for Mobile Integration
- [x] **Production-ready Flask microservice** - Core functionality complete with error handling
- [x] **Hybrid API integration** - Local + Spoonacular combination implemented
- [x] **Professional project structure** - Organized codebase with separation of concerns
- [x] **Comprehensive error handling** - API resilience and graceful degradation
- [x] **Enhanced response formatting** - JSON optimized for programmatic consumption
- [ ] **Mobile client connectivity** - Phone-to-PC networking configuration (Phase 3)
- [ ] **Mobile test application** - Client app development (Phase 3)

### Portfolio Readiness - 🔄 IN PROGRESS
**Current Status**: Backend microservice complete, ready for frontend integration

**Completed for Portfolio:**
- ✅ Flask microservice architecture
- ✅ External API integration (Spoonacular)
- ✅ Optimized algorithms and data structures
- ✅ Professional code organization
- ✅ Error handling and resilience
- ✅ Environment-based configuration
- ✅ Comprehensive documentation

**Next for Portfolio:**
- 🔄 Mobile client integration
- 🔄 Production deployment preparation
- 🔄 Advanced feature implementation

## Getting Started

### Prerequisites
- Python 3.x
- Spoonacular API key (optional - graceful fallback to local recipes)

### Setup
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with `SPOONACULAR_API_KEY=your_key_here` (optional)
4. Run: `python main.py`
5. Test web interface: `http://localhost:5000/interface`
6. Test API directly: `http://localhost:5000/find_recipe/egg,cheese,milk`

### API Usage
```bash
# Basic ingredient search
curl "http://localhost:5000/find_recipe/egg,milk,flour"

# Test external API integration
curl "http://localhost:5000/test_api/chicken,rice"

# Access web interface
open http://localhost:5000/interface
```

**Project Status**: Phase 2 Complete ✅ | Ready for Mobile Integration 🚀