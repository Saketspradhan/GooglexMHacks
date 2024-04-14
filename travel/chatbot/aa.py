aa ={
  "destination": "Ann Arbor, MI",
  "budget": "$200",
  "duration": "3 days",
  "interests": ["Art", "local food"],
  "itinerary": [
    {
      "day": 1,
      "activities": [
        {
          "name": "Visit the University of Michigan Museum of Art",
          "cost": "free"
        },
        {
          "name": "Lunch at Zingerman's Deli",
          "cost": "$15"
        },
        {
          "name": "Explore Kerrytown Market & Shops",
          "cost": "free"
        },
        {
          "name": "Dinner at Sava's",
          "cost": "$25"
        }
      ]
    },
    {
      "day": 2,
      "activities": [
        {
          "name": "Visit the Ann Arbor Hands-On Museum",
          "cost": "$15"
        },
        {
          "name": "Lunch at Braun Court",
          "cost": "$10"
        },
        {
          "name": "Shop for souvenirs on Main Street",
          "cost": "varies"
        },
        {
          "name": "Dinner at The Earle",
          "cost": "$30"
        }
      ]
    },
    {
      "day": 3,
      "activities": [
        {
          "name": "Visit the Matthaei Botanical Gardens",
          "cost": "$10"
        },
        {
          "name": "Lunch at Arbor Brewing Company",
          "cost": "$15"
        },
        {
          "name": "Take a walk through the Nichols Arboretum",
          "cost": "free"
        },
        {
          "name": "Farewell dinner at Pizza House",
          "cost": "$20"
        }
      ]
    }
  ],
  "totalCost": "$180"
}
def format_itinerary():
    formatted_itinerary = ""
    for day in aa['itinerary']:
        formatted_itinerary += f"Day {day['day']}:\n"
        for activity in day['activities']:
            formatted_itinerary += f"  - {activity['name']} (Cost: {activity['cost']})\n"
        formatted_itinerary += "\n"
    return formatted_itinerary
