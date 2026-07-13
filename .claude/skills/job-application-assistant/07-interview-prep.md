# Interview Preparation Guide

<!-- SETUP: STAR examples are personalized by running /setup based on your actual experience -->

## STAR Format

Structure answers as: **Situation** (context), **Task** (your responsibility), **Action** (what you did), **Result** (outcome).

Keep answers to 1-2 minutes. Be specific. End with what you learned or would do differently.

## Ready-Made STAR Examples

### 1. Agentic RAG System (Generative AI & Semantic Search)
**S:** Organizations often fail to find precise answers within massive PDF/document archives due to standard keywords search limitations.
**T:** I needed to build a Retrieval-Augmented Generation pipeline to enable context-aware PDF question-answering and summarization.
**A:** I leveraged LangChain and the Gemini API, indexing document chunks into a Pinecone vector database for semantic similarity. I built ReAct agents to dynamically orchestrate retrieval and generation.
**R:** Successfully engineered a semantic answer engine with high-speed query resolution, showcasing expertise in vector databases, embeddings, and agentic workflows.
**Use for:** "Describe a time you worked with LLMs or GenAI", "How do you implement semantic search?"

### 2. NexCart (Full-Stack API & Data Validation)
**S:** Catalog systems require rigorous data constraints and interactive analytics dashboards to ensure business logic is consistent across inventory databases.
**T:** My goal was to build a full-stack product management database with auto-computed business schemas and live diagnostics.
**A:** I engineered a FastAPI backend with Pydantic v2 cross-field schema validation (auto-computing final_price, volume_cm3). I built a 5-module Streamlit interface with interactive Plotly analytics.
**R:** Produced a production-ready inventory tool that prevented invalid data entries and provided live telemetry of database states.
**Use for:** "Describe a full-stack project you engineered", "How do you handle API validation and dashboard design?"

### 3. NeuralPrice AI Laptop Predictor (Deep Learning & Cloud MLOps)
**S:** Laptop prices vary across thousands of configuration permutations, making manual pricing models slow and inaccurate.
**T:** I set out to build an end-to-end deep learning pipeline to predict laptop prices in real-time.
**A:** I trained a 4-layer ANN using TensorFlow, preprocessing 337 features via one-hot encoding. I containerized the entire application using Docker and deployed it to Hugging Face Spaces.
**R:** Deployed a reliable cloud inference model that processes live multi-currency (INR/USD/EUR) predictions.
**Use for:** "Tell me about a neural network model you built", "How do you containerize and deploy ML models?"

<!-- Add more STAR examples as needed. Aim for 4-6 covering different competencies. -->

## Common Tough Questions

### "Why did you leave [previous company]?"
> [PREPARE YOUR ANSWER - be honest, forward-looking, no negativity about former employer]

### "You don't have [specific skill/experience]."
> [PREPARE YOUR ANSWER - acknowledge the gap, bridge to adjacent experience, show willingness to learn]

### "Where do you see yourself in 5 years?"
> [PREPARE YOUR ANSWER - show ambition aligned with the role's growth path]

### "What's your biggest weakness?"
> [PREPARE YOUR ANSWER - genuine weakness with concrete mitigation strategy]

### "Why this company specifically?"
> Customize per company. Must reference: specific projects, company values, market position, or team structure. Never give a generic answer.

## Questions You Should Ask Interviewers

### About the Role
- "What does a typical week look like in this role?"
- "What would success look like in the first 6 months?"
- "What's the biggest challenge the team is facing right now?"

### About the Team
- "How big is the team, and how do you divide work?"
- "What does the development/project lifecycle look like, from idea to production?"
- "How do you onboard new team members?"

### About Tech & Growth
- "What's your current tech stack for [relevant area]?"
- "Is there room to grow into more architectural or strategic decisions?"
- "How does the team stay current with new tools and methods?"

### About Culture (use these to prevent disappointment)
- "How would you describe the team culture?"
- "What does professional development look like here?"
- "Is there flexibility for remote/hybrid work?"
- "What's the balance between development/new projects and maintenance work?"
- "How would you describe the leadership style in this team?"
- "What do people who thrive here have in common?"

## Phone/Video Interview Tips
- Have STAR examples written out (use this file)
- Keep a glass of water nearby
- Smile when speaking (it changes your tone)
- Ask for clarification if a question is vague
- It's OK to take 5 seconds to think before answering
- End with: "Is there anything else you'd like to know about my background?"

## After the Application (Best Practice)

### Follow-Up Etiquette
- **Don't call to "stand out"** or to learn more about the role post-submission - this risks a negative impression
- If the employer specified a timeline, respect it and wait
- If no timeline was given and significant time has passed (2+ weeks), a brief call to ask about status is acceptable
- If you have genuinely new, relevant information to share, a short follow-up is fine

### Thank-You Notes
- When you receive any update (interview invitation, rejection, or status update), send a brief thank-you message
- Express appreciation for their time and the process
- Keep it short (2-3 sentences)

## Roleplay Guidelines
When the user asks for interview practice:
1. Ask which role/company to simulate
2. Start with easy warm-up questions ("Tell me about yourself")
3. Progress to role-specific technical questions
4. Include 1-2 behavioral questions using the competencies from the job posting
5. End with a tough question or curveball
6. After each answer, give brief feedback: what worked, what to sharpen
7. Suggest which STAR example would work best for each question
