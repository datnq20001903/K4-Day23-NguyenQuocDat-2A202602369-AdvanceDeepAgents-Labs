# Verify draft claims about modular routing, ReAct interaction, and function-call execution boundaries

```json
[
  {
    "id": "2205.00445",
    "url": "https://arxiv.org/abs/2205.00445",
    "title": "MRKL Systems A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning",
    "date": "unknown",
    "source": "web",
    "claims": [
      "MRKL proposes a system of multiple neural models complemented by discrete knowledge and reasoning modules; calling this modular/neuro-symbolic is supported.",
      "Its router is described conceptually as dispatching natural-language inputs to a suitable module; the output can either answer the user or be routed to another module.",
      "Calculators, currency converters, and database APIs are examples of symbolic modules, but the paper explicitly treats intelligent routing and extraction of module parameters as implementation challenges.",
      "The paper's abstract describes the architecture and technical challenges, not a demonstrated general guarantee of reliable routing across tools."
    ],
    "evidence": [
      "we define a flexible architecture with multiple neural models, complemented by discrete knowledge and reasoning modules.",
      "a router that routes every incoming natural language input to a module that can best respond to the input (the output of that module can be the output of the MRKL system, or be routed to another module).",
      "Symbolic, for example a math calculator, a currency converter or an API call to a database.",
      "There is also an interesting challenge of how to intelligently route input among modules, which we leave for a separate discussion.",
      "it must extract from the text discrete parameters required by the module."
    ],
    "limitations": [
      "Confirms the architectural description, but not any claim that routing is reliable, learned in a particular way, or universally applicable.",
      "Only relevant architecture and challenge excerpts were retrieved; no evaluation should be inferred from these excerpts."
    ]
  },
  {
    "id": "2210.03629",
    "url": "https://arxiv.org/abs/2210.03629",
    "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "date": "2023-03-10",
    "source": "web",
    "claims": [
      "ReAct interleaves reasoning traces with task-specific actions: reasoning helps induce, track, and update action plans, while actions enable interaction with external sources or environments and gathering information.",
      "The seed draft's description of an action/observation loop is consistent with ReAct's interactive setup; it should not be represented as mere one-shot tool invocation.",
      "ReAct evaluations cover question answering, fact verification, and interactive decision benchmarks including ALFWorld and WebShop; its reported gains are tied to those studied settings.",
      "The paper reports absolute success-rate gains of 34% and 10% over imitation and reinforcement-learning methods on ALFWorld and WebShop respectively, with one or two in-context examples."
    ],
    "evidence": [
      "generate both reasoning traces and task-specific actions in an interleaved manner",
      "reasoning traces help the model induce, track, and update action plans as well as handle exceptions",
      "actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.",
      "on two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples."
    ],
    "limitations": [
      "The fetched abstract supports the high-level loop and headline benchmark claims, not arbitrary tool compatibility, safe execution, or reliability beyond the named settings.",
      "The exact mechanics and semantics of observations should not be overgeneralized beyond the studied environments and task setups."
    ]
  },
  {
    "id": "OpenAI function calling guide",
    "url": "https://developers.openai.com/api/docs/guides/function-calling",
    "title": "Function calling",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The official guide specifies an application-mediated tool cycle: the application provides available tools; the model can return a tool-call request and arguments; application code executes the function and returns its output to the model.",
      "Function tools can be defined using JSON Schema; the guide also distinguishes custom tools that use free-form text inputs and outputs.",
      "The model's function call is a request/interface response, not evidence that the model itself executes the external function.",
      "This is an operational integration protocol, not a general agent architecture or empirical proof that requested actions are correct or safe."
    ],
    "evidence": [
      "we can include a list of tools the model could consider using.",
      "A function call or tool call refers to a special kind of response we can get from the model",
      "When the model calls a function, you must execute it and return the result.",
      "function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs."
    ],
    "limitations": [
      "Documentation establishes the described API workflow, not comparative performance or a complete theory of planning and reasoning.",
      "It does not by itself establish safety, permissions, validation, or successful execution; these should not be claimed as guaranteed by schema-based calling.",
      "The page provides no publication date in the retrieved text; date is unknown, and the documentation is version-sensitive."
    ]
  }
]
```

Synthesis: Draft claims are supported when narrowly framed: MRKL is a proposed modular neural/discrete architecture with a router, but routing and argument extraction remain challenges; ReAct interleaves reasoning and actions to gather observations and revise plans; function calling explicitly leaves execution to application code after the model requests a call. ReAct's benchmark results are context-specific.

Gaps: The supplied primary URLs and seed evidence do not support claims of universal routing quality, guaranteed ReAct correctness, or safe execution from function schemas. No need to introduce other architectures or recent evidence for this focused verification; the current official guide also has no displayed date in the retrieved text.