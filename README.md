# Agentic RAG with Supervisor Agent Architecture

An intelligent multi-agent system that combines web search, knowledge graphs, and vector databases to provide comprehensive answers using a supervisor-coordinated approach.

## Architecture Overview

```
┌─────────────────────┐
│   Streamlit UI      │
│   (Chat Interface)  │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  Supervisor Agent   │
│  (Orchestrates &    │
│   Routes Queries)   │
└─────────┬───────────┘
          │
    ┌─────▼─────┐
    │           │
┌───▼──┐   ┌───▼──┐
│Search│   │  KG  │
│Agent │   │Agent │
└───┬──┘   └─┬─┬─┘
    │        │ │
┌───▼──┐     │ │
│Tavily│     │ │
│ API  │     │ │
└──────┘     │ │
           ┌─▼ ▼─┐
           │Neo4j│
           │  ┌─────────┐
           │  │Retrieve │
           │  │ Path    │
           │  └─────────┘
           │  ┌─────────┐
           │  │ Store   │
           │  │ Path    │
           │  └─────────┘
           └─────┘
```

## Agent Capabilities

### Search Agent
- **Tools**: `SearchEngine` (Tavily API)
- **Purpose**: Fetches real-time web search results
- **Prompt**: Optimized for search query formulation

### Knowledge Graph Agent  
- **Tools**: `get_vector_response`, `add_data_to_kg`
- **Purpose**: Manages Neo4j vector database interactions with dual pathways
- **Features**: 
  - **Retrieve Path**: Vector similarity search (`get_vector_response`)
  - **Store Path**: Dynamic knowledge graph updates (`add_data_to_kg`)

### Supervisor Agent
- **Role**: Orchestrates agent collaboration
- **Decision Logic**: Routes queries to appropriate agents
- **Output**: Synthesizes multi-agent responses


## Technical Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Orchestration** | LangGraph |
| **LLM Framework** | LangChain |
| **Search** | Tavily API |
| **Vector DB** | Neo4j |
| **Tracing** | LangSmith |

## Usage Examples

### Simple Query
```
User: "What are the latest developments in AI?"
→ Search Agent: Fetches recent AI news
→ KG Agent: Adds results to knowledge graph
→ Supervisor: Synthesizes comprehensive answer
```

### Knowledge Building
```
User: "Tell me about renewable energy trends"
→ Search Agent: Gets current market data
→ KG Agent: Updates knowledge base with findings
→ Future queries benefit from accumulated knowledge
```

## Customization

### Add New Agents
1. Create agent in `functions/agents.py`
2. Define tools in `functions/tools.py`  
3. Update supervisor configuration
4. Add to UI display logic

### Modify Prompts
- Edit `functions/prompts.py` for agent-specific instructions
- Adjust supervisor routing logic
- Customize response formatting

## Performance Tips

- **Caching**: Uses `@st.cache_resource` for supervisor
- **Streaming**: Consider streaming responses for better UX
- **Parallel Execution**: Agents can run concurrently when independent
- **Memory Management**: Neo4j connection pooling recommended

---

*Built with ❤️ using LangGraph, LangChain, and Streamlit*
