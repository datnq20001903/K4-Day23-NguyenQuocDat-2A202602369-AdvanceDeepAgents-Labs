# What are core paradigms for LLM agents using tools/actions, including CodeAct and AgentOptimizer?

```json
[
  {
    "id": "2402.01030",
    "url": "https://arxiv.org/abs/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-06-07",
    "source": "web",
    "claims": [
      "The primary arXiv record identifies arXiv:2402.01030 with the exact title Executable Code Actions Elicit Better LLM Agents.",
      "CodeAct uses executable Python as a unified action representation rather than limiting actions to predefined text or JSON calls; an interpreter runs actions and returns observations for multi-turn interaction and action revision.",
      "The paper evaluates 17 LLMs on API-Bank and a new benchmark, M3 ToolEval, comprising 82 human-curated multi-tool, multi-turn tasks; it reports up to 20% absolute success-rate improvement over alternatives on complex tasks.",
      "The paper also introduces CodeActInstruct, a dataset of 7,000 multi-turn interactions, and CodeActAgent models fine-tuned from LLaMA-2 and Mistral.",
      "The abstract says interpreter error messages support self-debugging in multi-turn tasks."
    ],
    "evidence": [
      "This work proposes to use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct).",
      "Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions.",
      "Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate).",
      "We curate a new benchmark consisting of 82 human-curated tasks",
      "CodeActInstruct that consists of 7k multi-turn interactions using CodeAct."
    ],
    "limitations": [
      "The reported maximum improvement is not a universal effect; the full paper describes task-dependent results and notes no improvement for the Llama-2 CodeActAgent variant in one reported comparison.",
      "Executable code broadens the action space, but the retrieved text does not establish that arbitrary code execution is safe; sandboxing and access-control requirements are not evaluated in these excerpts.",
      "The benchmark's task count is 82; the available excerpts do not establish broad real-world deployment validity."
    ]
  },
  {
    "id": "2402.11359",
    "url": "https://arxiv.org/html/2402.11359v4",
    "title": "Offline Training of Language Model Agents with Functions as Learnable Weights",
    "date": "unknown",
    "source": "hf-search",
    "claims": [
      "The primary paper text identifies the title as Offline Training of Language Model Agents with Functions as Learnable Weights; HF search independently associates identifier 2402.11359 with the different title Training Language Model Agents without Modifying Language Models, so the latter is not the title of the fetched version.",
      "AgentOptimizer is an offline agent-training method that changes an agent's function/tool set while leaving the base LLM weights unchanged.",
      "It uses execution histories and task outcomes to prompt an LLM optimizer to add, revise, or remove functions, rather than regenerating the entire function set.",
      "The training workflow evaluates on a training set each epoch and uses rollback after performance degradation and early stopping after repeated non-improving steps.",
      "The paper reports experiments across downstream tasks and says the method was integrated into AutoGen, but the fetched excerpts do not expose task-specific quantitative results."
    ],
    "evidence": [
      "we propose to progressively forge agent’s functions to better solve the downstream tasks instead of modifying the LLM weights.",
      "By treating the functions as learnable ‘agent parameters’",
      "the AgentOptimizer to perform one of the predefined function manipulation actions (add, revise, and remove)",
      "The former is to withdraw the current function updates if the performance over the training set is degraded",
      "We have integrated our method into AutoGen library."
    ],
    "limitations": [
      "The tool/tool-function discovery record reports a conflicting title for this identifier; the fetched primary paper title is used here, and metadata discrepancy remains unresolved.",
      "The available fetched portion did not include the complete experimental results, so no per-task metrics or effect sizes are asserted.",
      "Because function updates are guided by execution histories and training-task performance, evidence here does not establish generalization beyond the evaluated settings or rule out training-set overfitting."
    ]
  },
  {
    "id": "2210.03629",
    "url": "https://arxiv.org/abs/2210.03629",
    "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "date": "2023-03-10",
    "source": "web",
    "claims": [
      "ReAct interleaves language-model reasoning traces and task-specific actions, using observations from external sources to inform subsequent reasoning and actions.",
      "The paper evaluates question answering, fact verification, text-game interaction, and web navigation; its reported comparison includes absolute success-rate gains of 34% on ALFWorld and 10% on WebShop over cited imitation/reinforcement-learning baselines in the stated few-shot setting.",
      "The authors identify prompt-context limits for complex tasks with large action spaces as a limitation and suggest additional demonstrations, training, and reinforcement learning as future directions."
    ],
    "evidence": [
      "generate both reasoning traces and task-specific actions in an interleaved manner",
      "actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.",
      "with an absolute improvement of 34% and 10% respectively",
      "complex tasks with large action spaces require more demonstrations to learn well, which unfortunately can easily go beyond the input length limit"
    ],
    "limitations": [
      "These results concern the paper's specific benchmarks, models, prompts, and baselines and should not be treated as general performance guarantees.",
      "The retrieved evidence describes a prompting paradigm and does not establish safety or reliability of tool execution in deployment."
    ]
  },
  {
    "id": "2402.01030",
    "url": "https://huggingface.co/papers/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-02-01",
    "source": "hf-search",
    "claims": [
      "HF paper discovery independently associates arXiv identifier 2402.01030 with the exact CodeAct title.",
      "The HF summary characterizes CodeAct as using executable Python, dynamic action revision, and multi-turn interaction."
    ],
    "evidence": [
      "A framework using executable Python code for LLM agents",
      "dynamic action revision and multi-turn interactions."
    ],
    "limitations": [
      "HF's published date differs from the primary arXiv page's displayed publication/update date; the record is included to establish independent identity corroboration, not to resolve publication chronology.",
      "The summary is brief and cannot support detailed quantitative or methodological claims; those are grounded in the primary arXiv page."
    ]
  },
  {
    "id": "2402.11359",
    "url": "https://huggingface.co/papers/2402.11359",
    "title": "Training Language Model Agents without Modifying Language Models",
    "date": "2024-02-17",
    "source": "hf-search",
    "claims": [
      "HF search associates identifier 2402.11359 with the title Training Language Model Agents without Modifying Language Models, while the fetched primary paper page title is Offline Training of Language Model Agents with Functions as Learnable Weights.",
      "The HF summary describes a method that improves agents by updating functions without altering LLM weights and mentions rollback and early stopping."
    ],
    "evidence": [
      "Training Language Model Agents without Modifying Language Models",
      "updating agent functions without altering LLM weights, using techniques like roll-back and early-stop."
    ],
    "limitations": [
      "The title mismatch between HF metadata and the primary paper is an unresolved catalog/version discrepancy; identifier and primary fetched title are explicitly preserved.",
      "The HF summary supplies no task-specific scores or detailed evaluation protocol."
    ]
  }
]
```

Synthesis: Core paradigms span interleaved reasoning/action loops (ReAct), constrained API or text/JSON calls, executable code as a compositional action language (CodeAct), and learning the agent's tool/function inventory without changing model weights (AgentOptimizer). CodeAct changes the action interface at inference time; AgentOptimizer changes the available functions across offline training iterations, so they address distinct architectural layers and can in principle complement one another.

Evidence supports benchmark gains and mechanisms but does not establish deployment safety, robust generalization, or comparable head-to-head results across all paradigms. The AgentOptimizer identifier has a title discrepancy between HF metadata and the fetched primary text; exact per-task metrics were not available in the retrieved excerpt.