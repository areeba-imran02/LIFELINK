# LIFELINK — Multi-Agent Real-World Needs Coordination Platform

LIFELINK is a global-first multi-agent AI platform that turns a real-world need into a coordinated, verified action plan.

Instead of being a generic chatbot or marketplace, LIFELINK decomposes a user's request into specialized checks:
- Need understanding
- Service/resource discovery
- Business/provider matching
- Availability
- Location
- Cost
- Accessibility
- Trust/risk
- Coordination
- Follow-up

## Example
User:
"I need wheelchair-accessible transport for my elderly mother tomorrow morning."

LIFELINK produces:
1. Structured need
2. Matching provider/resource candidates
3. Availability assumptions or confirmed status when connected to a real provider source
4. Cost comparison
5. Accessibility requirements
6. Trust/risk notes
7. Recommended next actions
8. A coordination checklist

## Important demo limitation
This starter project does NOT claim real-time booking, payment, identity verification, or live provider availability unless a real integration is connected. The UI clearly labels demo/inferred data.

## Stack
- Python
- Streamlit
- Groq-compatible OpenAI SDK interface (optional)
- Rule-based multi-agent orchestration fallback
- JSON data layer
- Pytest
- Docker

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Optional:
```bash
export GROQ_API_KEY="your_key"
```

## Project structure
```text
LIFELINK/
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
├── LICENSE
├── .streamlit/config.toml
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── need_agent.py
│   ├── service_agent.py
│   ├── availability_agent.py
│   ├── location_agent.py
│   ├── cost_agent.py
│   ├── accessibility_agent.py
│   ├── trust_agent.py
│   ├── coordination_agent.py
│   └── followup_agent.py
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── llm.py
│   ├── registry.py
│   └── pipeline.py
├── data/
│   └── demo_resources.json
└── tests/
    └── test_pipeline.py
```

## Global-first positioning
Pakistan can be configured as the initial localization layer, but the architecture is country-agnostic: providers, currencies, languages, accessibility requirements, and service categories are represented as data rather than hard-coded assumptions.
